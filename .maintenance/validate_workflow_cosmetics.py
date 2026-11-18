"""Compare ComfyUI frontend workflows; fail on any non-cosmetic change."""

import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import re
import subprocess
import sys


MISSING = object()
COLOR = re.compile(r"#[0-9a-fA-F]{3}(?:[0-9a-fA-F]{3})?\Z")
REFERENCE_TOKEN = re.compile(r"<[^<>\r\n]+>")


def load_json(data):
    def unique_object(pairs):
        result = {}
        for key, value in pairs:
            if key in result:
                raise ValueError(f"Duplicate JSON key: {key}")
            result[key] = value
        return result

    def reject_constant(value):
        raise ValueError(f"Invalid JSON number: {value}")

    return json.loads(data, object_pairs_hook=unique_object,
                      parse_constant=reject_constant)


def pointer(path):
    return "/" + "/".join(str(p).replace("~", "~0").replace("/", "~1")
                           for p in path)


def graphs(value, path=()):
    """Find root and embedded definitions, including recursively nested ones."""
    if isinstance(value, dict):
        if not path or (len(path) >= 3 and
                        path[-3:-1] == ("definitions", "subgraphs")):
            yield path, value
        for key, child in value.items():
            yield from graphs(child, path + (key,))
    elif isinstance(value, list):
        for index, child in enumerate(value):
            yield from graphs(child, path + (index,))


def check_structure(document):
    if not isinstance(document, dict):
        raise ValueError("Expected a frontend workflow object")
    for path, graph in graphs(document):
        for field in ("nodes", "links"):
            if not isinstance(graph.get(field), list):
                raise ValueError(f"{pointer(path + (field,))}: expected an array")
        if not isinstance(graph.get("groups", []), list):
            raise ValueError(f"{pointer(path)}: groups must be an array")
        ids = set()
        for node in graph["nodes"]:
            if (not isinstance(node, dict) or type(node.get("id")) is not int
                    or not isinstance(node.get("type"), str)):
                raise ValueError(f"{pointer(path)}: invalid node id/type")
            if node["id"] in ids:
                raise ValueError(f"{pointer(path)}: duplicate node id {node['id']}")
            ids.add(node["id"])
        if any(not isinstance(group, dict) for group in graph.get("groups", [])):
            raise ValueError(f"{pointer(path)}: invalid group object")
    # A malformed definition must not escape graph discovery.
    def check_definitions(value):
        if isinstance(value, dict):
            if "definitions" in value:
                definitions = value["definitions"]
                if not isinstance(definitions, dict):
                    raise ValueError("definitions must be an object")
                subgraphs = definitions.get("subgraphs", [])
                if (not isinstance(subgraphs, list) or
                        any(not isinstance(g, dict) for g in subgraphs)):
                    raise ValueError("definitions.subgraphs must be an object array")
            for child in value.values():
                check_definitions(child)
        elif isinstance(value, list):
            for child in value:
                check_definitions(child)
    check_definitions(document)


def cosmetic_paths(original, allow_note_text=False, allow_root_layout=False, modified=None):
    allowed = {}
    modified_graphs = dict(graphs(modified)) if modified is not None else {}
    for path, graph in graphs(original):
        for index, node in enumerate(graph["nodes"]):
            base = path + ("nodes", index)
            for field in ("title", "color", "bgcolor"):
                allowed[base + (field,)] = (field, f"Node {node['id']} ({node['type']})")
            if allow_root_layout and not path:
                for field in ("pos", "size"):
                    for component in range(2):
                        kind = "layout_size" if field == "size" else "layout_position"
                        allowed[base + (field, component)] = (kind, f"Node {node['id']} ({node['type']})")
            values = node.get("widgets_values")
            if (allow_note_text and node["type"] in ("Note", "MarkdownNote")
                    and not node.get("inputs") and not node.get("outputs") and isinstance(values, list)
                    and values and isinstance(values[0], str)):
                named = node.get("widgets_values_named")
                if isinstance(named, dict) and named.get("text") == values[0]:
                    peer_nodes = modified_graphs.get(path, {}).get("nodes", [])
                    if index >= len(peer_nodes):
                        continue
                    peer = peer_nodes[index]
                    peer_values = peer.get("widgets_values")
                    peer_named = peer.get("widgets_values_named")
                    if (not isinstance(peer_values, list) or not peer_values
                            or not isinstance(peer_named, dict)
                            or peer_named.get("text") != peer_values[0]):
                        continue
                    allowed[base + ("widgets_values_named", "text")] = ("note", f"Note {node['id']}")
                elif named is not None:
                    continue
                allowed[base + ("widgets_values", 0)] = ("note", f"Note {node['id']}")
        for index, group in enumerate(graph.get("groups", [])):
            for field in ("title", "color"):
                allowed[path + ("groups", index, field)] = (
                    field, f"Group {group.get('id', index)}")
            if allow_root_layout and not path:
                for component in range(4):
                    kind = "layout_size" if component >= 2 else "layout_position"
                    allowed[("groups", index, "bounding", component)] = (
                        kind, f"Group {group.get('id', index)}")
    return allowed


