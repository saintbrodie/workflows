# Pilot Cosmetic Validation

This comparison checks JSON structure and unchanged saved data. It does not prove runtime functionality or visual quality.

Visual inspection in ComfyUI: pending user review. No workflow execution was performed.

## Minimax H3 i2v.json

Result: **PASS** — 21 changed fields; 0 unauthorized changes.

Original: `Yellow-header pilot before requested charcoal lightening`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Original SHA-256: `cf35c83a9bf66b202f672ec123f01a940f9cf6b792da7d91728dc5baca0f1199`

Modified SHA-256: `59017ff3915a34460bf5a34ef8cf684725f5f00a879a2742f4770a5ab3d3f424`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/nodes/14/bgcolor | Node 277 (PrimitiveFloat) | "#24262B" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/18/bgcolor | Node 325 (a5572c1f-da0d-4fd8-a7c6-7f6cab508de5) | "#24262B" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/27/bgcolor | Node 358 (PrimitiveBoolean) | "#24262B" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/31/bgcolor | Node 364 (ImageScaleToTotalPixels) | "#24262B" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/32/bgcolor | Node 365 (ImageScaleToTotalPixels) | "#24262B" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/0/bgcolor | Node 317 (SomethingToString) | "#24262B" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/1/bgcolor | Node 318 (SomethingToString) | "#24262B" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/5/bgcolor | Node 322 (SomethingToString) | "#24262B" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/1/bgcolor | Node 342 (MiniMaxChunkFeedForward) | "#24262B" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/3/bgcolor | Node 344 (MiniMaxH3SigmaShift) | "#24262B" | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/1/bgcolor | Node 350 (MiniMaxChunkFeedForward) | "#24262B" | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/3/bgcolor | Node 352 (MiniMaxH3SigmaShift) | "#24262B" | "#30343B" | Allowed |
| /nodes/0/bgcolor | Node 300 (Power Lora Loader (rgthree)) | "#24262B" | "#30343B" | Allowed |
| /nodes/1/bgcolor | Node 293 (SeedNode) | "#24262B" | "#30343B" | Allowed |
| /nodes/2/bgcolor | Node 290 (SaveVideo) | "#24262B" | "#30343B" | Allowed |
| /nodes/3/bgcolor | Node 289 (e5f30591-fb92-4c19-ba9b-d9687794a624) | "#24262B" | "#30343B" | Allowed |
| /nodes/4/bgcolor | Node 315 (LoadImage) | "#24262B" | "#30343B" | Allowed |
| /nodes/5/bgcolor | Node 312 (LoadImage) | "#24262B" | "#30343B" | Allowed |
| /nodes/6/bgcolor | Node 295 (ModelPreviewOverrideKJ) | "#24262B" | "#30343B" | Allowed |
| /nodes/7/bgcolor | Node 363 (PreviewAny) | "#24262B" | "#30343B" | Allowed |
| /nodes/8/bgcolor | Node 371 (PreviewAny) | "#24262B" | "#30343B" | Allowed |
