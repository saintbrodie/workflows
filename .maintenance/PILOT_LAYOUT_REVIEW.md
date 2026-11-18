# Pilot Cosmetic Validation

Historical layout-revision snapshot. Its settings colors have since been replaced; see `PILOT_COLOR_REVIEW.md` for that revision and `PILOT_VALIDATION.md` for the current full comparison.

This comparison checks JSON structure and unchanged saved data. It does not prove runtime functionality or visual quality.

Visual inspection in ComfyUI: pending user review. No workflow execution was performed.

## Minimax H3 i2v.json

Result: **PASS** — 40 changed fields; 0 unauthorized changes.

Original: `Presentation-only pilot v1, before group contrast and root layout revision`

Layout allowance: explicit root-only positions, sizes, and group bounds; embedded layouts remain protected.

Original SHA-256: `11b415afa7cd33fda59d0737ddd300b0b4de9431475b485934a3d43adb2bb5b5`

Modified SHA-256: `38c9e34eb650a8dd22243cee5eab9518c4d50bf01d40af00a889c58902a5ca32`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /groups/0/bounding/0 | Group 15 | -860 | -800 | Allowed (Layout) |
| /groups/0/bounding/2 | Group 15 | 1760 | 1560 | Allowed (Layout) |
| /groups/0/bounding/3 | Group 15 | 690 | 900 | Allowed (Layout) |
| /groups/1/bounding/0 | Group 17 | -1280 | -1220 | Allowed (Layout) |
| /groups/1/bounding/2 | Group 17 | 380 | 360 | Allowed (Layout) |
| /groups/1/bounding/3 | Group 17 | 680 | 420 | Allowed (Layout) |
| /groups/1/color | Group 17 | "#715B2D" | "#D2B16F" | Allowed |
| /groups/2/bounding/2 | Group 25 | 473.0776660160866 | 520 | Allowed (Layout) |
| /groups/2/bounding/3 | Group 25 | 851.3603087312758 | 880 | Allowed (Layout) |
| /nodes/0/pos/0 | Node 300 (Power Lora Loader (rgthree)) | -1260 | -1200 | Allowed (Layout) |
| /nodes/0/pos/1 | Node 300 (Power Lora Loader (rgthree)) | 5220 | 5240 | Allowed (Layout) |
| /nodes/0/size/0 | Node 300 (Power Lora Loader (rgthree)) | 340 | 320 | Allowed (Layout) |
| /nodes/0/size/1 | Node 300 (Power Lora Loader (rgthree)) | 150 | 160 | Allowed (Layout) |
| /nodes/1/pos/0 | Node 293 (SeedNode) | -1260 | -1200 | Allowed (Layout) |
| /nodes/1/size/0 | Node 293 (SeedNode) | 340 | 320 | Allowed (Layout) |
| /nodes/1/size/1 | Node 293 (SeedNode) | 90 | 100 | Allowed (Layout) |
| /nodes/2/pos/0 | Node 290 (SaveVideo) | 160 | 260 | Allowed (Layout) |
| /nodes/2/size/0 | Node 290 (SaveVideo) | 440 | 480 | Allowed (Layout) |
| /nodes/2/size/1 | Node 290 (SaveVideo) | 538 | 600 | Allowed (Layout) |
| /nodes/3/pos/0 | Node 289 (e5f30591-fb92-4c19-ba9b-d9687794a624) | -840 | -780 | Allowed (Layout) |
| /nodes/3/size/0 | Node 289 (e5f30591-fb92-4c19-ba9b-d9687794a624) | 440 | 480 | Allowed (Layout) |
| /nodes/3/size/1 | Node 289 (e5f30591-fb92-4c19-ba9b-d9687794a624) | 580 | 600 | Allowed (Layout) |
| /nodes/4/pos/0 | Node 315 (LoadImage) | -1790 | -1780 | Allowed (Layout) |
| /nodes/4/pos/1 | Node 315 (LoadImage) | 5480 | 5500 | Allowed (Layout) |
| /nodes/4/size/0 | Node 315 (LoadImage) | 453.0776660160866 | 480 | Allowed (Layout) |
| /nodes/4/size/1 | Node 315 (LoadImage) | 361.36030873127584 | 360 | Allowed (Layout) |
| /nodes/5/pos/0 | Node 312 (LoadImage) | -1790 | -1780 | Allowed (Layout) |
| /nodes/5/pos/1 | Node 312 (LoadImage) | 5070 | 5080 | Allowed (Layout) |
| /nodes/5/size/0 | Node 312 (LoadImage) | 453.0776660160866 | 480 | Allowed (Layout) |
| /nodes/5/size/1 | Node 312 (LoadImage) | 361.36030873127584 | 360 | Allowed (Layout) |
| /nodes/6/pos/0 | Node 295 (ModelPreviewOverrideKJ) | -360 | -260 | Allowed (Layout) |
| /nodes/6/size/0 | Node 295 (ModelPreviewOverrideKJ) | 490 | 480 | Allowed (Layout) |
| /nodes/6/size/1 | Node 295 (ModelPreviewOverrideKJ) | 580 | 600 | Allowed (Layout) |
| /nodes/7/pos/0 | Node 363 (PreviewAny) | -840 | -780 | Allowed (Layout) |
| /nodes/7/pos/1 | Node 363 (PreviewAny) | 5730 | 5960 | Allowed (Layout) |
| /nodes/7/size/0 | Node 363 (PreviewAny) | 440 | 480 | Allowed (Layout) |
| /nodes/8/pos/0 | Node 371 (PreviewAny) | 628.5196922557193 | 260 | Allowed (Layout) |
| /nodes/8/pos/1 | Node 371 (PreviewAny) | 5124.3064405275845 | 5740 | Allowed (Layout) |
| /nodes/8/size/0 | Node 371 (PreviewAny) | 210 | 480 | Allowed (Layout) |
| /nodes/8/size/1 | Node 371 (PreviewAny) | 122 | 140 | Allowed (Layout) |
