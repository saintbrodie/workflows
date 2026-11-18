# Approved Workflow Presentation Rollout

Applied the user-approved visual standard to all 21 active root workflows on `codex/workflow-design-pilot`. The I2V pilot was visually inspected and approved by the user. Other workflows have not been executed or visually inspected by the agent.

## Validation

All 21 workflows passed. The notes pass was also compared against the previously styled files, with edits limited to instructional nodes and the node-ID counter for new notes. The [full comparison](WORKFLOW_VALIDATION.md) includes the visual rollout and the Quick Start notes.

| Workflow | Quick Start | Note ID | Note Pass Fields | Total Fields |
| --- | --- | --- | --- | --- |
| Background Removal (SAM3).json | Added | 323 | 2 | 25 |
| Bernini Video Editing.json | Revised | 392 | 8 | 89 |
| Ideogram4 Playground.json | Added | 210 | 2 | 60 |
| Klein Dataset Maker.json | Added | 381 | 2 | 49 |
| Klein Edit.json | Revised | 732 | 2 | 61 |
| Klein Face Maker.json | Added | 365 | 2 | 106 |
| Klein Headswap.json | Added | 146 | 2 | 47 |
| Krea2 Turbo.json | Revised | 50 | 4 | 42 |
| LTX Video 2.5 FLF2V.json | Revised | 254 | 3 | 53 |
| LTX Video 2.5 I2V.json | Revised | 399 | 3 | 60 |
| LTX Video 2.5 T2V.json | Revised | 407 | 6 | 57 |
| Minimax H3 CharacterSheet 6p.json | Revised | 142 | 4 | 63 |
| Minimax H3 i2v.json | Revised | 372 | 1 | 126 |
| Minimax H3 r2v.json | Added | 407 | 2 | 85 |
| Minimax H3 t2v.json | Added | 375 | 2 | 67 |
| Qwen Image 2.1 Edit.json | Added | 943 | 2 | 31 |
| Qwen Image 2.1 Multi Angle.json | Added | 950 | 7 | 44 |
| SeedVR2 Image Upscale.json | Added | 77 | 2 | 15 |
| SeedVR2 Video Upscale.json | Revised | 82 | 3 | 18 |
| Song Gen v1.json | Added | 151 | 2 | 35 |
| Video Metadata.json | Added | 8 | 2 | 11 |

63 note-pass fields and 1144 cumulative fields across 21 workflows.

The validator suite passes all 13 tests.

## Preserved Exceptions

- MiniMax numbered picture/video/audio reference tags remain exact. All prompts, model selections, trigger words, parser templates, and subgraph names/interfaces are untouched.
- CharacterSheet accelerator groups retain their exact cyan `#8AA` colors because its bypasser filters by `cyan`. Its group titles and Klein Face Maker group titles remain exact.
- Krea2 `Text String (User Prompt)`, CharacterSheet `Input Text (Prompt)`, LTX documented `Load First Frame` / `Load Last Frame`, and Bernini's referenced note title remain unchanged to keep existing instructions accurate.
- Every active workflow now has a Quick Start note. New notes sit to the left of the graph. Existing overview notes were reused where practical, with downloads and advanced reference details retained.
- Remaining workflow layouts are preserved. The approved spacing rules apply to new or separately authorized layout work.
- Bypassed nodes retain ComfyUI's bypass tint and their original states. Ordinary technical nodes generally retain default appearance; existing custom technical colors were standardized.
- `archive/` was not read, edited, or validated. `.index.json` and workflow filenames are untouched.

## Maintenance References

[WORKFLOW_STYLE_GUIDE.md](WORKFLOW_STYLE_GUIDE.md) is authoritative. [AGENTS.md](../AGENTS.md) provides concise maintenance rules; [the GitHub README](../.github/README.md) links to both without changing its dependency documentation. The historical pilot reports remain available, while WORKFLOW_VALIDATION.md is the current complete result.
