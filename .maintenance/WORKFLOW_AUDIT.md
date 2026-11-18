# Active Workflow Presentation Audit

## Scope and Status

Baseline: Git commit `53eeee7ba97a9d9cd0e62dcf8064785cec990a07`, branch `codex/workflow-design-pilot`.

Inspected the **21 active root-level workflow JSON files** and their embedded subgraphs: **69 graphs, 889 nodes, 142 groups, and 17 instructional Note/MarkdownNote nodes**. Counts include the 21 root graphs and all embedded definitions. This audit prioritizes presentation patterns and artist-facing entry points rather than cataloging every processing node.

`archive/` is completely excluded from the audit, editing, and validation. `.index.json` is not edited. No workflow is renamed. The former Ref2V pilot was removed by the user; the replacement pilot is **`Minimax H3 i2v.json` only**. `Klein Dataset Maker.json` and all MiniMax Ref2V workflows remain unchanged and excluded from implementation.

The user approved the I2V pilot design and authorized rollout. All 21 active root workflows now use the approved presentation conventions. The remaining 20 workflows received display-only edits with their original geometry and instructional bodies preserved. The I2V layout and added Quick Start note remain the only explicitly authorized geometry/node-addition exceptions. No GUI interaction or workflow execution was performed by the agent; the user visually inspected and approved the pilot. See `WORKFLOW_ROLLOUT.md` and `WORKFLOW_VALIDATION.md` for current rollout results.

## Findings and Proposed Improvements

| Priority | Finding | Active Examples | Proposed Improvement |
| --- | --- | --- | --- |
| High | Colors do not consistently identify artist actions. | MiniMax I2V frame inputs are green; its preview text is uncolored; internal text conversions and chunk processing are purple. Klein Dataset Maker uses several unrelated palettes. | Blue input headers, yellow controls, violet previews, green save/export headers, all over a shared charcoal body. Replace misleading existing processing headers with slate; retain defaults on ordinary technical nodes. |
| High | Nearly every group has the same blue color regardless of purpose. | LTX, MiniMax, Qwen, Bernini, and Ideogram groups often use `#3f789e` for models, inputs, prompts, sampling, and results alike. | Color existing groups by purpose. Use gray for processing/mixed pipeline areas; never move nodes or change boundaries. |
| High | Type prefixes and abbreviations obscure artist-facing choices. | `Float (duration)`, `Turbo Boolean`, `PE Switch`, `Boolean (Enable LoRA?)`, `Text String (User Prompt)`, and `Int (Width)`. | Use labels such as `Duration (Seconds)`, `Use Turbo`, `Prompt Enhancement Switch`, and `Width (Pixels)` after verifying units. Retain technical names where they help identify processing operations. |
| High | Prompt preview, live preview configuration, metadata, and export have inconsistent names or no semantic cues. | MiniMax `Prompt Enhance Output` and `Video Info`; Qwen `Prompt Preview`; `SaveVideo` uses its default title. | Name readouts consistently and reserve green for the actual save node. A video assembly stage remains processing. |
| High | Some unusual names are literal model identifiers. | Active MiniMax R2V titles include `<Picture 1>` through `<Picture 3>`, `<Video 1>`, `<Video 2>`, `<Audio 1>`, and `<Audio 2>`. CharacterSheet instructions also use picture-reference syntax. | Preserve exact tags, numbering, prompts, and model-specific structured fields. Do not apply general capitalization rules inside syntax. R2V files remain outside the pilot. |
| Medium | Equivalent controls vary in case and units. | LTX `height`, `Frame Rate(int)`, `Frame Rate`, `Duration`; MiniMax `Float (duration)`; Song Gen `seed` and `TimeSig`. | Standardize confirmed units and terminology. Distinguish requested duration from calculated video duration and internal conversions. |
| Medium | Group titles range from vague to sentence-length instructions. | Krea2 `Group`/`Post`; Klein `Head_Swap`; LTX `FIrst Frame`; MiniMax `Decoding and create video`; Klein Dataset Maker's batch instruction in a group title. | Use concise stage names and preserve important instructions. Do not shorten names that extensions match without first confirming they are cosmetic. |
| Medium | Existing notes vary between long product introductions, detailed setup guides, short dependency reminders, and model-link lists. | Bernini has a task/reference guide; LTX has long descriptions plus model links; Krea2 has usage and model notes; Qwen has a settings table and a Node 2.0 requirement; SeedVR2 has parameter/long-video guidance. | Use concise, consistent headings where appropriate while retaining all links, defaults, conditions, limitations, and technical requirements. Keep substantive setup details even when lengthy. No note rewrites are needed in I2V because it has no Note nodes. |
| Review | Subgraph/interface labels may be technical or inconsistently capitalized but are protected by scope. | MiniMax I2V exposes `seconds`, `Prompt Enhance`, `Turbo`, `Preview In`, and `RTX`; one model interface says `Turbo_LoRa`. | Preserve interfaces, widget identifiers, and definition names. Improve only visible instance titles. Flag the remaining wording as an intentional scope exception. |
| Review | Group bypassers can make a group title functional. | Klein Face Maker and MiniMax CharacterSheet contain rgthree Fast Groups Bypasser nodes. | Review matching behavior before a future group rename. Preserve uncertain names; do not adjust bypasser settings during cosmetic cleanup. The I2V pilot contains no group bypasser. |