def differences(before, after, path=()):
    if type(before) is not type(after):
        yield path, before, after
    elif isinstance(before, dict):
        for key in sorted(before.keys() | after.keys()):
            old, new = before.get(key, MISSING), after.get(key, MISSING)
            if old is MISSING or new is MISSING:
                yield path + (key,), old, new
            else:
                yield from differences(old, new, path + (key,))
    elif isinstance(before, list):
        if len(before) != len(after):
            yield path, before, after
        else:
            for index, (old, new) in enumerate(zip(before, after)):
                yield from differences(old, new, path + (index,))
    elif before != after:
        yield path, before, after


def compare(original, modified, allow_note_text=False, allow_root_layout=False, allow_root_note=None):
    check_structure(original)
    check_structure(modified)
    additions = []
    if allow_root_note is not None:
        if len(modified['nodes']) != len(original['nodes']) + 1:
            raise ValueError('Expected exactly one appended instructional note')
        note = modified['nodes'][-1]
        required = {'id', 'type', 'pos', 'size', 'flags', 'order', 'mode', 'inputs',
                    'outputs', 'title', 'properties', 'widgets_values', 'color', 'bgcolor'}
        if (set(note) != required or note['id'] != allow_root_note
                or note['id'] <= max([original.get('last_node_id', 0), *(n['id'] for n in original['nodes'])])
                or note['type'] not in ('Note', 'MarkdownNote')
                or note['inputs'] != [] or note['outputs'] != []
                or note['flags'] != {} or note['properties'] != {} or note['mode'] != 0
                or type(note['order']) is not int
                or not isinstance(note['title'], str)
                or not isinstance(note['widgets_values'], list)
                or len(note['widgets_values']) != 1
                or not isinstance(note['widgets_values'][0], str)
                or modified.get('last_node_id') != note['id']):
            raise ValueError('Only an explicitly authorized, unconnected instructional note may be appended')
        for key in ('pos', 'size'):
            if (not isinstance(note[key], list) or len(note[key]) != 2
                    or any(type(v) not in (int, float) or not math.isfinite(v)
                           or (key == 'size' and v <= 0) for v in note[key])):
                raise ValueError('Invalid note geometry')
        if any(not isinstance(note[k], str) or not COLOR.fullmatch(note[k]) for k in ('color', 'bgcolor')):
            raise ValueError('Invalid note colors')
        for path, old, new in [(('nodes', len(original['nodes'])), MISSING, note),
                               (('last_node_id',), original.get('last_node_id', MISSING), note['id'])]:
            additions.append({'path': pointer(path), 'object': 'Authorized instructional note addition',
                              'before_present': old is not MISSING, 'before': None if old is MISSING else old,
                              'after_present': True, 'after': new, 'scope': 'note addition',
                              'allowed': True, 'reason': 'Explicitly authorized note addition'})
        modified = dict(modified, nodes=modified['nodes'][:-1])
        if 'last_node_id' in original:
            modified['last_node_id'] = original['last_node_id']
        else:
            modified.pop('last_node_id', None)
    allowed = cosmetic_paths(original, allow_note_text, allow_root_layout, modified)
    changes = []
    for path, old, new in differences(original, modified):
        kind, label = allowed.get(path, (None, "Protected workflow data"))
        reason = "Allowed cosmetic field" if kind else "Field is outside the cosmetic allowlist"
        permitted = kind is not None
        if permitted and kind.startswith("layout_"):
            reason = "Explicitly allowed root layout field"
            if type(new) not in (int, float) or not math.isfinite(new):
                permitted, reason = False, "Layout coordinates must be finite numbers"
            elif kind == "layout_size" and new <= 0:
                permitted, reason = False, "Layout dimensions must be positive"
        elif permitted and new is not MISSING:
            if not isinstance(new, str):
                permitted, reason = False, "Cosmetic values must be strings"
            elif kind in ("color", "bgcolor") and not COLOR.fullmatch(new):
                permitted, reason = False, "Expected a hex color"
            elif kind == "title" and not new.strip():
                permitted, reason = False, "Display titles must not be blank"
        if kind in ("title", "note"):
            old_tokens = Counter(REFERENCE_TOKEN.findall(old)) if isinstance(old, str) else Counter()
            new_tokens = Counter(REFERENCE_TOKEN.findall(new)) if isinstance(new, str) else Counter()
            if old_tokens != new_tokens:
                permitted, reason = False, "Model reference identifiers must remain exact"
        changes.append({"path": pointer(path), "object": label,
                        "before_present": old is not MISSING,
                        "before": None if old is MISSING else old,
                        "after_present": new is not MISSING,
                        "after": None if new is MISSING else new,
                        "scope": "root layout" if kind and kind.startswith("layout_") else "cosmetic",
                        "allowed": permitted, "reason": reason})
    return changes + additions


