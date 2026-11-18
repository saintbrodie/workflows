import copy
import unittest

from validate_workflow_cosmetics import compare, load_json


def graph():
    return {"nodes": [{"id": 1, "type": "LoadImage", "pos": [0, 0],
                       "size": [200, 300], "mode": 4, "flags": {"collapsed": False},
                       "inputs": [{"name": "image", "type": "IMAGE", "link": 1}],
                       "widgets_values": ["example.png"], "properties": {"label": "keep"}}],
            "links": [[1, 1, 0, 2, 0, "IMAGE"]],
            "groups": [{"id": 1, "title": "Inputs", "bounding": [0, 0, 300, 400]}]}


class CosmeticValidationTests(unittest.TestCase):
    def setUp(self):
        self.original = graph()
        child = graph()
        child.update({"id": "subgraph", "name": "Protected Definition Name",
                      "inputs": [{"name": "prompt", "label": "Prompt"}],
                      "outputs": [], "widgets": []})
        child["definitions"] = {"subgraphs": [graph()]}
        self.original["definitions"] = {"subgraphs": [child]}

    def test_permits_only_cosmetics_at_all_depths(self):
        changed = copy.deepcopy(self.original)
        for g in (changed, changed["definitions"]["subgraphs"][0],
                  changed["definitions"]["subgraphs"][0]["definitions"]["subgraphs"][0]):
            g["nodes"][0].update(title="First Frame", color="#235B74", bgcolor="#142D3A")
            g["groups"][0].update(title="Input Frames", color="#235B74")
        changes = compare(self.original, changed)
        self.assertEqual(len(changes), 15)
        self.assertTrue(all(c["allowed"] for c in changes))

    def test_rejects_functional_fields_at_all_depths(self):
        mutations = [lambda g: g["nodes"][0]["pos"].__setitem__(0, 1),
                     lambda g: g["nodes"][0]["size"].__setitem__(1, 310),
                     lambda g: g["nodes"][0].__setitem__("mode", 0),
                     lambda g: g["nodes"][0].__setitem__("id", 2),
                     lambda g: g["nodes"][0].__setitem__("type", "SaveImage"),
                     lambda g: g["nodes"][0]["widgets_values"].__setitem__(0, "other.png"),
                     lambda g: g["nodes"][0]["flags"].__setitem__("collapsed", True),
                     lambda g: g["nodes"][0]["inputs"][0].__setitem__("name", "other"),
                     lambda g: g["nodes"][0]["properties"].__setitem__("label", "changed"),
                     lambda g: g["links"][0].__setitem__(1, 3),
                     lambda g: g["groups"][0]["bounding"].__setitem__(0, 5),
                     lambda g: g["nodes"].clear()]
        for depth in range(3):
            for mutate in mutations:
                with self.subTest(depth=depth, mutation=mutate):
                    changed = copy.deepcopy(self.original)
                    g = changed
                    for _ in range(depth):
                        g = g["definitions"]["subgraphs"][0]
                    mutate(g)
                    self.assertTrue(any(not c["allowed"] for c in compare(self.original, changed)))

    def test_preserves_interfaces_and_definition_names(self):
        for field, new in (("inputs", []), ("outputs", [{"name": "new"}]),
                           ("widgets", ["new"]), ("name", "New Name")):
            changed = copy.deepcopy(self.original)
            changed["definitions"]["subgraphs"][0][field] = new
            self.assertFalse(compare(self.original, changed)[0]["allowed"])

    def test_note_text_requires_opt_in_and_no_outputs(self):
        original = graph()
        original["nodes"][0].update(type="MarkdownNote", inputs=[], widgets_values=["Supply <Picture 1>."])
        changed = copy.deepcopy(original)
        changed["nodes"][0]["widgets_values"][0] = "Load <Picture 1> first."
        self.assertFalse(compare(original, changed)[0]["allowed"])
        self.assertTrue(compare(original, changed, allow_note_text=True)[0]["allowed"])
        original["nodes"][0]["outputs"] = [{"name": "STRING", "links": [1]}]
        changed["nodes"][0]["outputs"] = copy.deepcopy(original["nodes"][0]["outputs"])
        self.assertFalse(compare(original, changed, allow_note_text=True)[0]["allowed"])

    def test_reference_tokens_cannot_be_removed_or_changed(self):
        for new in ("Reference Image", "<picture 1>", "<Picture 2>"):
            original = graph()
            original["nodes"][0]["title"] = "<Picture 1>"
            changed = copy.deepcopy(original)
            changed["nodes"][0]["title"] = new
            self.assertFalse(compare(original, changed)[0]["allowed"])

    def test_rejects_invalid_cosmetics_and_hidden_metadata(self):
        for field, value in (("color", "red"), ("bgcolor", 123), ("title", ""),
                             ("label", "Not an allowed title")):
            changed = copy.deepcopy(self.original)
            changed["nodes"][0][field] = value
            self.assertFalse(compare(self.original, changed)[0]["allowed"])
        changed = copy.deepcopy(self.original)
        changed["nodes"][0]["properties"]["title"] = "Hidden change"
        self.assertFalse(compare(self.original, changed)[0]["allowed"])

    def test_distinguishes_booleans_and_numbers(self):
        changed = copy.deepcopy(self.original)
        changed["nodes"][0]["pos"][0] = False
        self.assertFalse(compare(self.original, changed)[0]["allowed"])

    def test_rejects_bad_json_and_malformed_graphs(self):
        for data in ('{"nodes":[],"nodes":[]}', '{"x":NaN}', '{"x":Infinity}', '{'):
            with self.assertRaises(ValueError):
                load_json(data)
        for data in ({"nodes": []}, {"nodes": {}, "links": []},
                     {"nodes": [], "links": [], "definitions": {"subgraphs": [None]}}):
            with self.assertRaises(ValueError):
                compare(data, data)

    def test_note_addition_requires_explicit_id_and_preserves_existing_data(self):
        changed = copy.deepcopy(self.original)
        note = {'id': 3, 'type': 'MarkdownNote', 'pos': [0, -400], 'size': [480, 360],
                'flags': {}, 'order': 3, 'mode': 0, 'inputs': [], 'outputs': [],
                'title': 'Quick Start', 'properties': {}, 'widgets_values': ['Load an image.'],
                'color': '#35414A', 'bgcolor': '#30343B'}
        changed['nodes'].append(note)
        changed['last_node_id'] = 3
        self.assertTrue(any(not c['allowed'] for c in compare(self.original, changed)))
        self.assertTrue(all(c['allowed'] for c in compare(self.original, changed, allow_root_note=3)))
        changed['nodes'][0]['mode'] = 0
        self.assertTrue(any(not c['allowed'] for c in compare(self.original, changed, allow_root_note=3)))
        note['outputs'] = [{'name': 'STRING', 'links': [1]}]
        with self.assertRaises(ValueError):
            compare(self.original, changed, allow_root_note=3)

    def test_mirrored_note_text_must_be_updated_together(self):
        original = copy.deepcopy(self.original)
        note = original["nodes"][0]
        note.update(type="MarkdownNote", inputs=[], outputs=[],
                    widgets_values=["Start with <Picture 1>."],
                    widgets_values_named={"text": "Start with <Picture 1>.", "other": "keep"})
        changed = copy.deepcopy(original)
        edited = changed["nodes"][0]
        edited["widgets_values"][0] = "Load <Picture 1> first."
        self.assertTrue(any(not c["allowed"] for c in compare(original, changed, allow_note_text=True)))
        edited["widgets_values_named"]["text"] = edited["widgets_values"][0]
        self.assertTrue(all(c["allowed"] for c in compare(original, changed, allow_note_text=True)))
        edited["widgets_values_named"]["other"] = "changed"
        self.assertTrue(any(not c["allowed"] for c in compare(original, changed, allow_note_text=True)))

    def test_node_and_socket_order_are_protected(self):
        original = graph()
        original["nodes"].append({"id": 2, "type": "SaveImage"})
        changed = copy.deepcopy(original)
        changed["nodes"].reverse()
        self.assertTrue(any(not c["allowed"] for c in compare(original, changed)))
        original["nodes"][0]["inputs"].append({"name": "second", "type": "IMAGE", "link": None})
        changed = copy.deepcopy(original)
        changed["nodes"][0]["inputs"].reverse()
        self.assertTrue(any(not c["allowed"] for c in compare(original, changed)))

    def test_root_layout_requires_opt_in_and_does_not_unlock_subgraphs(self):
        changed = copy.deepcopy(self.original)
        changed["nodes"][0]["pos"] = [20, 80]
        changed["nodes"][0]["size"] = [480, 360]
        changed["groups"][0]["bounding"] = [0, 0, 520, 460]
        self.assertTrue(any(not c["allowed"] for c in compare(self.original, changed)))
        self.assertTrue(all(c["allowed"] for c in compare(self.original, changed, allow_root_layout=True)))
        changed["definitions"]["subgraphs"][0]["nodes"][0]["pos"][0] = 20
        self.assertTrue(any(not c["allowed"] for c in compare(self.original, changed, allow_root_layout=True)))
        changed = copy.deepcopy(self.original)
        changed["nodes"][0]["mode"] = 0
        self.assertFalse(compare(self.original, changed, allow_root_layout=True)[0]["allowed"])

    def test_layout_opt_in_rejects_invalid_values_and_changed_array_shapes(self):
        for new in (True, "20", float("inf")):
            changed = copy.deepcopy(self.original)
            changed["nodes"][0]["pos"][0] = new
            self.assertFalse(compare(self.original, changed, allow_root_layout=True)[0]["allowed"])
        for new in (0, -20):
            changed = copy.deepcopy(self.original)
            changed["nodes"][0]["size"][0] = new
            self.assertFalse(compare(self.original, changed, allow_root_layout=True)[0]["allowed"])
        changed = copy.deepcopy(self.original)
        changed["nodes"][0]["pos"].append(10)
        self.assertFalse(compare(self.original, changed, allow_root_layout=True)[0]["allowed"])


if __name__ == "__main__":
    unittest.main()