## Family-Level Observations

- **MiniMax H3:** Keep MiniMax capitalization, FL2VA/FL2V model identifiers, LoRA filenames, structured prompt fields, and reference tags intact. Make frame inputs and optional branches recognizable without altering their saved states. The pilot was limited to I2V; the approved rollout now includes the other MiniMax variants with reference syntax protected.
- **LTX:** Normalize visible duration/frame-rate labels and obvious capitalization errors after approval. Keep model/version naming and detailed requirements intact; long notes should retain their important setup and conditional instructions.
- **Klein / FLUX.2 and Ideogram:** Several workflows mix exposed technical pipelines and subgraphs. Highlight entry points and outputs without expanding, collapsing, or restructuring pipelines. Dataset Maker was excluded from the pilot; its approved presentation rollout preserves the exposed pipeline and layout.
- **Qwen:** Distinguish prompt input, prompt preview, turbo controls, and technical schedules. Preserve manual sigma values, system text, LoRA selections, and the camera-angle dependency reminder.
- **SeedVR2, Song Gen, and utility workflows:** Small graphs would benefit from selective input/output cues and consistent units. Keep SeedVR2's model requirements, Song Gen's musical values, and metadata formatter templates unchanged.
- **Bernini / SAM3:** Clarify visible reference/mask actions while retaining task codes, reference syntax, RGB cleanup behavior, and detailed usage constraints.

These observations propose presentation work only. Model/default discrepancies and execution behavior are not being corrected or runtime-certified by this audit.

## Implemented I2V Pilot

The original pilot had **72 nodes across six graphs** (one root and five definitions), ten existing groups, and no instructional notes. The user subsequently requested a Quick Start note; the current pilot has **73 nodes**, including one unconnected instructional MarkdownNote (ID 372). Its initial presentation pass changed **85 fields across 31 nodes and ten groups**. The requested layout revision adds **39 root geometry component changes**, for **124 presentation/layout changes relative to Git**. Palette revisions affect already-styled fields, so the presentation/layout total remains 124. The latest revision lightens the 21 styled node bodies to charcoal `#30343B` for greater separation from the canvas. Headers and all geometry remain unchanged. See `PILOT_VALIDATION.md` for every current original/modified value and its exact JSON Pointer; `PILOT_LAYOUT_REVIEW.md` records the earlier layout revision and `PILOT_COLOR_REVIEW.md` isolates the latest card-style revision.

| Area | Changes | Artist Benefit |
| --- | --- | --- |
| Input frames | Blue headers and charcoal bodies for `First Frame` and `Last Frame (Optional)`; blue `Input Frames` group. | Identifies where to supply images and makes the optional ending frame clear. The ending frame remains bypassed exactly as saved. |
| Creative controls | Yellow headers and charcoal bodies for `Seed`, `LoRA Settings`, and `Image to Video (MiniMax H3)`; light yellow `Creative Settings` group. | Shows the main generation settings and supporting creative controls together without changing their contents. |
| Previews and results | Violet preview headers and a green `Save Video` header, all over the same charcoal body. | Distinguishes feedback/readouts from the saved result without large tinted surfaces competing with the media. Existing output paths and codecs are unchanged. |
| Embedded controls | `Duration (Seconds)`, `Use Turbo`, `Prompt Enhancement Switch`, `Turbo Sampling Switch`, `Turbo Model Switch`, `Use Last Frame`, and `Use RTX Upscaling`. | Replaces implementation prefixes and unclear abbreviations while identifying each switch's role. |
| Embedded processing | Clearer resize, model-instance, and metadata titles. Existing colored text conversion and accelerator nodes use gray. | Removes preview/control cues from technical processing; most processing nodes retain default appearance. |
| Groups | Gray pipeline groups; clearer `Text, Video, and Audio Models`, `Video and Audio Assembly`, `Prompt Enhancement`, and `Base and Turbo Models`. | Makes stages easier to recognize within the existing graph and separates the two model areas. |

### Protected Exceptions and Unchanged Data

