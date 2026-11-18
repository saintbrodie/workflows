# Pilot Cosmetic Validation

This comparison checks JSON structure and unchanged saved data. It does not prove runtime functionality or visual quality.

Visual inspection in ComfyUI: pending user review. No workflow execution was performed.

## Minimax H3 i2v.json

Result: **PASS** — 2 changed fields; 0 unauthorized changes.

Original: `Approved visual pilot before requested Quick Start note`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note addition allowance: 372.

Original SHA-256: `59017ff3915a34460bf5a34ef8cf684725f5f00a879a2742f4770a5ab3d3f424`

Modified SHA-256: `ff5a6505ba80f6cbb0c1d1c8a88126b5517b6a08a3331f09fd16ccbe060aa205`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /nodes/9 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 372, "type": "MarkdownNote", "pos": [-1780, 4560], "size": [480, 360], "flags": {}, "order": 9, "mode": 0, "inputs": [], "outputs": [], "title": "MiniMax H3 Quick Start", "properties": {}, "widgets_values": ["Animate a starting image into a video with MiniMax H3.\n\n1. Load your image in First Frame.\n2. Describe the motion and scene in the generation card. Set seconds and megapixels; adjust Seed or LoRA Settings if needed.\n3. Optional ending image: enable the Last Frame (Optional) image node and turn on Last Frame in the generation card.\n4. Run the workflow. Watch Generation Preview and find the saved video in ComfyUI/output/video/ (MiniMax_H3 prefix).\n\nPrompt Enhance rewrites your prompt through Ollama. Turn it off to use your own wording; Turbo and RTX Upscale 2x are optional choices."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 371 | 372 | Allowed |
