# Pilot Cosmetic Validation

This comparison checks JSON structure and unchanged saved data. It does not prove runtime functionality or visual quality.

Visual inspection in ComfyUI: pending user review. No workflow execution was performed.

## Minimax H3 i2v.json

Result: **PASS** — 126 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Minimax H3 i2v.json`

Layout allowance: explicit root-only positions, sizes, and group bounds; embedded layouts remain protected.

Instructional note addition allowance: 372.

Original SHA-256: `65f61cbe68a20f340c21a6f49e76bccab874be6664d9ae4da0c77f982768df99`

Modified SHA-256: `0a75558b05fd8d475a2d07937186e8378a5b549611b871a0c967aeadaa219091`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/0/title | Group 1 | "Models" | "Text, Video, and Audio Models" | Allowed |
| /definitions/subgraphs/0/groups/1/color | Group 2 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/2/color | Group 3 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/3/color | Group 4 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/3/title | Group 4 | "Decoding and create video" | "Video and Audio Assembly" | Allowed |
| /definitions/subgraphs/0/groups/4/color | Group 18 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/4/title | Group 18 | "Prompt Enhance" | "Prompt Enhancement" | Allowed |
| /definitions/subgraphs/0/groups/5/color | Group 20 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/6/color | Group 24 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/6/title | Group 24 | "Models" | "Base and Turbo Models" | Allowed |
| /definitions/subgraphs/0/nodes/14/bgcolor | Node 277 (PrimitiveFloat) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/14/color | Node 277 (PrimitiveFloat) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/14/title | Node 277 (PrimitiveFloat) | "Float (duration)" | "Duration (Seconds)" | Allowed |
| /definitions/subgraphs/0/nodes/18/bgcolor | Node 325 (a5572c1f-da0d-4fd8-a7c6-7f6cab508de5) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/18/color | Node 325 (a5572c1f-da0d-4fd8-a7c6-7f6cab508de5) | "#432" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/18/title | Node 325 (a5572c1f-da0d-4fd8-a7c6-7f6cab508de5) | (absent; ComfyUI default) | "Enhance Prompt (Ollama)" | Allowed |
| /definitions/subgraphs/0/nodes/20/title | Node 328 (ComfySwitchNode) | "PE Switch" | "Prompt Enhancement Switch" | Allowed |
| /definitions/subgraphs/0/nodes/26/title | Node 340 (ComfySwitchNode) | "Turbo Switch" | "Turbo Sampling Switch" | Allowed |
| /definitions/subgraphs/0/nodes/27/bgcolor | Node 358 (PrimitiveBoolean) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/27/color | Node 358 (PrimitiveBoolean) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/27/title | Node 358 (PrimitiveBoolean) | "Turbo Boolean" | "Use Turbo" | Allowed |
| /definitions/subgraphs/0/nodes/28/title | Node 359 (ComfySwitchNode) | "Turbo Switch" | "Turbo Model Switch" | Allowed |
| /definitions/subgraphs/0/nodes/29/title | Node 361 (f71e86b4-e2a3-465b-8b33-7059d1ab844a) | (absent; ComfyUI default) | "Turbo Model and LoRA" | Allowed |
| /definitions/subgraphs/0/nodes/30/title | Node 362 (1be35f87-762a-4947-8cec-df05670df1a9) | (absent; ComfyUI default) | "Base Model" | Allowed |
| /definitions/subgraphs/0/nodes/31/bgcolor | Node 364 (ImageScaleToTotalPixels) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/31/color | Node 364 (ImageScaleToTotalPixels) | "#432" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/31/title | Node 364 (ImageScaleToTotalPixels) | (absent; ComfyUI default) | "Resize First Frame" | Allowed |
| /definitions/subgraphs/0/nodes/32/bgcolor | Node 365 (ImageScaleToTotalPixels) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/32/color | Node 365 (ImageScaleToTotalPixels) | "#432" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/32/title | Node 365 (ImageScaleToTotalPixels) | (absent; ComfyUI default) | "Resize Last Frame" | Allowed |
| /definitions/subgraphs/0/nodes/34/title | Node 367 (ComfySwitchNode) | "Last Frame Switch" | "Use Last Frame" | Allowed |
| /definitions/subgraphs/0/nodes/35/title | Node 368 (ComfySwitchNode) | "RTX Switch" | "Use RTX Upscaling" | Allowed |
| /definitions/subgraphs/0/nodes/36/title | Node 370 (1d9afd10-f22f-4b34-950c-a643e4748dd2) | (absent; ComfyUI default) | "Video Details" | Allowed |
| /definitions/subgraphs/1/nodes/0/bgcolor | Node 317 (SomethingToString) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/0/color | Node 317 (SomethingToString) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/1/nodes/0/title | Node 317 (SomethingToString) | "Duration" | "Duration to Text" | Allowed |
| /definitions/subgraphs/1/nodes/1/bgcolor | Node 318 (SomethingToString) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/1/color | Node 318 (SomethingToString) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/1/nodes/1/title | Node 318 (SomethingToString) | "Height" | "Height to Text" | Allowed |
| /definitions/subgraphs/1/nodes/5/bgcolor | Node 322 (SomethingToString) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/5/color | Node 322 (SomethingToString) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/1/nodes/5/title | Node 322 (SomethingToString) | "Width" | "Width to Text" | Allowed |
| /definitions/subgraphs/2/nodes/1/bgcolor | Node 342 (MiniMaxChunkFeedForward) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/1/color | Node 342 (MiniMaxChunkFeedForward) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/3/bgcolor | Node 344 (MiniMaxH3SigmaShift) | "#3f5159" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/3/color | Node 344 (MiniMaxH3SigmaShift) | "#2a363b" | "#35414A" | Allowed |
| /definitions/subgraphs/3/nodes/1/bgcolor | Node 350 (MiniMaxChunkFeedForward) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/1/color | Node 350 (MiniMaxChunkFeedForward) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/3/nodes/3/bgcolor | Node 352 (MiniMaxH3SigmaShift) | "#3f5159" | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/3/color | Node 352 (MiniMaxH3SigmaShift) | "#2a363b" | "#35414A" | Allowed |
| /definitions/subgraphs/4/nodes/2/title | Node 4 (ComfyMathExpression) | "Duration (frames / fps)" | "Video Duration (Seconds)" | Allowed |
| /definitions/subgraphs/4/nodes/3/title | Node 5 (StringFormat) | "Video metadata summary" | "Video Details Summary" | Allowed |
| /groups/0/bounding/0 | Group 15 | -860 | -800 | Allowed (Layout) |
| /groups/0/bounding/2 | Group 15 | 1760 | 1560 | Allowed (Layout) |
| /groups/0/bounding/3 | Group 15 | 690 | 900 | Allowed (Layout) |
| /groups/0/color | Group 15 | "#3f789e" | "#35414A" | Allowed |
| /groups/0/title | Group 15 | "Image to Video" | "Video Generation" | Allowed |
| /groups/1/bounding/0 | Group 17 | -1280 | -1220 | Allowed (Layout) |
| /groups/1/bounding/2 | Group 17 | 380 | 360 | Allowed (Layout) |
| /groups/1/bounding/3 | Group 17 | 680 | 420 | Allowed (Layout) |
| /groups/1/color | Group 17 | "#3f789e" | "#D2B16F" | Allowed |
| /groups/1/title | Group 17 | "Extra Settings" | "Creative Settings" | Allowed |
| /groups/2/bounding/2 | Group 25 | 473.0776660160866 | 520 | Allowed (Layout) |
| /groups/2/bounding/3 | Group 25 | 851.3603087312758 | 880 | Allowed (Layout) |
| /groups/2/color | Group 25 | "#3f789e" | "#235B74" | Allowed |
| /groups/2/title | Group 25 | "Image Inputs" | "Input Frames" | Allowed |
| /nodes/0/bgcolor | Node 300 (Power Lora Loader (rgthree)) | "#653" | "#30343B" | Allowed |
| /nodes/0/color | Node 300 (Power Lora Loader (rgthree)) | "#432" | "#715B2D" | Allowed |
| /nodes/0/pos/0 | Node 300 (Power Lora Loader (rgthree)) | -1260 | -1200 | Allowed (Layout) |
| /nodes/0/pos/1 | Node 300 (Power Lora Loader (rgthree)) | 5220 | 5240 | Allowed (Layout) |
| /nodes/0/size/0 | Node 300 (Power Lora Loader (rgthree)) | 340 | 320 | Allowed (Layout) |
| /nodes/0/size/1 | Node 300 (Power Lora Loader (rgthree)) | 150 | 160 | Allowed (Layout) |
| /nodes/0/title | Node 300 (Power Lora Loader (rgthree)) | (absent; ComfyUI default) | "LoRA Settings" | Allowed |
| /nodes/1/bgcolor | Node 293 (SeedNode) | "#653" | "#30343B" | Allowed |
| /nodes/1/color | Node 293 (SeedNode) | "#432" | "#715B2D" | Allowed |
| /nodes/1/pos/0 | Node 293 (SeedNode) | -1260 | -1200 | Allowed (Layout) |
| /nodes/1/size/0 | Node 293 (SeedNode) | 340 | 320 | Allowed (Layout) |
| /nodes/1/size/1 | Node 293 (SeedNode) | 90 | 100 | Allowed (Layout) |
| /nodes/1/title | Node 293 (SeedNode) | (absent; ComfyUI default) | "Seed" | Allowed |
| /nodes/2/bgcolor | Node 290 (SaveVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 290 (SaveVideo) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/2/pos/0 | Node 290 (SaveVideo) | 160 | 260 | Allowed (Layout) |
| /nodes/2/size/0 | Node 290 (SaveVideo) | 440 | 480 | Allowed (Layout) |
| /nodes/2/size/1 | Node 290 (SaveVideo) | 538 | 600 | Allowed (Layout) |
| /nodes/2/title | Node 290 (SaveVideo) | (absent; ComfyUI default) | "Save Video" | Allowed |
| /nodes/3/bgcolor | Node 289 (e5f30591-fb92-4c19-ba9b-d9687794a624) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/3/color | Node 289 (e5f30591-fb92-4c19-ba9b-d9687794a624) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/3/pos/0 | Node 289 (e5f30591-fb92-4c19-ba9b-d9687794a624) | -840 | -780 | Allowed (Layout) |
| /nodes/3/size/0 | Node 289 (e5f30591-fb92-4c19-ba9b-d9687794a624) | 440 | 480 | Allowed (Layout) |
| /nodes/3/size/1 | Node 289 (e5f30591-fb92-4c19-ba9b-d9687794a624) | 580 | 600 | Allowed (Layout) |
| /nodes/3/title | Node 289 (e5f30591-fb92-4c19-ba9b-d9687794a624) | (absent; ComfyUI default) | "Image to Video (MiniMax H3)" | Allowed |
| /nodes/4/bgcolor | Node 315 (LoadImage) | "#353" | "#30343B" | Allowed |
| /nodes/4/color | Node 315 (LoadImage) | "#232" | "#235B74" | Allowed |
| /nodes/4/pos/0 | Node 315 (LoadImage) | -1790 | -1780 | Allowed (Layout) |
| /nodes/4/pos/1 | Node 315 (LoadImage) | 5480 | 5500 | Allowed (Layout) |
| /nodes/4/size/0 | Node 315 (LoadImage) | 453.0776660160866 | 480 | Allowed (Layout) |
| /nodes/4/size/1 | Node 315 (LoadImage) | 361.36030873127584 | 360 | Allowed (Layout) |
| /nodes/4/title | Node 315 (LoadImage) | "Last Frame" | "Last Frame (Optional)" | Allowed |
| /nodes/5/bgcolor | Node 312 (LoadImage) | "#353" | "#30343B" | Allowed |
| /nodes/5/color | Node 312 (LoadImage) | "#232" | "#235B74" | Allowed |
| /nodes/5/pos/0 | Node 312 (LoadImage) | -1790 | -1780 | Allowed (Layout) |
| /nodes/5/pos/1 | Node 312 (LoadImage) | 5070 | 5080 | Allowed (Layout) |
| /nodes/5/size/0 | Node 312 (LoadImage) | 453.0776660160866 | 480 | Allowed (Layout) |
| /nodes/5/size/1 | Node 312 (LoadImage) | 361.36030873127584 | 360 | Allowed (Layout) |
| /nodes/6/bgcolor | Node 295 (ModelPreviewOverrideKJ) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/6/color | Node 295 (ModelPreviewOverrideKJ) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/6/pos/0 | Node 295 (ModelPreviewOverrideKJ) | -360 | -260 | Allowed (Layout) |
| /nodes/6/size/0 | Node 295 (ModelPreviewOverrideKJ) | 490 | 480 | Allowed (Layout) |
| /nodes/6/size/1 | Node 295 (ModelPreviewOverrideKJ) | 580 | 600 | Allowed (Layout) |
| /nodes/6/title | Node 295 (ModelPreviewOverrideKJ) | (absent; ComfyUI default) | "Generation Preview" | Allowed |
| /nodes/7/bgcolor | Node 363 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/7/color | Node 363 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/7/pos/0 | Node 363 (PreviewAny) | -840 | -780 | Allowed (Layout) |
| /nodes/7/pos/1 | Node 363 (PreviewAny) | 5730 | 5960 | Allowed (Layout) |
| /nodes/7/size/0 | Node 363 (PreviewAny) | 440 | 480 | Allowed (Layout) |
| /nodes/7/title | Node 363 (PreviewAny) | "Prompt Enhance Output" | "Enhanced Prompt Preview" | Allowed |
| /nodes/8/bgcolor | Node 371 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/8/color | Node 371 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/8/pos/0 | Node 371 (PreviewAny) | 628.5196922557193 | 260 | Allowed (Layout) |
| /nodes/8/pos/1 | Node 371 (PreviewAny) | 5124.3064405275845 | 5740 | Allowed (Layout) |
| /nodes/8/size/0 | Node 371 (PreviewAny) | 210 | 480 | Allowed (Layout) |
| /nodes/8/size/1 | Node 371 (PreviewAny) | 122 | 140 | Allowed (Layout) |
| /nodes/8/title | Node 371 (PreviewAny) | "Video Info" | "Video Details" | Allowed |
| /nodes/9 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 372, "type": "MarkdownNote", "pos": [-2340, 5080], "size": [480, 360], "flags": {}, "order": 9, "mode": 0, "inputs": [], "outputs": [], "title": "MiniMax H3 Quick Start", "properties": {}, "widgets_values": ["Animate a starting image into a video with MiniMax H3.\n\n1. Load your image in First Frame.\n2. Describe the motion and scene in the generation card. Set seconds and megapixels; adjust Seed or LoRA Settings if needed.\n3. Optional ending image: enable the Last Frame (Optional) image node and turn on Last Frame in the generation card.\n4. Run the workflow. Watch Generation Preview and find the saved video in ComfyUI/output/video/ (MiniMax_H3 prefix).\n\nPrompt Enhance rewrites your prompt through Ollama. Turn it off to use your own wording; Turbo and RTX Upscale 2x are optional choices."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 371 | 372 | Allowed |