- All node IDs/types, array ordering, sockets, links, widget values, prompts, system instructions, template strings, file/model references, execution/bypass states, flags, subgraph interfaces, and workflow metadata remain identical. All embedded positions, sizes, and group boundaries remain identical. Root geometry changes are confined to the separately requested layout revision below.
- Subgraph definition names and interfaces remain unchanged, including `Image to Video (MiniMax H3) TURBO`, `Auto Prompt Writing`, and `Turbo_LoRa`. Visible instance titles provide the cleaner names without touching definitions.
- The exposed turbo model's 8-step LoRA selection and the internal 4-step LoRA selections remain exactly as saved. No sampling/default correction is part of this work.
- The requested-duration control, frame-count expression, and metadata duration calculation retain their original values and formulas. Naming them does not promise equal requested and actual durations.
- `Save Video` retains the saved `video/MiniMax_H3` prefix and all codec/format defaults. The last-frame input remains bypassed; optional branches and accelerators retain every saved state.
- The I2V workflow has no reference-tag node titles. No existing prompt or text widget was edited. The user explicitly requested the new Quick Start note after approving the visual treatment; it has no inputs, outputs, or connections.
- Root widget/socket wording such as `Prompt Enhance` and `RTX` is intentionally left unchanged because interfaces are protected. Long/technical definition names likewise remain exceptions.

## Validation and Approval Boundary

`validate_workflow_cosmetics.py` compares the pilot with the exact baseline commit. It recursively checks embedded definitions and permits only explicit cosmetic node/group fields by default. The separate tests exercise forbidden changes in root, embedded, and more deeply nested graphs, plus reference-token protection and optional note handling.

The saved pilot comparison passes with **126 allowed changes and zero unauthorized changes** (124 presentation/layout changes plus the authorized note addition and node-ID counter update) when the explicitly requested root layout allowance is enabled. Default cosmetic-only mode continues to reject geometry edits. All twelve validator tests pass, including rejection of embedded geometry and functional changes under the root layout allowance. The workflow remains a single-line JSON file; edits replaced individual value tokens or inserted allowed display fields without reserializing unrelated data.

The comparison proves preservation of saved data outside the cosmetic and explicitly authorized root layout fields; it does not prove successful generation or visual quality. The user should inspect the main canvas for spacing, title fit, settings color/readability, preview sizing, and dimmed bypass presentation. No agent GUI or runtime checks are claimed.

## Revision After Visual Feedback

- Give all 21 explicitly styled nodes the same charcoal body `#30343B`. Use yellow settings headers `#715B2D` and light yellow group color `#D2B16F`; retain blue, violet, green, and slate headers for the other categories. Apply the same card treatment to root nodes and existing styled embedded nodes. Leave ordinary unstyled processing nodes at their defaults.
- Use 20 px side/bottom group padding, an 80 px top-to-node-body inset accounting for both title bars, 40 px horizontal card gaps, 30 px visible vertical card gaps, and 60 px between adjacent groups.
- Match both frame cards at 480 × 360 px. Use 480 px widths for primary generation/preview/output cards and 320 px for the two compact settings cards. Use role-appropriate, grid-aligned heights.
- Fit the settings group to its two controls rather than leaving a large unused lower area. Align the main generation, live preview, and save cards along the top row. Place video details below its save card, and keep the enhanced-prompt preview aligned below generation, outside its original group.
- Preserve node membership in all three root groups, every embedded layout, and all functional data. These layout conventions were approved with the pilot; existing geometry in the other workflows remains unchanged in the display-only rollout.

The geometry check confirms unchanged membership in all three root groups, no overlapping root node rectangles including 30 px title bars, at least 20 px side/bottom group clearance, and root node positions/dimensions on the 20 px grid. At the pilot stage, all 20 other active workflow files were byte-identical to the Git baseline; their subsequent presentation edits are recorded in the rollout report. These geometric checks do not replace the user's visual review of the revised canvas.

The user subsequently approved the design. The presentation rollout, authoritative guide, repository `AGENTS.md`, and short README maintenance link are now complete; review the rollout report for preserved exceptions.

## Requested Quick Start Note

Added one unconnected MarkdownNote to the left of the workflow, explaining image-to-video generation, input/prompt/settings usage, the optional ending-frame steps, Ollama prompt enhancement, and the saved-video location. Only the new node and `last_node_id` update differ from the prior visual pilot. Existing geometry, groups, prompts, widget defaults, links, interfaces, and execution states remain unchanged. The validator requires explicit `--allow-root-note 372` for this addition; default cosmetic-only mode rejects it. The full current report is `PILOT_VALIDATION.md`; `PILOT_NOTE_REVIEW.md` isolates the addition.

## Quick Start Notes

All 21 active workflows now have a novice-facing Quick Start with **What It Does** and **How to Use**. Nine workflows reused existing guides and twelve received a new unconnected note. Existing model links and reference syntax were checked against their pre-edit values. See `WORKFLOW_ROLLOUT.md` for the per-workflow notes and validation results.
