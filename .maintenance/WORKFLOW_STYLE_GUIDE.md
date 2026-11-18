# Workflow Style Guide

Status: **approved**. This is the authoritative presentation and naming reference for active workflows. The user approved the shared lighter-charcoal body, semantic colored headers with yellow settings accents, concise labels, and I2V pilot layout/Quick Start treatment. The approved presentation conventions now apply across all 21 active workflows. Historical pilot reports record earlier iterations; `WORKFLOW_VALIDATION.md` and `WORKFLOW_ROLLOUT.md` describe the current rollout.

## Purpose and Scope

Make each workflow readable as a creative tool: recognize inputs, adjust settings, understand previews, and find saved results. Use concise names and a few consistent color cues. Preserve the workflow's technical architecture and model-specific behavior.

Routine presentation work covers active root-level workflow JSON and their embedded subgraphs. Completely exclude `archive/`; do not read, audit, validate, reformat, or modify its contents. Do not edit `.index.json` or rename workflow files. Klein Dataset Maker and MiniMax reference-to-video workflows were excluded from the pilot only; they are included in the approved presentation rollout.

## Approved Semantic Palette

Use `color` for the node title bar and `bgcolor` for the node body. Every explicitly styled node uses the same **charcoal body `#30343B`**. Put semantic color in the header rather than filling the whole card with it. This shared surface gives inputs, settings, previews, and outputs one consistent visual style. The charcoal is slightly lighter than the canvas so card edges remain visible.

Existing groups use the category's title color, except **settings groups use the lighter yellow `#D2B16F`**. ComfyUI renders the group heading with its group color, so group headings need a lighter tone than node headers. The user requested a return to yellow settings accents while retaining the shared charcoal bodies; the blue, violet, green, and slate headers remain unchanged.

| Purpose | Node Title Color | Node Background | Examples |
| --- | --- | --- | --- |
| Inputs and reference media | Blue `#235B74` | Charcoal `#30343B` | First Frame, Reference Image, Prompt |
| Artist-adjustable settings | Yellow `#715B2D` | Charcoal `#30343B` | Seed, Duration (Seconds), LoRA Settings |
| Previews and comparisons | Violet `#594A72` | Charcoal `#30343B` | Generation Preview, Enhanced Prompt Preview, Video Details |
| Final outputs and exports | Green `#2B644C` | Charcoal `#30343B` | Save Video, Save Image, Export Audio |
| Technical processing | Slate `#35414A` | Charcoal `#30343B` | Resize First Frame, internal conversion nodes, sampling groups |

The common dark surface separates content from the colored headers and keeps large preview/output cards from becoming blocks of tinted color. Retain ComfyUI's text rendering; do not change global themes or widget styles. Check readability in the artist's actual theme before approval. Colors supplement names and never encode required instructions on their own.

Apply colors selectively:

- Emphasize the main inputs, adjustable controls, previews, and save nodes.
- Give mixed-purpose cards the header color of their principal artist interaction. The pilot's `Image to Video (MiniMax H3)` card uses a yellow header because it exposes the prompt and generation controls together. Its sockets and widget labels remain unchanged.
- Leave ordinary technical nodes with ComfyUI's default appearance. Use neutral gray to replace misleading existing custom colors or identify technical groups; do not paint every processing node.
- A generated video assembly node is processing, not an export. Use green for the actual save/export destination.
- A linked value conversion is processing, not an artist setting. `Duration to Text` has a slate header; the duration control has a yellow header. Both use the same charcoal body.
- Preserve all bypass, mute, collapse, and pin states. ComfyUI may dim bypassed nodes; do not change their execution state to make a color more visible. Its bypass tint can override this palette.

## Naming and Capitalization

Use Title Case for visible node titles and group names, with short connecting words such as "to", "and", and "of" lowercase. Preserve official spelling and capitalization: **MiniMax H3**, **FLUX.2**, **LoRA**, **ComfyUI**, **LTX**, **LTX-2.5**, **Qwen**, **SeedVR2**, **Ollama**, **SageAttention**, and **RTX**. Preserve intentional model/version punctuation rather than forcing every family into one spelling.