def display_value(change, side):
    if not change[side + "_present"]:
        return "(absent; ComfyUI default)"
    return json.dumps(change[side], ensure_ascii=False)


def markdown_report(results):
    lines = ["# Workflow Presentation Validation", "",
             "This comparison checks JSON structure and unchanged saved data. It does not prove runtime functionality or visual quality.", "",
             "Visual inspection is a separate user review. No workflow execution was performed by this validator.", ""]
    for result in results:
        changes = result["changes"]
        blocked = sum(not c["allowed"] for c in changes)
        lines.extend([f"## {result['workflow']}", "",
                      f"Result: **{'FAIL' if blocked else 'PASS'}** — {len(changes)} changed fields; {blocked} unauthorized changes.", "",
                      f"Original: `{result['source']}`", "",
                      "Layout allowance: " + ("explicit root-only positions, sizes, and group bounds; embedded layouts remain protected." if result.get("allow_root_layout") else "none; all positions, sizes, and group bounds are protected."), "",
                      f"Instructional note text allowance: {'enabled' if result.get('allow_note_text') else 'disabled'}.", "",
                      f"Instructional note addition allowance: {result.get('allow_root_note') or 'none'}.", "",
                      f"Original SHA-256: `{result['before_sha256']}`", "",
                      f"Modified SHA-256: `{result['after_sha256']}`", "",
                      "| JSON Pointer | Object | Before | After | Result |",
                      "| --- | --- | --- | --- | --- |"])
        for c in changes:
            cells = [c["path"], c["object"], display_value(c, "before"),
                     display_value(c, "after"), ("Allowed (Layout)" if c["scope"] == "root layout" else "Allowed") if c["allowed"] else "REJECTED: " + c["reason"]]
            lines.append("| " + " | ".join(v.replace("|", "\\|").replace("\n", "<br>") for v in cells) + " |")
        lines.append("")
    return "\n".join(lines)


def check_path(path):
    path = Path(path)
    if any(part.lower() == "archive" for part in path.resolve().parts):
        raise ValueError("archive/ is excluded")
    if path.name.lower() == ".index.json" or path.suffix.lower() != ".json":
        raise ValueError("Expected a workflow JSON; .index.json is excluded")
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="+", help="Original and modified files, or root filenames with --base-ref")
    parser.add_argument("--base-ref", help="Compare root workflow files to this Git commit/ref")
    parser.add_argument("--allow-note-text", action="store_true", help="Allow text-only edits in existing, output-free Note/MarkdownNote nodes; requires manual content review")
    parser.add_argument("--allow-root-layout", action="store_true", help="Explicitly allow root node positions/sizes and existing root group bounds; embedded layouts remain protected")
    parser.add_argument("--allow-root-note", type=int, help="Explicitly authorize exactly one appended, unconnected instructional note with this ID")
    parser.add_argument("--report", type=Path, help="Write every changed field to a Markdown report")
    args = parser.parse_args()
    root = Path(__file__).resolve().parent.parent
    results = []
    try:
        if args.base_ref:
            commit = subprocess.run(["git", "rev-parse", "--verify", "--end-of-options",
                                     args.base_ref + "^{commit}"], cwd=root, check=True,
                                    capture_output=True, text=True).stdout.strip()
            pairs = []
            for name in args.paths:
                path = check_path(name)
                if path.is_absolute() or path.parent != Path("."):
                    raise ValueError("--base-ref accepts active root filenames only")
                before = subprocess.run(["git", "show", f"{commit}:{name}"], cwd=root,
                                        check=True, capture_output=True).stdout
                pairs.append((name, f"{commit}:{name}", before, (root / path).read_bytes()))
        else:
            if len(args.paths) != 2:
                raise ValueError("Supply ORIGINAL.json MODIFIED.json, or use --base-ref")
            before_path, after_path = [check_path(p) for p in args.paths]
            pairs = [(after_path.name, str(before_path), before_path.read_bytes(), after_path.read_bytes())]
        for name, source, before, after in pairs:
            changes = compare(load_json(before), load_json(after), args.allow_note_text, args.allow_root_layout, args.allow_root_note)
            results.append({"workflow": name, "source": source, "changes": changes,
                            "before_sha256": hashlib.sha256(before).hexdigest(),
                            "allow_root_layout": args.allow_root_layout,
                            "allow_note_text": args.allow_note_text,
                            "allow_root_note": args.allow_root_note,
                            "after_sha256": hashlib.sha256(after).hexdigest()})
        report = markdown_report(results)
        print(report)
        if args.report:
            if args.report.suffix.lower() != ".md" or any(p.lower() == "archive" for p in args.report.resolve().parts):
                raise ValueError("Reports must be Markdown outside archive/")
            args.report.write_text(report, encoding="utf-8")
    except (ValueError, OSError, subprocess.CalledProcessError) as error:
        print(f"ERROR: {error}", file=sys.stderr)
        return 2
    return 1 if any(not c["allowed"] for r in results for c in r["changes"]) else 0


if __name__ == "__main__":
    sys.exit(main())