Prefer labels describing what the artist supplies, changes, or receives. Remove implementation prefixes such as `Float`, `Boolean`, `String`, and `Primitive` from display titles when they add no useful meaning. Retain technical terms inside technical pipelines when they identify the real operation.

| Avoid | Prefer | Reason |
| --- | --- | --- |
| Float (duration) | Duration (Seconds) | Clear control and units |
| Boolean (Enable Prompt Enhance) | Use Prompt Enhancement | Describes the choice |
| PE Switch | Prompt Enhancement Switch | Removes an unexplained abbreviation |
| Turbo Boolean | Use Turbo | Describes the control |
| Prompt Enhance Output | Enhanced Prompt Preview | Identifies a readout |
| Video Info | Video Details | Consistent result label |
| Frame Rate(int) | Frame Rate (FPS) | Useful units instead of data type |
| height | Height (Pixels) | Consistent capitalization and units, when confirmed |
| Lora Switch | LoRA Switch | Preserves official capitalization |
| Decoding and create video | Video and Audio Assembly | Names the pipeline stage |

Use consistent labels for equivalent controls: `First Frame`, `Last Frame (Optional)`, `Prompt`, `Seed`, `Duration (Seconds)`, `Frame Rate (FPS)`, `Width (Pixels)`, `Height (Pixels)`, `Resolution (Megapixels)`, `Enhanced Prompt Preview`, and `Save Video`. Confirm the actual unit and optional behavior before applying a label. Distinguish requested duration from calculated `Video Duration (Seconds)`; do not imply they are numerically identical.

Do not rename a node's internal `type`, `properties`, socket `name`/`label`/`localized_name`, widget identifier, or saved value. Do not rename subgraph definition `name`, descriptions, or interface metadata in a cosmetic pass. Override the instance's node `title` when a clearer visible label is needed.

## Protected Terminology and Identifiers

Model prompt syntax is literal data. Preserve `<Picture 1>`, `<Picture 2>`, `<Video 1>`, `<Audio 1>`, and every other numbered reference exactly, including brackets, capitalization, spaces, and numbering. A label containing one of these identifiers is not an invitation to translate it to "Reference Image".

The active MiniMax reference-to-video workflow uses numbered picture, video, and audio labels. These files were outside the initial pilot but are included in the approved presentation rollout. The I2V pilot does not contain such reference-tag titles; it still requires the same protection for prompts and any future identifiers.

Preserve structured MiniMax prompt fields such as `integrated_multimodal_description`, `overall_soundscape`, and `non_diegetic_music`. Keep timeline notation, parser keys, placeholders, model paths, filenames, trigger words, task codes, and reference ordering unchanged. For example, Bernini's `rv2v`, `r2v`, `image0`, and `reference_image` are syntax, not prose requiring Title Case.

Treat group names matched by group bypassers, Get/Set names, and title-based extension lookups as potentially functional. Confirm they are display-only before editing; otherwise preserve and flag them. When uncertain, retain the original identifier and record an exception.

## Existing Groups and Layout

Use the conceptual hierarchy **Inputs → Settings → Processing → Outputs** to choose names and colors. Presentation-only cleanup preserves layouts by default. The user's follow-up explicitly authorizes a separate layout pilot on the I2V main canvas; embedded layouts remain unchanged.

Name existing groups for their contents. Use blue for inputs, light yellow `#D2B16F` for controls, violet for preview/comparison areas, green for exports, and slate for processing or a mixed processing/results area. Preserve group IDs, font sizes, flags, order, and membership behavior. Do not add groups, collapse subgraphs, or change exposed controls. Changing positions, dimensions, or group bounds requires an explicit layout request and validation with the separate layout allowance.

### Approved Layout Measurements

The I2V root layout uses the following measurements in canvas units, independent of zoom:

| Property | Proposed Measurement |
| --- | --- |
| Alignment grid | 20 px for node positions, widths, and heights |
| Group side/bottom padding | 20 px from the outermost node body |
| Group top inset | Node body begins 80 px below group top: 30 px group heading + 20 px clearance + 30 px node title bar |
| Horizontal gap between cards | 40 px |
| Visible vertical gap between consecutive cards | 30 px minimum; next body normally starts 60 px after the previous body ends, allowing for its 30 px title bar. A card outside a group can sit farther below to preserve membership. |
| Gap between adjacent groups | 60 px |
| Primary card width | 480 px for media, generation, preview, and results |
| Compact settings width | 320 px |
| First/last frame card height | 360 px each |
| Generation/live preview/save card height | 600 px each |
| Seed / LoRA / metadata / prompt-preview body heights | 100 / 160 / 140 / 420 px respectively |

Align the primary row of node bodies at the same Y coordinate. Fit each existing group to its contents; a compact settings group need not stretch to match a media group. Use equal sizes for equivalent cards, and content-specific heights for different roles. Avoid forcing technical nodes or image/video previews into dimensions that clip controls or obscure media.

For this pilot, the original groups retain their original node membership. `Enhanced Prompt Preview` stays outside the generation group and aligns below its generation card. `Video Details` stays in the generation group, below `Save Video`. No embedded node positions or sizes change. Future layouts should preserve membership and existing flow unless a separate structural change is explicitly requested.

## Instructional Notes

Give every active workflow one **Quick Start** note on the main canvas. Name it **Quick Start** or use the workflow name followed by **Quick Start**.

- **What It Does** explains the result in one or two plain-language sentences.
- **How to Use** gives a short numbered sequence. Tell readers what to load or type, which controls matter on the first run, and where to see or find the result. Use the exact visible node labels and distinguish required inputs from optional branches.
- Keep installation steps, download links, model requirements, limits, and advanced settings under a separate reference heading or in supplemental notes. Preserve literal reference tags, model filenames, prompt syntax, and other identifiers.
- Reuse an existing overview note where practical. Place new notes to the left of the main graph with at least 60 px of clearance from nodes and groups. Start at 480 × 360 canvas units and size the note for its text. Use a slate header `#35414A` and a charcoal body `#30343B`.
- Edit only genuine instructional Note or MarkdownNote nodes. When an export contains both positional and named note text, update both copies together. Add nodes as part of explicit documentation work. Keep functional text widgets and existing graph layout intact.

## Applying the Standard to Existing Workflows

1. Confirm the approved scope and read this guide. Preserve an original file or identify its Git base commit before editing.
2. Inspect root nodes and embedded definitions. Identify the artist's entry points, controls, previews, and save destination, plus labels that may be consumed by models or extensions.
3. Make focused edits to node `title`/`color`/`bgcolor` and existing group `title`/`color`. Leave other fields unchanged unless a separate layout request explicitly permits positions, sizes, or group bounds. Preserve existing JSON formatting; do not load and reserialize the whole file for convenience.
4. Run the validator against the original, inspect every reported change, and review any note edits for preserved meaning.
5. Inspect the main canvas and relevant subgraphs in ComfyUI, checking text fit, colors, discoverability, and preserved bypass presentation. Obtain visual-design approval before rollout.

For new workflows, use the same vocabulary and palette as they are authored. Include a brief Quick Start note to the left of the workflow describing its purpose, inputs, main controls, optional branches, and output location. This authoring convention does not authorize adding nodes during a cosmetic-only cleanup. A request to create or functionally develop a workflow may authorize new nodes and logic; a cosmetic cleanup never does. Keep functional changes separate from presentation maintenance.

## Validation and Review

The dependency-free Python validator compares all fields recursively. Its only default exceptions are node `title`, `color`, `bgcolor` and group `title`, `color` at recognized graph locations. This includes nested `definitions.subgraphs`. Arrays retain their order, and every unlisted field must remain identical. It rejects duplicate JSON keys and malformed graph containers and reports a nonzero exit status on errors or unauthorized changes.

Run the validator and its tests from the repository root:

```powershell
python -B .maintenance/validate_workflow_cosmetics.py ORIGINAL.json MODIFIED.json
python -B -m unittest discover -s .maintenance -p "test_validate_workflow_cosmetics.py" -v
```

For the I2V pilot against the original baseline, enable the explicitly authorized layout and note changes:

```powershell
python -B .maintenance/validate_workflow_cosmetics.py --base-ref 53eeee7ba97a9d9cd0e62dcf8064785cec990a07 "Minimax H3 i2v.json" --allow-root-layout --allow-root-note 372
```

`--allow-root-layout` permits only numeric components of existing root node `pos`/`size` arrays and root group `bounding` arrays, in addition to the cosmetic allowlist. It rejects non-finite coordinates, non-positive dimensions, changed array lengths, and every embedded layout change. Execution fields, interfaces, widgets, flags, links, node counts, and processing data remain protected. Group containment and overlap require a separate geometry review; the flag does not authorize structural changes. `PILOT_LAYOUT_REVIEW.md` records the earlier layout revision; `PILOT_COLOR_REVIEW.md` isolates the latest unified card-style revision; `PILOT_VALIDATION.md` reports the current complete comparison with the Git baseline.

For two saved files, use `python -B .maintenance/validate_workflow_cosmetics.py ORIGINAL.json MODIFIED.json`. With `--base-ref`, pass explicit active root filenames; the script never crawls directories. It refuses `archive/` and `.index.json` paths.

`--allow-note-text` permits changes to the first text widget of existing unconnected `Note`/`MarkdownNote` nodes. For exports with mirrored `widgets_values_named.text`, both copies must match. All other widgets remain protected. Reference tokens in changed titles/notes must remain exact. This opt-in cannot prove that prose retains every requirement or that an extension never inspects a title: manual review is still required. Use it only for a requested documentation edit.

Review checklist:

- Only explicitly scoped active workflow JSON changed; archive files, `.index.json`, and filenames remain untouched.
- Every reported field is cosmetic or an explicitly authorized root layout component. Prompts, models, widget defaults, links, execution states, interfaces, and all embedded geometry remain identical.
- With layout authorization, margins/gaps are consistent, nodes do not overlap, equivalent cards match, and group membership is preserved. Without that authorization, all geometry remains identical.
- Official names, reference identifiers, parser syntax, and extension-dependent names remain intact.
- Colors distinguish artist actions; processing does not compete with input and result cues.
- Titles are concise and legible at the reviewed sizes. Units and optional labels match actual behavior.
- Visual review is completed by the user in ComfyUI. A parsing or comparison pass is not a runtime test or visual approval.

Maintain this guide when a new design convention receives user approval. `AGENTS.md` points future sessions here; README links contributors to the maintenance standard.

### Explicit Instructional Note Addition

The user requested the Quick Start note after reviewing the visual pilot. `--allow-root-note 372` permits exactly one appended, unconnected Note/MarkdownNote with that ID and its `last_node_id` update. All existing nodes, links, widget values, and execution fields still undergo the normal strict comparison. Without this explicit flag, adding a node is rejected. See `PILOT_NOTE_REVIEW.md` for the note addition and `PILOT_VALIDATION.md` for the full current comparison.

## Rollout Exceptions

- CharacterSheet's Fast Groups Bypasser uses `matchColors: cyan`. Its five `#8AA` accelerator group colors remain exact. Never recolor those groups or change the selector to force palette uniformity during cosmetic cleanup.
- Group names in Klein Face Maker and CharacterSheet remain exact because group-control behavior is more important than capitalization. Other group colors follow the palette where no selection depends on them.
- Keep `Text String (User Prompt)` in Krea2, `Input Text (Prompt)` in CharacterSheet, and LTX's documented `Load First Frame` / `Load Last Frame` names until their instructional references can be updated in a separately reviewed note edit. Bernini's note title likewise retains its documented wording.
- The follow-up notes pass added or revised every workflow’s Quick Start. It preserved download links, model requirements, and reference syntax. Never change definition names or interfaces to normalize them.
- The original layout exception applies only to MiniMax I2V. For note-only changes, preserve existing positions, sizes, and group bounds. Enable the addition allowance only for the ID of a newly appended note.

To reproduce the current full check, compare each active root filename to baseline commit `53eeee7ba97a9d9cd0e62dcf8064785cec990a07`. Use `--allow-note-text` for edited notes and the per-file `--allow-root-note ID` recorded in `WORKFLOW_VALIDATION.md` for appended notes. Only MiniMax I2V additionally requires `--allow-root-layout`. The report lists every changed field. New maintenance should use the actual pre-edit revision as its comparison base.
