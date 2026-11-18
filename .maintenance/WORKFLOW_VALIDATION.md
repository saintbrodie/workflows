# Workflow Presentation Validation

This comparison checks JSON structure and unchanged saved data. It does not prove runtime functionality or visual quality.

Visual inspection is a separate user review. No workflow execution was performed by this validator.

## Background Removal (SAM3).json

Result: **PASS** — 25 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Background Removal (SAM3).json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: 323.

Original SHA-256: `a67de8b128d0b68974e18e9c0abe31a3b7ba75d185d059dee43f91d901e67cb7`

Modified SHA-256: `385014f3fa64ecd717060cecfebe6937ffa43ef0044e51dcc06ab6694d3ab5d6`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/nodes/3/bgcolor | Node 312 (PreviewImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/3/color | Node 312 (PreviewImage) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/0/nodes/3/title | Node 312 (PreviewImage) | (absent; ComfyUI default) | "Image Preview" | Allowed |
| /definitions/subgraphs/0/nodes/5/bgcolor | Node 314 (MaskPreview) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/5/color | Node 314 (MaskPreview) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/0/nodes/5/title | Node 314 (MaskPreview) | (absent; ComfyUI default) | "Mask Preview" | Allowed |
| /definitions/subgraphs/0/nodes/8/bgcolor | Node 317 (PreviewImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/8/color | Node 317 (PreviewImage) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/0/nodes/8/title | Node 317 (PreviewImage) | (absent; ComfyUI default) | "Image Preview" | Allowed |
| /definitions/subgraphs/0/nodes/9/title | Node 318 (EmptyImage) | "White RGB background (change color here)" | "RGB Background Color" | Allowed |
| /definitions/subgraphs/0/nodes/11/title | Node 320 (ImageCompositeMasked) | "Clean RGB: replace ALL hidden background pixels" | "Clean All Hidden Background Pixels" | Allowed |
| /definitions/subgraphs/0/nodes/12/bgcolor | Node 321 (PreviewImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/12/color | Node 321 (PreviewImage) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/0/nodes/12/title | Node 321 (PreviewImage) | (absent; ComfyUI default) | "Image Preview" | Allowed |
| /nodes/0/bgcolor | Node 307 (PreviewImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/0/color | Node 307 (PreviewImage) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/0/title | Node 307 (PreviewImage) | (absent; ComfyUI default) | "Image Preview" | Allowed |
| /nodes/1/bgcolor | Node 308 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/1/color | Node 308 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/1/title | Node 308 (LoadImage) | (absent; ComfyUI default) | "Reference Image" | Allowed |
| /nodes/2/bgcolor | Node 322 (05456c0c-65e7-4f52-b12f-5175972df56a) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 322 (05456c0c-65e7-4f52-b12f-5175972df56a) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/2/title | Node 322 (05456c0c-65e7-4f52-b12f-5175972df56a) | (absent; ComfyUI default) | "Background Removal (SAM3)" | Allowed |
| /nodes/3 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 323, "type": "MarkdownNote", "pos": [-660, 5820], "size": [480, 360], "flags": {}, "order": 3, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nSeparate an object from its background and preview the cutout.\n\n### How to Use\n\n1. Load a picture in **Reference Image**.\n2. In **Background Removal (SAM3)**, set **object** to a short description such as “cat head.” If the wrong area is selected, try a more specific description.\n3. Click **Run** and inspect **Image Preview**. The result appears on the canvas."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 322 | 323 | Allowed |

## Bernini Video Editing.json

Result: **PASS** — 89 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Bernini Video Editing.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: none.

Original SHA-256: `25256595a39b3251ebe55b64a8b210f2a8bc423254af599e261ae40b96d3ba95`

Modified SHA-256: `87c6d02b569c24e039429ff4410691d7abdfdab78e458b5f41a1eb265c0477dd`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/color | Group 2 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/2/color | Group 3 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/3/color | Group 8 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/4/color | Group 4 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/4/title | Group 4 | "System Prompt (Based on task type)" | "System Prompt (Based on Task Type)" | Allowed |
| /definitions/subgraphs/0/groups/5/color | Group 7 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/0/groups/6/color | Group 5 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/0/groups/6/title | Group 5 | "Distill LoRA settings" | "Distill LoRA Settings" | Allowed |
| /definitions/subgraphs/0/groups/7/color | Group 6 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/0/nodes/2/bgcolor | Node 267 (CLIPTextEncode) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/2/color | Node 267 (CLIPTextEncode) | "#223" | "#235B74" | Allowed |
| /definitions/subgraphs/0/nodes/10/bgcolor | Node 280 (CLIPTextEncode) | "#353" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/10/color | Node 280 (CLIPTextEncode) | "#232" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/15/bgcolor | Node 285 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/15/color | Node 285 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/15/title | Node 285 (PrimitiveInt) | "Int (Steps)" | "Steps" | Allowed |
| /definitions/subgraphs/0/nodes/16/bgcolor | Node 286 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/16/color | Node 286 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/16/title | Node 286 (PrimitiveInt) | "Int (Steps)" | "Steps" | Allowed |
| /definitions/subgraphs/0/nodes/18/bgcolor | Node 288 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/18/color | Node 288 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/18/title | Node 288 (PrimitiveInt) | "Int (Split Steps)" | "Split Steps" | Allowed |
| /definitions/subgraphs/0/nodes/19/bgcolor | Node 289 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/19/color | Node 289 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/19/title | Node 289 (PrimitiveInt) | "Int (Split Steps)" | "Split Steps" | Allowed |
| /definitions/subgraphs/0/nodes/22/bgcolor | Node 292 (PrimitiveFloat) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/22/color | Node 292 (PrimitiveFloat) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/22/title | Node 292 (PrimitiveFloat) | "Float (CFG)" | "Guidance (CFG)" | Allowed |
| /definitions/subgraphs/0/nodes/23/bgcolor | Node 293 (PrimitiveFloat) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/23/color | Node 293 (PrimitiveFloat) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/23/title | Node 293 (PrimitiveFloat) | "Float (CFG)" | "Guidance (CFG)" | Allowed |
| /definitions/subgraphs/0/nodes/25/bgcolor | Node 296 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/25/color | Node 296 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/25/title | Node 296 (MarkdownNote) | (absent; ComfyUI default) | "Original Bernini Settings" | Allowed |
| /definitions/subgraphs/0/nodes/25/widgets_values/0 | Note 296 | "You can find the original settings here: https://github.com/bytedance/Bernini/blob/main/gradio_demo.py" | "See the [original Bernini settings](https://github.com/bytedance/Bernini/blob/main/gradio_demo.py) for the full-quality defaults." | Allowed |
| /definitions/subgraphs/0/nodes/25/widgets_values_named/text | Note 296 | "You can find the original settings here: https://github.com/bytedance/Bernini/blob/main/gradio_demo.py" | "See the [original Bernini settings](https://github.com/bytedance/Bernini/blob/main/gradio_demo.py) for the full-quality defaults." | Allowed |
| /definitions/subgraphs/0/nodes/26/bgcolor | Node 297 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/26/color | Node 297 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /definitions/subgraphs/0/nodes/28/bgcolor | Node 278 (BerniniConditioning) | "#533" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/28/color | Node 278 (BerniniConditioning) | "#322" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/29/bgcolor | Node 343 (ResolutionSelector) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/29/color | Node 343 (ResolutionSelector) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/29/title | Node 343 (ResolutionSelector) | (absent; ComfyUI default) | "Image Size (Ratio and Megapixels)" | Allowed |
| /definitions/subgraphs/0/nodes/30/bgcolor | Node 271 (LoraLoaderModelOnly) | "#593930" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/30/color | Node 271 (LoraLoaderModelOnly) | "#332922" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/32/bgcolor | Node 355 (LoraLoaderModelOnly) | "#593930" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/32/color | Node 355 (LoraLoaderModelOnly) | "#332922" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/33/bgcolor | Node 294 (PrimitiveBoolean) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/33/color | Node 294 (PrimitiveBoolean) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/33/title | Node 294 (PrimitiveBoolean) | "Boolean (Enable Turbo LoRA?)" | "Use Turbo LoRA" | Allowed |
| /definitions/subgraphs/1/nodes/0/bgcolor | Node 381 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/0/color | Node 381 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/1/nodes/0/title | Node 381 (PrimitiveInt) | "Seconds" | "Duration (Seconds)" | Allowed |
| /definitions/subgraphs/2/nodes/0/bgcolor | Node 1 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/0/color | Node 1 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/2/nodes/0/title | Node 1 (PreviewAny) | (absent; ComfyUI default) | "Line Index Preview" | Allowed |
| /definitions/subgraphs/2/nodes/2/bgcolor | Node 56 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/2/color | Node 56 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/2/nodes/2/title | Node 56 (PrimitiveInt) | "Int (line index)" | "Line Index" | Allowed |
| /groups/0/color | Group 10 | "#3f789e" | "#235B74" | Allowed |
| /groups/0/title | Group 10 | "Reference Image input" | "Reference Image Input" | Allowed |
| /nodes/0/bgcolor | Node 384 (SaveVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/0/color | Node 384 (SaveVideo) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/0/title | Node 384 (SaveVideo) | (absent; ComfyUI default) | "Save Video" | Allowed |
| /nodes/1/bgcolor | Node 385 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /nodes/1/color | Node 385 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /nodes/1/widgets_values/0 | Note 385 | "### Reference Image input (multi-image)\n\nUse this group when a task needs **one or more reference images** (`rv2v`, `r2v`, multi-piece outfits).\n\n1. **Load Image** — one node per reference (coat, pants, full outfit, face, etc.).\n2. **Batch Images** — connect each load to `image0`, `image1`, … (add slots as needed).\n3. **Subgraph** — connect **Batch Images → IMAGE** to **`reference_image`**.\n\nEach batched image becomes its own in-context token. Mention **`image0`, `image1`, …** in the user prompt if refs play different roles." | "### Use Multiple Reference Images\n\nFor tasks such as `rv2v` or `r2v`, load one image per **Reference Image** node. Connect them to **Batch Images** in order (`image0`, `image1`, and so on). Connect the batch’s **IMAGE** output to **reference_images**. In the prompt, use each slot name and describe what you want to borrow from it." | Allowed |
| /nodes/1/widgets_values_named/text | Note 385 | "### Reference Image input (multi-image)\n\nUse this group when a task needs **one or more reference images** (`rv2v`, `r2v`, multi-piece outfits).\n\n1. **Load Image** — one node per reference (coat, pants, full outfit, face, etc.).\n2. **Batch Images** — connect each load to `image0`, `image1`, … (add slots as needed).\n3. **Subgraph** — connect **Batch Images → IMAGE** to **`reference_image`**.\n\nEach batched image becomes its own in-context token. Mention **`image0`, `image1`, …** in the user prompt if refs play different roles." | "### Use Multiple Reference Images\n\nFor tasks such as `rv2v` or `r2v`, load one image per **Reference Image** node. Connect them to **Batch Images** in order (`image0`, `image1`, and so on). Connect the batch’s **IMAGE** output to **reference_images**. In the prompt, use each slot name and describe what you want to borrow from it." | Allowed |
| /nodes/2/bgcolor | Node 386 (961375a2-9e31-44b2-b783-985cbddf537c) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 386 (961375a2-9e31-44b2-b783-985cbddf537c) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/2/title | Node 386 (961375a2-9e31-44b2-b783-985cbddf537c) | (absent; ComfyUI default) | "Video Edit (Bernini-R)" | Allowed |
| /nodes/4/bgcolor | Node 389 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/4/color | Node 389 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/4/title | Node 389 (LoadImage) | (absent; ComfyUI default) | "Reference Image" | Allowed |
| /nodes/5/bgcolor | Node 390 (3fff3c09-5705-4010-8f31-6963e6b4dfa4) | "#3f5159" | "#30343B" | Allowed |
| /nodes/5/color | Node 390 (3fff3c09-5705-4010-8f31-6963e6b4dfa4) | "#2a363b" | "#715B2D" | Allowed |
| /nodes/5/title | Node 390 (3fff3c09-5705-4010-8f31-6963e6b4dfa4) | (absent; ComfyUI default) | "Duration (Seconds)" | Allowed |
| /nodes/6/bgcolor | Node 391 (PrimitiveFloat) | "#3f5159" | "#30343B" | Allowed |
| /nodes/6/color | Node 391 (PrimitiveFloat) | "#2a363b" | "#715B2D" | Allowed |
| /nodes/6/title | Node 391 (PrimitiveFloat) | "FPS (16 or 24)" | "Frame Rate (FPS, 16 or 24)" | Allowed |
| /nodes/7/bgcolor | Node 392 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /nodes/7/color | Node 392 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /nodes/7/title | Node 392 (MarkdownNote) | "Bernini-R Video Editing Guide" | "Quick Start" | Allowed |
| /nodes/7/widgets_values/0 | Note 392 | "## Bernini-R · Video Editing Workflow\n\n**Official repos**\n- Inference & task docs: [bytedance/Bernini](https://github.com/bytedance/Bernini)\n- Bernini-R weights (ComfyUI): [Comfy-Org/Bernini-R](https://huggingface.co/Comfy-Org/Bernini-R)\n- Paper: [Bernini: Latent Semantic Planning for Video Diffusion](https://arxiv.org/abs/2605.22344)\n\n---\n\n### What is this workflow?\n\nBuilt for **Bernini-R video editing** in ComfyUI: **source video** + optional **reference image(s)** / **reference video** → pick **task type** → write prompt → run.\n\nBernini-R is ByteDance's **renderer-only** Wan 2.2 model (in-context conditioning). It does **not** include the full Bernini MLLM planner. For official-quality long prompts, see `--use_pe` in the [Bernini repo](https://github.com/bytedance/Bernini).\n\n\| Task \| What to connect \|\n\|------\|-----------------\|\n\| Text to Video \| No media \|\n\| Video Editing (`v2v`, `mv2v`) \| `source_video` only \|\n\| Reference to Video (`r2v`) \| `reference_image(s)` only \|\n\| **Video Editing with Reference (`rv2v`)** \| `source_video` + `reference_image(s)` — **outfit / look swap** \|\n\| Ads / Content Insertion (`ads2v`) \| `source_video` + `reference_video` \|\n\n**Prompt format:** `{system prompt from task type}` + `{your English description}` via **Prompt Construction**.\n\n---\n\n### Inputs: source video, reference images, reference video\n\n**`source_video` (required for most edits)**\n- The clip to edit (canvas). Loaded via **Load Video** → subgraph `source_video`.\n- Resized to **`width × height`** and trimmed to **`length`** frames.\n- Match output size to your clip (e.g. portrait **832 × 1104**, landscape **848 × 480**). Both dimensions should be **multiples of 16**.\n\n**`reference_image(s)` (optional — group: Reference Image input)**\n- Used for **`rv2v`** (edit guided by refs), **`r2v`** (refs only), or multi-item outfits.\n- Each image is encoded as a **separate in-context stream**; long edge capped by **`ref_max_size`** (default **848**), **aspect ratio preserved**.\n- **How to wire:** put one or more **Load Image** nodes into **Batch Images** (`image0`, `image1`, …) → connect **Batch Images → IMAGE** to the subgraph input **`reference_image`**.\n- **Multi-image tips:** e.g. flat-lay coat + pants + boots on separate Load Image slots; in prompt use **image0, image1, …** (order = batch / slot order). Official training supports ~**5** reference streams reliably; the node allows up to **8** slots inside the graph.\n- **Not** resized to full canvas — only long-edge limited (unlike `source_video`).\n\n**`reference_video` (optional)**\n- Used for **`ads2v`** — content to **insert into** the source scene (moving clip, screen content, etc.).\n- Connect a **second video** (often **Load Video → Get Video Components → images**) to subgraph **`reference_video`**, or feed frame sequence as IMAGE.\n- Same **`ref_max_size`** / aspect rules as reference images; trimmed to **`length`** frames.\n- Prompt can be short: *Add the video on the computer.*\n\nLeave unused inputs **disconnected** for tasks that do not need them.\n\n---\n\n### Turbo mode (`enable_turbo_mode`)\n\n**Turbo = fast preview / iteration**, not the official Bernini-R sampling recipe.\n\n\| \| **Turbo ON** (default) \| **Turbo OFF** (Original settings) \|\n\|--\|------------------------\|-----------------------------------\|\n\| **LightX2V distill LoRA** \| ON (high noise **3.0**, low noise **1.5**) \| OFF (pure Bernini-R weights) \|\n\| **Total steps** \| **6** \| **40** (official default) \|\n\| **High / low split** \| **3** / **3** \| **20** / **20** \|\n\| **CFG** \| **1** \| **5** \|\n\nTurbo is much **faster** and lighter on VRAM, but **quality and edit fidelity** are usually below official **40-step** inference (which also uses APG guidance in Python — not fully replicated here). Use Turbo to test prompts and wiring; turn **Turbo OFF** for final exports or difficult edits (outfit swap, fine detail).\n\nToggle **`enable_turbo_mode`** on the main subgraph widget (or **Boolean Enable Turbo LoRA?** inside the graph).\n\nOfficial defaults reference: [gradio_demo.py](https://github.com/bytedance/Bernini/blob/main/gradio_demo.py)\n\n---\n\n### Recommended resolution & length\n\n\| Setting \| Recommended \|\n\|---------\|-------------\|\n\| **width × height** \| **848 × 480** or **832 × 480** (landscape); match source aspect for portrait \|\n\| **ref_max_size** \| **848** (raise to **1280** for 720p experiments) \|\n\| **length** \| **81** frames @ 16 fps; must be **4n+1** \|\n\nNegative prompt: Wan 2.2 **Chinese default** in `bernini/cli.py`.\n\n---\n\n### Task types & prompt examples\n\nEdits: **what to change** + **what stays unchanged**.\n\n- **`rv2v` (outfit swap):** *Remove the hat. Replace the person's clothing with the full outfit from the reference image … Keep pose, framing, lighting, background, and motion unchanged.*\n- **`v2v`:** *Add a snowman on the right … Keep the dog, road, and scene unchanged.*\n- **`mv2v`:** *Change the person's motion to crouch … preserving framing and background.*\n- **`ads2v`:** *Add the video on the computer.*\n- **`r2v`:** *The subject from image0 wearing items from image1 and image2 …*\n\nMore: [assets/testcases/](https://github.com/bytedance/Bernini/tree/main/assets/testcases/)\n\n---\n\n### Capability notes\n\n**Strengths:** video edit, reference-guided edit, outfit swap (`rv2v`), content insertion (`ads2v`), reference-to-video (`r2v`).\n\n**Limits:** no Bernini planner; Turbo ≠ official 40-step APG; long / 720p needs more VRAM; flat-lay outfit refs are harder than on-person reference photos.\n" | "### What It Does\n\nEdit a video with a written instruction and optional reference media. The task you choose determines which inputs you need.\n\n### How to Use\n\n1. For the saved setup, load the original clip in **Input Video** and the look or object to borrow in **Reference Image**. Use **Video Editing with Reference** in **Video Edit (Bernini-R)**.\n2. Describe what to change and what to keep. Set **Duration (Seconds)** and a frame rate of 16 or 24 FPS. Leave **Enable Turbo** on for a faster test.\n3. Click **Run**. **Save Video** writes `Bernini_r` files under `ComfyUI/output/video/`. See the task table below for other input setups.\n\n### Setup and Reference\n\n**Official repos**\n- Inference & task docs: [bytedance/Bernini](https://github.com/bytedance/Bernini)\n- Bernini-R weights (ComfyUI): [Comfy-Org/Bernini-R](https://huggingface.co/Comfy-Org/Bernini-R)\n- Paper: [Bernini: Latent Semantic Planning for Video Diffusion](https://arxiv.org/abs/2605.22344)\n\n---\n\nBernini-R is ByteDance's **renderer-only** Wan 2.2 model (in-context conditioning). It does **not** include the full Bernini MLLM planner. For official-quality long prompts, see `--use_pe` in the [Bernini repo](https://github.com/bytedance/Bernini).\n\n\| Task \| What to connect \|\n\|------\|-----------------\|\n\| Text to Video \| No media \|\n\| Video Editing (`v2v`, `mv2v`) \| `source_video` only \|\n\| Reference to Video (`r2v`) \| `reference_image(s)` only \|\n\| **Video Editing with Reference (`rv2v`)** \| `source_video` + `reference_image(s)` — **outfit / look swap** \|\n\| Ads / Content Insertion (`ads2v`) \| `source_video` + `reference_video` \|\n\n**Prompt format:** `{system prompt from task type}` + `{your English description}` via **Prompt Construction**.\n\n---\n\n### Inputs: source video, reference images, reference video\n\n**`source_video` (required for most edits)**\n- The clip to edit (canvas). Loaded via **Input Video** → subgraph `source_video`.\n- Resized to **`width × height`** and trimmed to **`length`** frames.\n- Match output size to your clip (e.g. portrait **832 × 1104**, landscape **848 × 480**). Both dimensions should be **multiples of 16**.\n\n**`reference_image(s)` (optional — group: Reference Image input)**\n- Used for **`rv2v`** (edit guided by refs), **`r2v`** (refs only), or multi-item outfits.\n- Each image is encoded as a **separate in-context stream**; long edge capped by **`ref_max_size`** (default **848**), **aspect ratio preserved**.\n- **How to wire:** put one or more **Load Image** nodes into **Batch Images** (`image0`, `image1`, …) → connect **Batch Images → IMAGE** to the subgraph input **`reference_image`**.\n- **Multi-image tips:** e.g. flat-lay coat + pants + boots on separate Load Image slots; in prompt use **image0, image1, …** (order = batch / slot order). Official training supports ~**5** reference streams reliably; the node allows up to **8** slots inside the graph.\n- **Not** resized to full canvas — only long-edge limited (unlike `source_video`).\n\n**`reference_video` (optional)**\n- Used for **`ads2v`** — content to **insert into** the source scene (moving clip, screen content, etc.).\n- Connect a **second video** (often **Load Video → Get Video Components → images**) to subgraph **`reference_video`**, or feed frame sequence as IMAGE.\n- Same **`ref_max_size`** / aspect rules as reference images; trimmed to **`length`** frames.\n- Prompt can be short: *Add the video on the computer.*\n\nLeave unused inputs **disconnected** for tasks that do not need them.\n\n---\n\n### Turbo mode (`enable_turbo_mode`)\n\n**Turbo = fast preview / iteration**, not the official Bernini-R sampling recipe.\n\n\| \| **Turbo ON** (default) \| **Turbo OFF** (Original settings) \|\n\|--\|------------------------\|-----------------------------------\|\n\| **LightX2V distill LoRA** \| ON (high noise **3.0**, low noise **1.5**) \| OFF (pure Bernini-R weights) \|\n\| **Total steps** \| **6** \| **40** (official default) \|\n\| **High / low split** \| **3** / **3** \| **20** / **20** \|\n\| **CFG** \| **1** \| **5** \|\n\nTurbo is much **faster** and lighter on VRAM, but **quality and edit fidelity** are usually below official **40-step** inference (which also uses APG guidance in Python — not fully replicated here). Use Turbo to test prompts and wiring; turn **Turbo OFF** for final exports or difficult edits (outfit swap, fine detail).\n\nToggle **Enable Turbo** on the main node (`enable_turbo_mode`) (or **Use Turbo LoRA** inside the graph).\n\nOfficial defaults reference: [gradio_demo.py](https://github.com/bytedance/Bernini/blob/main/gradio_demo.py)\n\n---\n\n### Recommended resolution & length\n\n\| Setting \| Recommended \|\n\|---------\|-------------\|\n\| **width × height** \| **848 × 480** or **832 × 480** (landscape); match source aspect for portrait \|\n\| **ref_max_size** \| **848** (raise to **1280** for 720p experiments) \|\n\| **length** \| **81** frames @ 16 fps; must be **4n+1** \|\n\nNegative prompt: Wan 2.2 **Chinese default** in `bernini/cli.py`.\n\n---\n\n### Task types & prompt examples\n\nEdits: **what to change** + **what stays unchanged**.\n\n- **`rv2v` (outfit swap):** *Remove the hat. Replace the person's clothing with the full outfit from the reference image … Keep pose, framing, lighting, background, and motion unchanged.*\n- **`v2v`:** *Add a snowman on the right … Keep the dog, road, and scene unchanged.*\n- **`mv2v`:** *Change the person's motion to crouch … preserving framing and background.*\n- **`ads2v`:** *Add the video on the computer.*\n- **`r2v`:** *The subject from image0 wearing items from image1 and image2 …*\n\nMore: [assets/testcases/](https://github.com/bytedance/Bernini/tree/main/assets/testcases/)\n\n---\n\n### Capability notes\n\n**Strengths:** video edit, reference-guided edit, outfit swap (`rv2v`), content insertion (`ads2v`), reference-to-video (`r2v`).\n\n**Limits:** no Bernini planner; Turbo ≠ official 40-step APG; long / 720p needs more VRAM; flat-lay outfit refs are harder than on-person reference photos." | Allowed |
| /nodes/7/widgets_values_named/text | Note 392 | "## Bernini-R · Video Editing Workflow\n\n**Official repos**\n- Inference & task docs: [bytedance/Bernini](https://github.com/bytedance/Bernini)\n- Bernini-R weights (ComfyUI): [Comfy-Org/Bernini-R](https://huggingface.co/Comfy-Org/Bernini-R)\n- Paper: [Bernini: Latent Semantic Planning for Video Diffusion](https://arxiv.org/abs/2605.22344)\n\n---\n\n### What is this workflow?\n\nBuilt for **Bernini-R video editing** in ComfyUI: **source video** + optional **reference image(s)** / **reference video** → pick **task type** → write prompt → run.\n\nBernini-R is ByteDance's **renderer-only** Wan 2.2 model (in-context conditioning). It does **not** include the full Bernini MLLM planner. For official-quality long prompts, see `--use_pe` in the [Bernini repo](https://github.com/bytedance/Bernini).\n\n\| Task \| What to connect \|\n\|------\|-----------------\|\n\| Text to Video \| No media \|\n\| Video Editing (`v2v`, `mv2v`) \| `source_video` only \|\n\| Reference to Video (`r2v`) \| `reference_image(s)` only \|\n\| **Video Editing with Reference (`rv2v`)** \| `source_video` + `reference_image(s)` — **outfit / look swap** \|\n\| Ads / Content Insertion (`ads2v`) \| `source_video` + `reference_video` \|\n\n**Prompt format:** `{system prompt from task type}` + `{your English description}` via **Prompt Construction**.\n\n---\n\n### Inputs: source video, reference images, reference video\n\n**`source_video` (required for most edits)**\n- The clip to edit (canvas). Loaded via **Load Video** → subgraph `source_video`.\n- Resized to **`width × height`** and trimmed to **`length`** frames.\n- Match output size to your clip (e.g. portrait **832 × 1104**, landscape **848 × 480**). Both dimensions should be **multiples of 16**.\n\n**`reference_image(s)` (optional — group: Reference Image input)**\n- Used for **`rv2v`** (edit guided by refs), **`r2v`** (refs only), or multi-item outfits.\n- Each image is encoded as a **separate in-context stream**; long edge capped by **`ref_max_size`** (default **848**), **aspect ratio preserved**.\n- **How to wire:** put one or more **Load Image** nodes into **Batch Images** (`image0`, `image1`, …) → connect **Batch Images → IMAGE** to the subgraph input **`reference_image`**.\n- **Multi-image tips:** e.g. flat-lay coat + pants + boots on separate Load Image slots; in prompt use **image0, image1, …** (order = batch / slot order). Official training supports ~**5** reference streams reliably; the node allows up to **8** slots inside the graph.\n- **Not** resized to full canvas — only long-edge limited (unlike `source_video`).\n\n**`reference_video` (optional)**\n- Used for **`ads2v`** — content to **insert into** the source scene (moving clip, screen content, etc.).\n- Connect a **second video** (often **Load Video → Get Video Components → images**) to subgraph **`reference_video`**, or feed frame sequence as IMAGE.\n- Same **`ref_max_size`** / aspect rules as reference images; trimmed to **`length`** frames.\n- Prompt can be short: *Add the video on the computer.*\n\nLeave unused inputs **disconnected** for tasks that do not need them.\n\n---\n\n### Turbo mode (`enable_turbo_mode`)\n\n**Turbo = fast preview / iteration**, not the official Bernini-R sampling recipe.\n\n\| \| **Turbo ON** (default) \| **Turbo OFF** (Original settings) \|\n\|--\|------------------------\|-----------------------------------\|\n\| **LightX2V distill LoRA** \| ON (high noise **3.0**, low noise **1.5**) \| OFF (pure Bernini-R weights) \|\n\| **Total steps** \| **6** \| **40** (official default) \|\n\| **High / low split** \| **3** / **3** \| **20** / **20** \|\n\| **CFG** \| **1** \| **5** \|\n\nTurbo is much **faster** and lighter on VRAM, but **quality and edit fidelity** are usually below official **40-step** inference (which also uses APG guidance in Python — not fully replicated here). Use Turbo to test prompts and wiring; turn **Turbo OFF** for final exports or difficult edits (outfit swap, fine detail).\n\nToggle **`enable_turbo_mode`** on the main subgraph widget (or **Boolean Enable Turbo LoRA?** inside the graph).\n\nOfficial defaults reference: [gradio_demo.py](https://github.com/bytedance/Bernini/blob/main/gradio_demo.py)\n\n---\n\n### Recommended resolution & length\n\n\| Setting \| Recommended \|\n\|---------\|-------------\|\n\| **width × height** \| **848 × 480** or **832 × 480** (landscape); match source aspect for portrait \|\n\| **ref_max_size** \| **848** (raise to **1280** for 720p experiments) \|\n\| **length** \| **81** frames @ 16 fps; must be **4n+1** \|\n\nNegative prompt: Wan 2.2 **Chinese default** in `bernini/cli.py`.\n\n---\n\n### Task types & prompt examples\n\nEdits: **what to change** + **what stays unchanged**.\n\n- **`rv2v` (outfit swap):** *Remove the hat. Replace the person's clothing with the full outfit from the reference image … Keep pose, framing, lighting, background, and motion unchanged.*\n- **`v2v`:** *Add a snowman on the right … Keep the dog, road, and scene unchanged.*\n- **`mv2v`:** *Change the person's motion to crouch … preserving framing and background.*\n- **`ads2v`:** *Add the video on the computer.*\n- **`r2v`:** *The subject from image0 wearing items from image1 and image2 …*\n\nMore: [assets/testcases/](https://github.com/bytedance/Bernini/tree/main/assets/testcases/)\n\n---\n\n### Capability notes\n\n**Strengths:** video edit, reference-guided edit, outfit swap (`rv2v`), content insertion (`ads2v`), reference-to-video (`r2v`).\n\n**Limits:** no Bernini planner; Turbo ≠ official 40-step APG; long / 720p needs more VRAM; flat-lay outfit refs are harder than on-person reference photos.\n" | "### What It Does\n\nEdit a video with a written instruction and optional reference media. The task you choose determines which inputs you need.\n\n### How to Use\n\n1. For the saved setup, load the original clip in **Input Video** and the look or object to borrow in **Reference Image**. Use **Video Editing with Reference** in **Video Edit (Bernini-R)**.\n2. Describe what to change and what to keep. Set **Duration (Seconds)** and a frame rate of 16 or 24 FPS. Leave **Enable Turbo** on for a faster test.\n3. Click **Run**. **Save Video** writes `Bernini_r` files under `ComfyUI/output/video/`. See the task table below for other input setups.\n\n### Setup and Reference\n\n**Official repos**\n- Inference & task docs: [bytedance/Bernini](https://github.com/bytedance/Bernini)\n- Bernini-R weights (ComfyUI): [Comfy-Org/Bernini-R](https://huggingface.co/Comfy-Org/Bernini-R)\n- Paper: [Bernini: Latent Semantic Planning for Video Diffusion](https://arxiv.org/abs/2605.22344)\n\n---\n\nBernini-R is ByteDance's **renderer-only** Wan 2.2 model (in-context conditioning). It does **not** include the full Bernini MLLM planner. For official-quality long prompts, see `--use_pe` in the [Bernini repo](https://github.com/bytedance/Bernini).\n\n\| Task \| What to connect \|\n\|------\|-----------------\|\n\| Text to Video \| No media \|\n\| Video Editing (`v2v`, `mv2v`) \| `source_video` only \|\n\| Reference to Video (`r2v`) \| `reference_image(s)` only \|\n\| **Video Editing with Reference (`rv2v`)** \| `source_video` + `reference_image(s)` — **outfit / look swap** \|\n\| Ads / Content Insertion (`ads2v`) \| `source_video` + `reference_video` \|\n\n**Prompt format:** `{system prompt from task type}` + `{your English description}` via **Prompt Construction**.\n\n---\n\n### Inputs: source video, reference images, reference video\n\n**`source_video` (required for most edits)**\n- The clip to edit (canvas). Loaded via **Input Video** → subgraph `source_video`.\n- Resized to **`width × height`** and trimmed to **`length`** frames.\n- Match output size to your clip (e.g. portrait **832 × 1104**, landscape **848 × 480**). Both dimensions should be **multiples of 16**.\n\n**`reference_image(s)` (optional — group: Reference Image input)**\n- Used for **`rv2v`** (edit guided by refs), **`r2v`** (refs only), or multi-item outfits.\n- Each image is encoded as a **separate in-context stream**; long edge capped by **`ref_max_size`** (default **848**), **aspect ratio preserved**.\n- **How to wire:** put one or more **Load Image** nodes into **Batch Images** (`image0`, `image1`, …) → connect **Batch Images → IMAGE** to the subgraph input **`reference_image`**.\n- **Multi-image tips:** e.g. flat-lay coat + pants + boots on separate Load Image slots; in prompt use **image0, image1, …** (order = batch / slot order). Official training supports ~**5** reference streams reliably; the node allows up to **8** slots inside the graph.\n- **Not** resized to full canvas — only long-edge limited (unlike `source_video`).\n\n**`reference_video` (optional)**\n- Used for **`ads2v`** — content to **insert into** the source scene (moving clip, screen content, etc.).\n- Connect a **second video** (often **Load Video → Get Video Components → images**) to subgraph **`reference_video`**, or feed frame sequence as IMAGE.\n- Same **`ref_max_size`** / aspect rules as reference images; trimmed to **`length`** frames.\n- Prompt can be short: *Add the video on the computer.*\n\nLeave unused inputs **disconnected** for tasks that do not need them.\n\n---\n\n### Turbo mode (`enable_turbo_mode`)\n\n**Turbo = fast preview / iteration**, not the official Bernini-R sampling recipe.\n\n\| \| **Turbo ON** (default) \| **Turbo OFF** (Original settings) \|\n\|--\|------------------------\|-----------------------------------\|\n\| **LightX2V distill LoRA** \| ON (high noise **3.0**, low noise **1.5**) \| OFF (pure Bernini-R weights) \|\n\| **Total steps** \| **6** \| **40** (official default) \|\n\| **High / low split** \| **3** / **3** \| **20** / **20** \|\n\| **CFG** \| **1** \| **5** \|\n\nTurbo is much **faster** and lighter on VRAM, but **quality and edit fidelity** are usually below official **40-step** inference (which also uses APG guidance in Python — not fully replicated here). Use Turbo to test prompts and wiring; turn **Turbo OFF** for final exports or difficult edits (outfit swap, fine detail).\n\nToggle **Enable Turbo** on the main node (`enable_turbo_mode`) (or **Use Turbo LoRA** inside the graph).\n\nOfficial defaults reference: [gradio_demo.py](https://github.com/bytedance/Bernini/blob/main/gradio_demo.py)\n\n---\n\n### Recommended resolution & length\n\n\| Setting \| Recommended \|\n\|---------\|-------------\|\n\| **width × height** \| **848 × 480** or **832 × 480** (landscape); match source aspect for portrait \|\n\| **ref_max_size** \| **848** (raise to **1280** for 720p experiments) \|\n\| **length** \| **81** frames @ 16 fps; must be **4n+1** \|\n\nNegative prompt: Wan 2.2 **Chinese default** in `bernini/cli.py`.\n\n---\n\n### Task types & prompt examples\n\nEdits: **what to change** + **what stays unchanged**.\n\n- **`rv2v` (outfit swap):** *Remove the hat. Replace the person's clothing with the full outfit from the reference image … Keep pose, framing, lighting, background, and motion unchanged.*\n- **`v2v`:** *Add a snowman on the right … Keep the dog, road, and scene unchanged.*\n- **`mv2v`:** *Change the person's motion to crouch … preserving framing and background.*\n- **`ads2v`:** *Add the video on the computer.*\n- **`r2v`:** *The subject from image0 wearing items from image1 and image2 …*\n\nMore: [assets/testcases/](https://github.com/bytedance/Bernini/tree/main/assets/testcases/)\n\n---\n\n### Capability notes\n\n**Strengths:** video edit, reference-guided edit, outfit swap (`rv2v`), content insertion (`ads2v`), reference-to-video (`r2v`).\n\n**Limits:** no Bernini planner; Turbo ≠ official 40-step APG; long / 720p needs more VRAM; flat-lay outfit refs are harder than on-person reference photos." | Allowed |
| /nodes/8/bgcolor | Node 393 (VHS_LoadVideo) | "#3f5159" | "#30343B" | Allowed |
| /nodes/8/color | Node 393 (VHS_LoadVideo) | "#2a363b" | "#235B74" | Allowed |
| /nodes/8/title | Node 393 (VHS_LoadVideo) | (absent; ComfyUI default) | "Input Video" | Allowed |

## Ideogram4 Playground.json

Result: **PASS** — 60 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Ideogram4 Playground.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: 210.

Original SHA-256: `366c89104e96905dfd71d0dc5440b39e6a99356eb2fecd3f8ac552e66adf2223`

Modified SHA-256: `0f9b43334fb70ce593f344ee6d918ff9bcd38b326bd5d17ce1bc231728123e04`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/color | Group 2 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/2/color | Group 3 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/3/color | Group 4 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/4/color | Group 5 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/0/groups/5/color | Group 9 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/0/nodes/7/title | Node 24 (CLIPTextEncode) | "CLIP Text Encode (Positive Prompt)" | "Positive Prompt" | Allowed |
| /definitions/subgraphs/0/nodes/9/bgcolor | Node 27 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/9/color | Node 27 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/9/title | Node 27 (PrimitiveInt) | "Int (Width)" | "Width (Pixels)" | Allowed |
| /definitions/subgraphs/0/nodes/10/bgcolor | Node 28 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/10/color | Node 28 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/10/title | Node 28 (PrimitiveInt) | "Int (Height)" | "Height (Pixels)" | Allowed |
| /definitions/subgraphs/3/groups/0/color | Group 14 | "#3f789e" | "#35414A" | Allowed |
| /groups/0/color | Group 10 | "#3f789e" | "#35414A" | Allowed |
| /groups/1/color | Group 11 | "#3f789e" | "#35414A" | Allowed |
| /groups/2/color | Group 12 | "#3f789e" | "#35414A" | Allowed |
| /groups/3/color | Group 13 | "#3f789e" | "#35414A" | Allowed |
| /groups/3/title | Group 13 | "Post" | "Image Finishing" | Allowed |
| /nodes/0/bgcolor | Node 111 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/0/color | Node 111 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/0/title | Node 111 (PreviewAny) | (absent; ComfyUI default) | "Prompt Preview" | Allowed |
| /nodes/1/bgcolor | Node 158 (SaveImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/1/color | Node 158 (SaveImage) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/1/title | Node 158 (SaveImage) | (absent; ComfyUI default) | "Save Image" | Allowed |
| /nodes/2/bgcolor | Node 185 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 185 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/2/title | Node 185 (PreviewAny) | (absent; ComfyUI default) | "Prompt Preview" | Allowed |
| /nodes/3/bgcolor | Node 37 (ResolutionSelector) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/3/color | Node 37 (ResolutionSelector) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/3/title | Node 37 (ResolutionSelector) | (absent; ComfyUI default) | "Image Size (Ratio and Megapixels)" | Allowed |
| /nodes/4/bgcolor | Node 191 (52d489ca-ffb3-4e04-8508-5d3db8beae91) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/4/color | Node 191 (52d489ca-ffb3-4e04-8508-5d3db8beae91) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/4/title | Node 191 (52d489ca-ffb3-4e04-8508-5d3db8beae91) | (absent; ComfyUI default) | "Image to Ideogram Prompt" | Allowed |
| /nodes/5/bgcolor | Node 186 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/5/color | Node 186 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/5/title | Node 186 (PreviewAny) | (absent; ComfyUI default) | "Prompt Preview" | Allowed |
| /nodes/6/bgcolor | Node 181 (9eb09529-b883-46ac-9be4-8e0defa39daa) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/6/color | Node 181 (9eb09529-b883-46ac-9be4-8e0defa39daa) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/6/title | Node 181 (9eb09529-b883-46ac-9be4-8e0defa39daa) | (absent; ComfyUI default) | "Image to Ideogram Prompt" | Allowed |
| /nodes/7/bgcolor | Node 198 (SaveImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/7/color | Node 198 (SaveImage) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/7/title | Node 198 (SaveImage) | (absent; ComfyUI default) | "Save Image" | Allowed |
| /nodes/12/bgcolor | Node 199 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/12/color | Node 199 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/12/title | Node 199 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "Image Comparison" | Allowed |
| /nodes/14/bgcolor | Node 177 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/14/color | Node 177 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/14/title | Node 177 (LoadImage) | (absent; ComfyUI default) | "Reference Image" | Allowed |
| /nodes/16/bgcolor | Node 98 (83e6e004-48ea-408e-9024-eb49c3d7dc14) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/16/color | Node 98 (83e6e004-48ea-408e-9024-eb49c3d7dc14) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/16/title | Node 98 (83e6e004-48ea-408e-9024-eb49c3d7dc14) | (absent; ComfyUI default) | "Text to Image (Ideogram4)" | Allowed |
| /nodes/17/bgcolor | Node 208 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/17/color | Node 208 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/17/title | Node 208 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "Image Comparison" | Allowed |
| /nodes/18/bgcolor | Node 209 (72fb4e2f-3839-4b7c-9b8e-9cd1ad1952ae) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/18/color | Node 209 (72fb4e2f-3839-4b7c-9b8e-9cd1ad1952ae) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/18/title | Node 209 (72fb4e2f-3839-4b7c-9b8e-9cd1ad1952ae) | (absent; ComfyUI default) | "Upscale Image (SeedVR2 7B Int8)" | Allowed |
| /nodes/19 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 210, "type": "MarkdownNote", "pos": [3140, 440], "size": [480, 360], "flags": {}, "order": 19, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nCreate an image from a description and compare it with enlarged and finished versions.\n\n### How to Use\n\n1. In **Ideogram4PromptBuilderKJ**, enter your description in **high_level_description**. Set **width** and **height** there too.\n2. Keep the saved settings and leave the disabled reference branches alone for a first run.\n3. Click **Run**. See **Image Comparison** for the differences. The **Save Image** nodes write the original and finished images under `ComfyUI/output/`."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 209 | 210 | Allowed |

## Klein Dataset Maker.json

Result: **PASS** — 49 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Klein Dataset Maker.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: 381.

Original SHA-256: `8587ab881ad559f66624aa9633ae79aed75f6435c51373d865afc3af3e661f7c`

Modified SHA-256: `c254fc08290619a4e4a257e4b6be484fc5017be4ba73749848d4eea745f267ab`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /groups/0/color | Group 1 | "#8AA" | "#35414A" | Allowed |
| /groups/1/color | Group 2 | "#a1309b" | "#35414A" | Allowed |
| /groups/2/color | Group 3 | "#3f789e" | "#35414A" | Allowed |
| /groups/3/color | Group 4 | "#a1309b" | "#35414A" | Allowed |
| /groups/3/title | Group 4 | "CR Prompt List (Set batch of 20 when running)" | "CR Prompt List (Set Batch of 20 when Running)" | Allowed |
| /nodes/0/bgcolor | Node 153 (GetImageSize) | "#000" | "#30343B" | Allowed |
| /nodes/0/color | Node 153 (GetImageSize) | "#222" | "#35414A" | Allowed |
| /nodes/1/bgcolor | Node 351 (CLIPTextEncode) | "#535" | "#30343B" | Allowed |
| /nodes/1/color | Node 351 (CLIPTextEncode) | "#323" | "#35414A" | Allowed |
| /nodes/2/bgcolor | Node 146 (CLIPLoader) | "#3f5159" | "#30343B" | Allowed |
| /nodes/2/color | Node 146 (CLIPLoader) | "#2a363b" | "#35414A" | Allowed |
| /nodes/3/bgcolor | Node 149 (VAELoader) | "#3f5159" | "#30343B" | Allowed |
| /nodes/3/color | Node 149 (VAELoader) | "#2a363b" | "#35414A" | Allowed |
| /nodes/4/bgcolor | Node 155 (VAEEncode) | "#000" | "#30343B" | Allowed |
| /nodes/4/color | Node 155 (VAEEncode) | "#222" | "#35414A" | Allowed |
| /nodes/5/bgcolor | Node 156 (ReferenceLatent) | "#000" | "#30343B" | Allowed |
| /nodes/5/color | Node 156 (ReferenceLatent) | "#222" | "#35414A" | Allowed |
| /nodes/6/bgcolor | Node 154 (ReferenceLatent) | "#000" | "#30343B" | Allowed |
| /nodes/6/color | Node 154 (ReferenceLatent) | "#222" | "#35414A" | Allowed |
| /nodes/7/bgcolor | Node 159 (ConditioningZeroOut) | "#000" | "#30343B" | Allowed |
| /nodes/7/color | Node 159 (ConditioningZeroOut) | "#222" | "#35414A" | Allowed |
| /nodes/8/bgcolor | Node 377 (CR Prompt List) | "#535" | "#30343B" | Allowed |
| /nodes/8/color | Node 377 (CR Prompt List) | "#323" | "#235B74" | Allowed |
| /nodes/8/title | Node 377 (CR Prompt List) | (absent; ComfyUI default) | "Dataset Prompts" | Allowed |
| /nodes/9/bgcolor | Node 179 (EmptyFlux2LatentImage) | "#355" | "#30343B" | Allowed |
| /nodes/9/color | Node 179 (EmptyFlux2LatentImage) | "#233" | "#35414A" | Allowed |
| /nodes/10/bgcolor | Node 342 (Flux2Scheduler) | "#355" | "#30343B" | Allowed |
| /nodes/10/color | Node 342 (Flux2Scheduler) | "#233" | "#35414A" | Allowed |
| /nodes/11/bgcolor | Node 308 (KSamplerSelect) | "#355" | "#30343B" | Allowed |
| /nodes/11/color | Node 308 (KSamplerSelect) | "#233" | "#35414A" | Allowed |
| /nodes/12/bgcolor | Node 186 (CFGGuider) | "#355" | "#30343B" | Allowed |
| /nodes/12/color | Node 186 (CFGGuider) | "#233" | "#35414A" | Allowed |
| /nodes/13/bgcolor | Node 280 (SaveImage) | "#653" | "#30343B" | Allowed |
| /nodes/13/color | Node 280 (SaveImage) | "#432" | "#2B644C" | Allowed |
| /nodes/13/title | Node 280 (SaveImage) | "Save Image (Set your directory)" | "Save Image (Set Your Directory)" | Allowed |
| /nodes/14/bgcolor | Node 188 (SamplerCustomAdvanced) | "#355" | "#30343B" | Allowed |
| /nodes/14/color | Node 188 (SamplerCustomAdvanced) | "#233" | "#35414A" | Allowed |
| /nodes/15/bgcolor | Node 143 (VAEDecode) | "#355" | "#30343B" | Allowed |
| /nodes/15/color | Node 143 (VAEDecode) | "#233" | "#35414A" | Allowed |
| /nodes/16/bgcolor | Node 185 (RandomNoise) | "#355" | "#30343B" | Allowed |
| /nodes/16/color | Node 185 (RandomNoise) | "#233" | "#35414A" | Allowed |
| /nodes/17/bgcolor | Node 151 (ImageScaleToTotalPixels) | "#000" | "#30343B" | Allowed |
| /nodes/17/color | Node 151 (ImageScaleToTotalPixels) | "#222" | "#35414A" | Allowed |
| /nodes/18/bgcolor | Node 76 (LoadImage) | "#353" | "#30343B" | Allowed |
| /nodes/18/color | Node 76 (LoadImage) | "#232" | "#235B74" | Allowed |
| /nodes/20/bgcolor | Node 145 (UNETLoader) | "#3f5159" | "#30343B" | Allowed |
| /nodes/20/color | Node 145 (UNETLoader) | "#2a363b" | "#35414A" | Allowed |
| /nodes/21 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 381, "type": "MarkdownNote", "pos": [-1380, 280], "size": [480, 360], "flags": {}, "order": 21, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nCreate a set of images from one reference headshot and a list of prompts.\n\n### How to Use\n\n1. Load the subject in **Reference Headshot**.\n2. Enter one description per line in **Dataset Prompts**. Set **max_rows** to 1 for a first test. Use **start_index** and **max_rows** to pick rows. For a 20-row batch, follow the batch-size instruction on the **CR Prompt List** group.\n3. Set **filename_prefix** in **Save Image (Set Your Directory)** to choose the folder and name under `ComfyUI/output/`, then click **Run**."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 380 | 381 | Allowed |

## Klein Edit.json

Result: **PASS** — 61 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Klein Edit.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: none.

Original SHA-256: `2f5adf928353ecf10a8f821ecdb85dad4a0dddd786de6b09954724d8b15b5c47`

Modified SHA-256: `1e2cef1d88ec154bd924249dfc9e4090b46932387b45864d422a748a531808ad`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/color | Group 2 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/2/color | Group 3 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/3/color | Group 5 | "#3f789e" | "#235B74" | Allowed |
| /definitions/subgraphs/0/groups/3/title | Group 5 | "image 1" | "Image 1" | Allowed |
| /definitions/subgraphs/0/groups/4/color | Group 6 | "#3f789e" | "#235B74" | Allowed |
| /definitions/subgraphs/0/groups/4/title | Group 6 | "image 2" | "Image 2" | Allowed |
| /definitions/subgraphs/0/nodes/13/bgcolor | Node 722 (CLIPTextEncode) | "#353" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/13/color | Node 722 (CLIPTextEncode) | "#232" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/13/title | Node 722 (CLIPTextEncode) | "CLIP Text Encode (Positive Prompt)" | "Positive Prompt" | Allowed |
| /definitions/subgraphs/0/nodes/20/bgcolor | Node 728 (PrimitiveFloat) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/20/color | Node 728 (PrimitiveFloat) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/1/groups/0/color | Group 2 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/1/groups/0/title | Group 2 | "Step2 - Image size" | "Step 2 - Image Size" | Allowed |
| /definitions/subgraphs/1/groups/1/color | Group 3 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/1/groups/1/title | Group 3 | "Step3 - Prompt" | "Step 3 - Prompt" | Allowed |
| /definitions/subgraphs/1/groups/2/color | Group 4 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/1/groups/2/title | Group 4 | "Step1 - Load models" | "Step 1 - Load Models" | Allowed |
| /definitions/subgraphs/2/groups/0/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/2/groups/1/color | Group 2 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/2/groups/2/color | Group 3 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/11/bgcolor | Node 74 (CLIPTextEncode) | "#353" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/11/color | Node 74 (CLIPTextEncode) | "#232" | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/11/title | Node 74 (CLIPTextEncode) | "CLIP Text Encode (Positive Prompt)" | "Positive Prompt" | Allowed |
| /groups/0/color | Group 10 | "#3f789e" | "#35414A" | Allowed |
| /groups/1/color | Group 14 | "#3f789e" | "#35414A" | Allowed |
| /groups/1/title | Group 14 | "Multiple input example（Select all nodes then Ctrl-B to enable/disable）" | "Multiple Input Example (Select All Nodes, Ctrl+B to Enable/Disable)" | Allowed |
| /nodes/0/bgcolor | Node 740 (SaveImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/0/color | Node 740 (SaveImage) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/0/title | Node 740 (SaveImage) | (absent; ComfyUI default) | "Save Image" | Allowed |
| /nodes/1/bgcolor | Node 735 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/1/color | Node 735 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/1/title | Node 735 (LoadImage) | (absent; ComfyUI default) | "Reference Image" | Allowed |
| /nodes/2/bgcolor | Node 732 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /nodes/2/color | Node 732 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /nodes/2/title | Node 732 (MarkdownNote) | (absent; ComfyUI default) | "Quick Start" | Allowed |
| /nodes/2/widgets_values/0 | Note 732 | "Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)\n\n## Model links (for local users)\n\n\n**diffusion_models**\n\n- [flux-2-klein-9b-fp8.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-fp8)\n\n> Please visit BFL's repo, accept the agreement in the repo, and then download the models.\n\n**text_encoders**\n\n- [qwen_3_8b_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/flux2-klein-9B/resolve/main/split_files/text_encoders/qwen_3_8b_fp8mixed.safetensors)\n\n**vae**\n\n- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors)\n\n\nModel Storage Location\n\n```\n📂 ComfyUI/\n├── 📂 models/\n│   ├── 📂 diffusion_models/\n│   │      └── flux-2-klein-9b-fp8.safetensors\n│   ├── 📂 text_encoders/\n│   │      └── qwen_3_8b_fp8mixed.safetensors\n│   └── 📂 vae/\n│          └── flux2-vae.safetensors\n```\n## Report issue\n\nNote: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.\n\n- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)\n- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)\n- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)\n" | "### What It Does\n\nEdit an existing image with a written instruction using FLUX.2 Klein.\n\n### How to Use\n\n1. Load your image in the active **Reference Image** node. In **Image Edit (FLUX.2 Klein 9B Distilled)**, describe what should change and what should stay.\n2. Click **Run**. Check **Image Comparison** and look for `Flux2-Klein` files under `ComfyUI/output/`.\n3. Start with the single-image branch. The two-image example and Z-Image pass are disabled in the saved setup.\n\n### Model Files and Setup\n\nGuide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)\n\n## Model links (for local users)\n\n\n**diffusion_models**\n\n- [flux-2-klein-9b-fp8.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-fp8)\n\n> Please visit BFL's repo, accept the agreement in the repo, and then download the models.\n\n**text_encoders**\n\n- [qwen_3_8b_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/flux2-klein-9B/resolve/main/split_files/text_encoders/qwen_3_8b_fp8mixed.safetensors)\n\n**vae**\n\n- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors)\n\n\nModel Storage Location\n\n```\n📂 ComfyUI/\n├── 📂 models/\n│   ├── 📂 diffusion_models/\n│   │      └── flux-2-klein-9b-fp8.safetensors\n│   ├── 📂 text_encoders/\n│   │      └── qwen_3_8b_fp8mixed.safetensors\n│   └── 📂 vae/\n│          └── flux2-vae.safetensors\n```\n## Report issue\n\nNote: please update ComfyUI first ([guide](https://docs.comfy.org/installation/update_comfyui)) and prepare required models. Desktop/Cloud will be updated after the stable release; nightly-supported models may not be included yet, please wait for the next stable release.\n\n- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/Comfy-Org/ComfyUI/issues)\n- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)\n- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)" | Allowed |
| /nodes/3/bgcolor | Node 736 (9104fd18-55a4-4273-aad6-033c432b4288) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/3/color | Node 736 (9104fd18-55a4-4273-aad6-033c432b4288) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/3/title | Node 736 (9104fd18-55a4-4273-aad6-033c432b4288) | (absent; ComfyUI default) | "Image Edit (FLUX.2 Klein 9B Distilled)" | Allowed |
| /nodes/4/bgcolor | Node 741 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/4/color | Node 741 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/4/title | Node 741 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "Image Comparison" | Allowed |
| /nodes/5/bgcolor | Node 737 (SaveImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/5/color | Node 737 (SaveImage) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/5/title | Node 737 (SaveImage) | (absent; ComfyUI default) | "Save Image" | Allowed |
| /nodes/6/bgcolor | Node 734 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/6/color | Node 734 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/6/title | Node 734 (LoadImage) | (absent; ComfyUI default) | "Reference Image" | Allowed |
| /nodes/7/bgcolor | Node 742 (3b7f0d99-e689-4d7a-99dc-4e82694cb9d6) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/7/color | Node 742 (3b7f0d99-e689-4d7a-99dc-4e82694cb9d6) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/7/title | Node 742 (3b7f0d99-e689-4d7a-99dc-4e82694cb9d6) | (absent; ComfyUI default) | "Image Edit (FLUX.2 Klein 9B Distilled)" | Allowed |
| /nodes/8/bgcolor | Node 785 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/8/color | Node 785 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/8/title | Node 785 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "Image Comparison" | Allowed |
| /nodes/9/bgcolor | Node 738 (SaveImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/9/color | Node 738 (SaveImage) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/9/title | Node 738 (SaveImage) | (absent; ComfyUI default) | "Save Image" | Allowed |
| /nodes/10/bgcolor | Node 739 (b7d8ecf2-5665-4712-b5d6-b3048259e851) | "#355" | "#30343B" | Allowed |
| /nodes/10/color | Node 739 (b7d8ecf2-5665-4712-b5d6-b3048259e851) | "#233" | "#715B2D" | Allowed |
| /nodes/10/title | Node 739 (b7d8ecf2-5665-4712-b5d6-b3048259e851) | (absent; ComfyUI default) | "Z-Image Pass with LoRA" | Allowed |

## Klein Face Maker.json

Result: **PASS** — 106 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Klein Face Maker.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: 365.

Original SHA-256: `ac8214c91f568229890e7cdd5209ccad8430bad55469f2c4d4c56d214840c907`

Modified SHA-256: `8a0bc82090e37782cca2eeb4005364fd99d97abf895770948046319f09d13e9a`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/nodes/3/bgcolor | Node 59 (Flux2Scheduler) | "#3f5159" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/3/color | Node 59 (Flux2Scheduler) | "#2a363b" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/4/bgcolor | Node 60 (CFGGuider) | "#3f5159" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/4/color | Node 60 (CFGGuider) | "#2a363b" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/5/bgcolor | Node 13 (SamplerCustomAdvanced) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/5/color | Node 13 (SamplerCustomAdvanced) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/1/nodes/1/bgcolor | Node 329 (GrowMask) | "#47392a" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/1/color | Node 329 (GrowMask) | "#5b4d3e" | "#35414A" | Allowed |
| /definitions/subgraphs/1/nodes/3/bgcolor | Node 331 (ReferenceLatent) | "#3f5159" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/3/color | Node 331 (ReferenceLatent) | "#2a363b" | "#35414A" | Allowed |
| /definitions/subgraphs/1/nodes/4/bgcolor | Node 332 (DrawMaskOnImage) | "#292929" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/4/color | Node 332 (DrawMaskOnImage) | "#3d3d3d" | "#35414A" | Allowed |
| /definitions/subgraphs/1/nodes/4/title | Node 332 (DrawMaskOnImage) | "Draw Mask (ımg1)" | "Draw Mask (Image 1)" | Allowed |
| /definitions/subgraphs/1/nodes/5/bgcolor | Node 333 (VAEEncode) | "#593930" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/5/color | Node 333 (VAEEncode) | "#332922" | "#35414A" | Allowed |
| /definitions/subgraphs/1/nodes/6/bgcolor | Node 334 (MaskComposite) | "#292929" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/6/color | Node 334 (MaskComposite) | "#3d3d3d" | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/0/bgcolor | Node 339 (GrowMask) | "#47392a" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/0/color | Node 339 (GrowMask) | "#5b4d3e" | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/1/bgcolor | Node 340 (ReferenceLatent) | "#3f5159" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/1/color | Node 340 (ReferenceLatent) | "#2a363b" | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/3/bgcolor | Node 342 (DrawMaskOnImage) | "#292929" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/3/color | Node 342 (DrawMaskOnImage) | "#3d3d3d" | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/3/title | Node 342 (DrawMaskOnImage) | "Draw Mask (ımg1)" | "Draw Mask (Image 2)" | Allowed |
| /definitions/subgraphs/2/nodes/4/bgcolor | Node 343 (VAEEncode) | "#593930" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/4/color | Node 343 (VAEEncode) | "#332922" | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/5/bgcolor | Node 344 (MaskComposite) | "#292929" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/5/color | Node 344 (MaskComposite) | "#3d3d3d" | "#35414A" | Allowed |
| /definitions/subgraphs/3/nodes/0/bgcolor | Node 351 (ReferenceLatent) | "#3f5159" | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/0/color | Node 351 (ReferenceLatent) | "#2a363b" | "#35414A" | Allowed |
| /definitions/subgraphs/3/nodes/2/bgcolor | Node 353 (DrawMaskOnImage) | "#292929" | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/2/color | Node 353 (DrawMaskOnImage) | "#3d3d3d" | "#35414A" | Allowed |
| /definitions/subgraphs/3/nodes/2/title | Node 353 (DrawMaskOnImage) | "Draw Mask (ımg1)" | "Draw Mask (Image 3)" | Allowed |
| /definitions/subgraphs/3/nodes/3/bgcolor | Node 354 (GrowMask) | "#47392a" | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/3/color | Node 354 (GrowMask) | "#5b4d3e" | "#35414A" | Allowed |
| /definitions/subgraphs/3/nodes/4/bgcolor | Node 356 (VAEEncode) | "#593930" | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/4/color | Node 356 (VAEEncode) | "#332922" | "#35414A" | Allowed |
| /definitions/subgraphs/3/nodes/5/bgcolor | Node 355 (MaskComposite) | "#292929" | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/5/color | Node 355 (MaskComposite) | "#3d3d3d" | "#35414A" | Allowed |
| /groups/0/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /groups/1/color | Group 2 | "#3f789e" | "#35414A" | Allowed |
| /groups/2/color | Group 3 | "#3f789e" | "#35414A" | Allowed |
| /nodes/0/bgcolor | Node 90 (PreviewImage) | "#563453" | "#30343B" | Allowed |
| /nodes/0/color | Node 90 (PreviewImage) | "#6a4867" | "#594A72" | Allowed |
| /nodes/0/title | Node 90 (PreviewImage) | "Preview Image1" | "Image Preview" | Allowed |
| /nodes/1/bgcolor | Node 91 (PreviewImage) | "#563453" | "#30343B" | Allowed |
| /nodes/1/color | Node 91 (PreviewImage) | "#6a4867" | "#594A72" | Allowed |
| /nodes/1/title | Node 91 (PreviewImage) | "Preview Image1" | "Image Preview" | Allowed |
| /nodes/2/bgcolor | Node 106 (PreviewImage) | "#563453" | "#30343B" | Allowed |
| /nodes/2/color | Node 106 (PreviewImage) | "#6a4867" | "#594A72" | Allowed |
| /nodes/2/title | Node 106 (PreviewImage) | "Preview Image1" | "Image Preview" | Allowed |
| /nodes/3/bgcolor | Node 105 (LoadImage) | "#63212b" | "#30343B" | Allowed |
| /nodes/3/color | Node 105 (LoadImage) | "#77353f" | "#235B74" | Allowed |
| /nodes/3/title | Node 105 (LoadImage) | (absent; ComfyUI default) | "Reference Image" | Allowed |
| /nodes/4/bgcolor | Node 89 (LoadImage) | "#63212b" | "#30343B" | Allowed |
| /nodes/4/color | Node 89 (LoadImage) | "#77353f" | "#235B74" | Allowed |
| /nodes/4/title | Node 89 (LoadImage) | (absent; ComfyUI default) | "Reference Image" | Allowed |
| /nodes/5/bgcolor | Node 14 (CLIPLoader) | "#533" | "#30343B" | Allowed |
| /nodes/5/color | Node 14 (CLIPLoader) | "#322" | "#35414A" | Allowed |
| /nodes/6/bgcolor | Node 30 (CLIPTextEncode) | "#353" | "#30343B" | Allowed |
| /nodes/6/color | Node 30 (CLIPTextEncode) | "#232" | "#35414A" | Allowed |
| /nodes/7/bgcolor | Node 51 (VAEDecode) | "#593930" | "#30343B" | Allowed |
| /nodes/7/color | Node 51 (VAEDecode) | "#332922" | "#35414A" | Allowed |
| /nodes/8/bgcolor | Node 23 (ConditioningZeroOut) | "#533" | "#30343B" | Allowed |
| /nodes/8/color | Node 23 (ConditioningZeroOut) | "#322" | "#35414A" | Allowed |
| /nodes/9/bgcolor | Node 129 (Fast Groups Bypasser (rgthree)) | "#535" | "#30343B" | Allowed |
| /nodes/9/color | Node 129 (Fast Groups Bypasser (rgthree)) | "#323" | "#715B2D" | Allowed |
| /nodes/10/bgcolor | Node 348 (CLIPTextEncode) | "#355" | "#30343B" | Allowed |
| /nodes/10/color | Node 348 (CLIPTextEncode) | "#233" | "#235B74" | Allowed |
| /nodes/10/title | Node 348 (CLIPTextEncode) | "Sam3.1 Prompt" | "SAM3.1 Prompt" | Allowed |
| /nodes/11/bgcolor | Node 350 (d0bfcf72-d3d6-47e9-96f6-c095e8337e04) | "#355" | "#30343B" | Allowed |
| /nodes/11/color | Node 350 (d0bfcf72-d3d6-47e9-96f6-c095e8337e04) | "#233" | "#35414A" | Allowed |
| /nodes/11/title | Node 350 (d0bfcf72-d3d6-47e9-96f6-c095e8337e04) | (absent; ComfyUI default) | "Prepare Reference Image 2" | Allowed |
| /nodes/12/bgcolor | Node 363 (4a60c427-b5f5-43b4-b88c-ffaf52e5d4b7) | "#355" | "#30343B" | Allowed |
| /nodes/12/color | Node 363 (4a60c427-b5f5-43b4-b88c-ffaf52e5d4b7) | "#233" | "#35414A" | Allowed |
| /nodes/12/title | Node 363 (4a60c427-b5f5-43b4-b88c-ffaf52e5d4b7) | (absent; ComfyUI default) | "Prepare Reference Image 3" | Allowed |
| /nodes/13/bgcolor | Node 88 (LoadImage) | "#63212b" | "#30343B" | Allowed |
| /nodes/13/color | Node 88 (LoadImage) | "#77353f" | "#235B74" | Allowed |
| /nodes/13/title | Node 88 (LoadImage) | (absent; ComfyUI default) | "Reference Image" | Allowed |
| /nodes/14/bgcolor | Node 337 (155b7e0c-d937-4dc5-80f7-2d111be5bec8) | "#355" | "#30343B" | Allowed |
| /nodes/14/color | Node 337 (155b7e0c-d937-4dc5-80f7-2d111be5bec8) | "#233" | "#35414A" | Allowed |
| /nodes/14/title | Node 337 (155b7e0c-d937-4dc5-80f7-2d111be5bec8) | (absent; ComfyUI default) | "Prepare Reference Image 1" | Allowed |
| /nodes/15/bgcolor | Node 115 (SaveImage) | "#535" | "#30343B" | Allowed |
| /nodes/15/color | Node 115 (SaveImage) | "#323" | "#2B644C" | Allowed |
| /nodes/15/title | Node 115 (SaveImage) | (absent; ComfyUI default) | "Save Image" | Allowed |
| /nodes/16/bgcolor | Node 359 (CLIPTextEncode) | "#355" | "#30343B" | Allowed |
| /nodes/16/color | Node 359 (CLIPTextEncode) | "#233" | "#235B74" | Allowed |
| /nodes/16/title | Node 359 (CLIPTextEncode) | "Sam3.1 Prompt" | "SAM3.1 Prompt" | Allowed |
| /nodes/17/bgcolor | Node 326 (CLIPTextEncode) | "#355" | "#30343B" | Allowed |
| /nodes/17/color | Node 326 (CLIPTextEncode) | "#233" | "#235B74" | Allowed |
| /nodes/17/title | Node 326 (CLIPTextEncode) | "Sam3.1 Prompt" | "SAM3.1 Prompt" | Allowed |
| /nodes/18/bgcolor | Node 113 (13e4920b-4673-409b-945e-ce27035af11b) | "#355" | "#30343B" | Allowed |
| /nodes/18/color | Node 113 (13e4920b-4673-409b-945e-ce27035af11b) | "#233" | "#715B2D" | Allowed |
| /nodes/18/title | Node 113 (13e4920b-4673-409b-945e-ce27035af11b) | (absent; ComfyUI default) | "Generate Image" | Allowed |
| /nodes/19/bgcolor | Node 325 (CheckpointLoaderSimple) | "#563453" | "#30343B" | Allowed |
| /nodes/19/color | Node 325 (CheckpointLoaderSimple) | "#6a4867" | "#35414A" | Allowed |
| /nodes/19/title | Node 325 (CheckpointLoaderSimple) | "Load Checkpoint (Sam3.1)" | "Load Checkpoint (SAM3.1)" | Allowed |
| /nodes/20/bgcolor | Node 87 (UNETLoader) | "#593930" | "#30343B" | Allowed |
| /nodes/20/color | Node 87 (UNETLoader) | "#332922" | "#35414A" | Allowed |
| /nodes/21/bgcolor | Node 21 (VAELoader) | "#533" | "#30343B" | Allowed |
| /nodes/21/color | Node 21 (VAELoader) | "#322" | "#35414A" | Allowed |
| /nodes/22/bgcolor | Node 364 (PrimitiveStringMultiline) | "#353" | "#30343B" | Allowed |
| /nodes/22/color | Node 364 (PrimitiveStringMultiline) | "#232" | "#235B74" | Allowed |
| /nodes/22/title | Node 364 (PrimitiveStringMultiline) | "Positive" | "Positive Prompt" | Allowed |
| /nodes/23 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 365, "type": "MarkdownNote", "pos": [-1100, 1740], "size": [480, 360], "flags": {}, "order": 23, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nUse reference images and a written prompt to generate a face or portrait.\n\n### How to Use\n\n1. Load pictures in the **Reference Image** cards. The **Img 1**, **Img 2**, and **Img 3** groups show which controls go with each image.\n2. In each **SAM3.1 Prompt**, name the region to isolate, such as “face.” Check the nearby **Image Preview** cards after running.\n3. Describe your portrait in the editable **Positive Prompt** box. Click **Run** and find the result under `ComfyUI/output/`."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 364 | 365 | Allowed |

## Klein Headswap.json

Result: **PASS** — 47 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Klein Headswap.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: 146.

Original SHA-256: `6231f05b25103c2be8df8c3c30624a716fae5f6c5e3220d50216f30269cd1fb8`

Modified SHA-256: `971940d90045373727674b765f49a373b222e9dd6b8cfb79d0b5f0c58c277604`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 2 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/0/title | Group 2 | "Step2 - Image size" | "Step 2 - Image Size" | Allowed |
| /definitions/subgraphs/0/groups/1/color | Group 3 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/title | Group 3 | "Step3 - Prompt" | "Step 3 - Prompt" | Allowed |
| /definitions/subgraphs/0/groups/2/color | Group 4 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/2/title | Group 4 | "Step1 - Load models" | "Step 1 - Load Models" | Allowed |
| /definitions/subgraphs/0/nodes/12/bgcolor | Node 48 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/12/color | Node 48 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/0/nodes/12/title | Node 48 (PreviewAny) | (absent; ComfyUI default) | "Prompt Preview" | Allowed |
| /definitions/subgraphs/1/groups/0/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/1/groups/1/color | Group 13 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/1/groups/2/color | Group 14 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/1/groups/3/color | Group 7 | "#3f789e" | "#235B74" | Allowed |
| /definitions/subgraphs/1/groups/3/title | Group 7 | "image 1" | "Image 1" | Allowed |
| /definitions/subgraphs/1/groups/4/color | Group 8 | "#3f789e" | "#235B74" | Allowed |
| /definitions/subgraphs/1/groups/4/title | Group 8 | "image 2" | "Image 2" | Allowed |
| /definitions/subgraphs/1/nodes/11/bgcolor | Node 74 (CLIPTextEncode) | "#353" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/11/color | Node 74 (CLIPTextEncode) | "#232" | "#35414A" | Allowed |
| /definitions/subgraphs/1/nodes/11/title | Node 74 (CLIPTextEncode) | "CLIP Text Encode (Positive Prompt)" | "Positive Prompt" | Allowed |
| /groups/0/color | Group 9 | "#A88" | "#35414A" | Allowed |
| /groups/0/title | Group 9 | "Head_Swap" | "Head Swap" | Allowed |
| /groups/1/color | Group 10 | "#b58b2a" | "#35414A" | Allowed |
| /groups/2/color | Group 11 | "#444" | "#594A72" | Allowed |
| /groups/2/title | Group 11 | "Labeled Compare" | "Image Comparison" | Allowed |
| /groups/3/color | Group 12 | "#8A8" | "#235B74" | Allowed |
| /nodes/0/bgcolor | Node 138 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/0/color | Node 138 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/0/title | Node 138 (LoadImage) | "BODY" | "Body" | Allowed |
| /nodes/1/bgcolor | Node 139 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/1/color | Node 139 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/2/bgcolor | Node 140 (PreviewImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 140 (PreviewImage) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/2/title | Node 140 (PreviewImage) | (absent; ComfyUI default) | "Image Preview" | Allowed |
| /nodes/3/bgcolor | Node 141 (a072ba04-bba1-4a9c-b6dc-285a8e887ec7) | "#355" | "#30343B" | Allowed |
| /nodes/3/color | Node 141 (a072ba04-bba1-4a9c-b6dc-285a8e887ec7) | "#233" | "#715B2D" | Allowed |
| /nodes/3/title | Node 141 (a072ba04-bba1-4a9c-b6dc-285a8e887ec7) | (absent; ComfyUI default) | "Z-Image Pass with LoRA" | Allowed |
| /nodes/4/bgcolor | Node 142 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/4/color | Node 142 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/4/title | Node 142 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "Image Comparison" | Allowed |
| /nodes/5/bgcolor | Node 143 (SaveImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/5/color | Node 143 (SaveImage) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/5/title | Node 143 (SaveImage) | (absent; ComfyUI default) | "Save Image" | Allowed |
| /nodes/6/bgcolor | Node 144 (37bc07bf-c5f1-4075-b843-984ec40ccc94) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/6/color | Node 144 (37bc07bf-c5f1-4075-b843-984ec40ccc94) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/6/title | Node 144 (37bc07bf-c5f1-4075-b843-984ec40ccc94) | (absent; ComfyUI default) | "Image Edit (FLUX.2 Klein 9B Distilled)" | Allowed |
| /nodes/7 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 146, "type": "MarkdownNote", "pos": [-640, 4560], "size": [480, 360], "flags": {}, "order": 7, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nPut the head from one image onto the body and composition of another.\n\n### How to Use\n\n1. Load the base image in **Body** and the head reference in **Head**.\n2. Describe the swap and what to preserve, such as the pose or lighting, in **Image Edit (FLUX.2 Klein 9B Distilled)**.\n3. Click **Run**. **Image Preview** shows the initial edit. **Save Image** writes the finished result to `ComfyUI/output/` after the Z-Image pass."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 145 | 146 | Allowed |

## Krea2 Turbo.json

Result: **PASS** — 42 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Krea2 Turbo.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: none.

Original SHA-256: `7e451144aadaa1952a28778f7b99f256f035881d94e84d470fafc85a80804332`

Modified SHA-256: `c8a023f987b36f29222a82acb0119bed925a3e685b9dbca472f516ff4800084c`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/nodes/0/bgcolor | Node 250 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/0/color | Node 250 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/0/nodes/0/title | Node 250 (PreviewAny) | (absent; ComfyUI default) | "Prompt Preview" | Allowed |
| /definitions/subgraphs/1/groups/0/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/1/groups/1/color | Group 5 | "#3f789e" | "#235B74" | Allowed |
| /definitions/subgraphs/1/groups/1/title | Group 5 | "Group" | "User Prompt" | Allowed |
| /definitions/subgraphs/1/groups/2/color | Group 6 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/1/groups/3/color | Group 7 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/1/groups/4/color | Group 8 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/1/groups/5/color | Group 9 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/1/nodes/4/bgcolor | Node 346 (PrimitiveStringMultiline) | "#533" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/4/color | Node 346 (PrimitiveStringMultiline) | "#322" | "#235B74" | Allowed |
| /definitions/subgraphs/1/nodes/5/bgcolor | Node 347 (CLIPTextEncode) | "#353" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/5/color | Node 347 (CLIPTextEncode) | "#232" | "#35414A" | Allowed |
| /definitions/subgraphs/1/nodes/8/bgcolor | Node 350 (PrimitiveBoolean) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/8/color | Node 350 (PrimitiveBoolean) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/1/nodes/8/title | Node 350 (PrimitiveBoolean) | "Boolean (Enable LoRA?)" | "Use LoRA" | Allowed |
| /groups/0/color | Group 11 | "#3f789e" | "#35414A" | Allowed |
| /groups/0/title | Group 11 | "Post" | "Image Finishing" | Allowed |
| /nodes/0/bgcolor | Node 48 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /nodes/0/color | Node 48 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /nodes/0/title | Node 48 (MarkdownNote) | "Model Links" | "Model Files and Setup" | Allowed |
| /nodes/4/bgcolor | Node 50 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /nodes/4/color | Node 50 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /nodes/4/title | Node 50 (MarkdownNote) | "Note: Krea-2" | "Quick Start" | Allowed |
| /nodes/4/widgets_values/0 | Note 50 | "This workflow generates images with **Krea-2 Turbo**, a fast distilled text-to-image model. The workflow is organized into a few parts: each handles a different step so you can generate quickly without digging through every node.\n\n## Text to Image (Krea-2 Turbo) Subgraph\n\nDouble-click this node to open the full pipeline. Inside, the canvas is grouped into several areas:\n\n**Models**: Loads the diffusion model, text encoder, VAE, and optional style LoRA (`LoraLoaderModelOnly`).\n\n**Prompt**: Enter your image description in **Text String (User Prompt)**.\n\n**Prompt Enhancement**: Expands your prompt before generation. Enabled by default (`prompt_enhance`). You can turn it off to use your prompt as-is, or replace the built-in module with **OpenAI** or **Gemini** API nodes.\n\n**Feature Switch**: Quick toggles on the left side of the subgraph:\n- `prompt_enhance`: enable or disable prompt expansion\n- `enable_lora?`: enable or disable the style LoRA\n\n**Image Generation**: Handles latent sizing, sampling (8 steps), and VAE decode to produce the final image.\n\nWhen using a LoRA, set `enable_lora?` to true, select the matching file in **LoraLoaderModelOnly**, and adjust `lora_strength` as needed.\n\n## LoRA & Trigger Word (CustomCombo)\n\nOn the main canvas, the **CustomCombo** node is where you choose which style LoRA you are using (e.g. `krea2_coolblue`, `krea2_darkbrush`). The workflow uses your selection to automatically append the correct **trigger word** to your prompt.\n\n- Download LoRA files from [Comfy-Org/Krea-2/loras](https://huggingface.co/Comfy-Org/Krea-2/tree/main/loras) and place them in `ComfyUI/models/loras/`\n- Select the LoRA name that matches the file loaded inside the subgraph\n- The trigger word is applied for you: no need to type it manually\n- For trigger words and recommended strength values, see the **LoRA Trigger Words and Settings** note beside this workflow\n" | "### What It Does\n\nTurn a written description into an image, with optional style and finishing controls.\n\n### How to Use\n\n1. Start Ollama and enter your description in **Enhance Prompt (Krea-2)**. **Prompt Preview** shows the expanded wording after you run.\n2. Choose the shape and size in **Image Size (Ratio and Megapixels)**. To use a style add-on (LoRA), check **enable_lora?**, **lora_name**, and **lora_strength** in **Text to Image (Krea-2 Turbo)**.\n3. Click **Run**. **Save Image** writes `Krea2_turbo` files under `ComfyUI/output/`.\n\n### Model Setup and Style Options\n\n- See **Model Files and Setup** for the diffusion model, text encoder, and image decoder. Open **Text to Image (Krea-2 Turbo)** to inspect the model loaders and sampling controls.\n- Put optional [Krea-2 LoRA files](https://huggingface.co/Comfy-Org/Krea-2/tree/main/loras) in `ComfyUI/models/loras/`. Select the matching file and start with the saved strength.\n- The saved canvas sends the Ollama result to the generator. **Text String (User Prompt)** is inside the generation node. Use **Enhance Prompt (Krea-2)** on the main canvas for the saved setup.\n- Some Krea-2 presets use trigger words such as `krea2_coolblue` and `krea2_darkbrush`. Follow the instructions for the selected LoRA. A **CustomCombo** preset can append a trigger word when that setup is present." | Allowed |
| /nodes/4/widgets_values_named/text | Note 50 | "This workflow generates images with **Krea-2 Turbo**, a fast distilled text-to-image model. The workflow is organized into a few parts: each handles a different step so you can generate quickly without digging through every node.\n\n## Text to Image (Krea-2 Turbo) Subgraph\n\nDouble-click this node to open the full pipeline. Inside, the canvas is grouped into several areas:\n\n**Models**: Loads the diffusion model, text encoder, VAE, and optional style LoRA (`LoraLoaderModelOnly`).\n\n**Prompt**: Enter your image description in **Text String (User Prompt)**.\n\n**Prompt Enhancement**: Expands your prompt before generation. Enabled by default (`prompt_enhance`). You can turn it off to use your prompt as-is, or replace the built-in module with **OpenAI** or **Gemini** API nodes.\n\n**Feature Switch**: Quick toggles on the left side of the subgraph:\n- `prompt_enhance`: enable or disable prompt expansion\n- `enable_lora?`: enable or disable the style LoRA\n\n**Image Generation**: Handles latent sizing, sampling (8 steps), and VAE decode to produce the final image.\n\nWhen using a LoRA, set `enable_lora?` to true, select the matching file in **LoraLoaderModelOnly**, and adjust `lora_strength` as needed.\n\n## LoRA & Trigger Word (CustomCombo)\n\nOn the main canvas, the **CustomCombo** node is where you choose which style LoRA you are using (e.g. `krea2_coolblue`, `krea2_darkbrush`). The workflow uses your selection to automatically append the correct **trigger word** to your prompt.\n\n- Download LoRA files from [Comfy-Org/Krea-2/loras](https://huggingface.co/Comfy-Org/Krea-2/tree/main/loras) and place them in `ComfyUI/models/loras/`\n- Select the LoRA name that matches the file loaded inside the subgraph\n- The trigger word is applied for you: no need to type it manually\n- For trigger words and recommended strength values, see the **LoRA Trigger Words and Settings** note beside this workflow\n" | "### What It Does\n\nTurn a written description into an image, with optional style and finishing controls.\n\n### How to Use\n\n1. Start Ollama and enter your description in **Enhance Prompt (Krea-2)**. **Prompt Preview** shows the expanded wording after you run.\n2. Choose the shape and size in **Image Size (Ratio and Megapixels)**. To use a style add-on (LoRA), check **enable_lora?**, **lora_name**, and **lora_strength** in **Text to Image (Krea-2 Turbo)**.\n3. Click **Run**. **Save Image** writes `Krea2_turbo` files under `ComfyUI/output/`.\n\n### Model Setup and Style Options\n\n- See **Model Files and Setup** for the diffusion model, text encoder, and image decoder. Open **Text to Image (Krea-2 Turbo)** to inspect the model loaders and sampling controls.\n- Put optional [Krea-2 LoRA files](https://huggingface.co/Comfy-Org/Krea-2/tree/main/loras) in `ComfyUI/models/loras/`. Select the matching file and start with the saved strength.\n- The saved canvas sends the Ollama result to the generator. **Text String (User Prompt)** is inside the generation node. Use **Enhance Prompt (Krea-2)** on the main canvas for the saved setup.\n- Some Krea-2 presets use trigger words such as `krea2_coolblue` and `krea2_darkbrush`. Follow the instructions for the selected LoRA. A **CustomCombo** preset can append a trigger word when that setup is present." | Allowed |
| /nodes/6/bgcolor | Node 254 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/6/color | Node 254 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/6/title | Node 254 (PreviewAny) | (absent; ComfyUI default) | "Prompt Preview" | Allowed |
| /nodes/7/bgcolor | Node 29 (SaveImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/7/color | Node 29 (SaveImage) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/7/title | Node 29 (SaveImage) | (absent; ComfyUI default) | "Save Image" | Allowed |
| /nodes/9/bgcolor | Node 49 (ResolutionSelector) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/9/color | Node 49 (ResolutionSelector) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/9/title | Node 49 (ResolutionSelector) | (absent; ComfyUI default) | "Image Size (Ratio and Megapixels)" | Allowed |
| /nodes/10/bgcolor | Node 353 (47d96fb0-2522-425b-921a-b1e083833251) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/10/color | Node 353 (47d96fb0-2522-425b-921a-b1e083833251) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/10/title | Node 353 (47d96fb0-2522-425b-921a-b1e083833251) | (absent; ComfyUI default) | "Text to Image (Krea-2 Turbo)" | Allowed |
| /nodes/11/bgcolor | Node 253 (5dfe8fc1-c57e-4768-9d8a-018efd863913) | "#653" | "#30343B" | Allowed |
| /nodes/11/color | Node 253 (5dfe8fc1-c57e-4768-9d8a-018efd863913) | "#432" | "#715B2D" | Allowed |
| /nodes/11/title | Node 253 (5dfe8fc1-c57e-4768-9d8a-018efd863913) | (absent; ComfyUI default) | "Enhance Prompt (Krea-2)" | Allowed |

## LTX Video 2.5 FLF2V.json

Result: **PASS** — 53 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:LTX Video 2.5 FLF2V.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: none.

Original SHA-256: `63406cee33dca25844ba529acc8e5d520bdb9ccdb8f8d31e7c48e03ff5393246`

Modified SHA-256: `90193b0738dd6e7e478278948ff23d22624210a24c759174a93dc7cb3b04376e`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 7 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/color | Group 8 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/2/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/3/color | Group 6 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/4/color | Group 3 | "#b06634" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/4/title | Group 3 | "FIrst Frame" | "First Frame" | Allowed |
| /definitions/subgraphs/0/groups/5/color | Group 4 | "#b06634" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/6/color | Group 2 | "#8A8" | "#D2B16F" | Allowed |
| /definitions/subgraphs/0/groups/7/color | Group 5 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/8/color | Group 9 | (absent; ComfyUI default) | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/16/bgcolor | Node 217 (CLIPTextEncode) | "#535" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/16/color | Node 217 (CLIPTextEncode) | "#323" | "#235B74" | Allowed |
| /definitions/subgraphs/0/nodes/17/bgcolor | Node 222 (CLIPTextEncode) | "#353" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/17/color | Node 222 (CLIPTextEncode) | "#232" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/25/bgcolor | Node 249 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/25/color | Node 249 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/0/nodes/25/title | Node 249 (PreviewAny) | (absent; ComfyUI default) | "Prompt Preview" | Allowed |
| /definitions/subgraphs/0/nodes/31/bgcolor | Node 250 (PrimitiveBoolean) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/31/color | Node 250 (PrimitiveBoolean) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/31/title | Node 250 (PrimitiveBoolean) | "Boolean (Enable Prompt Enhance)" | "Use Prompt Enhancement" | Allowed |
| /definitions/subgraphs/0/nodes/32/bgcolor | Node 215 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/32/color | Node 215 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/32/title | Node 215 (PrimitiveInt) | "Width" | "Width (Pixels)" | Allowed |
| /definitions/subgraphs/0/nodes/33/bgcolor | Node 216 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/33/color | Node 216 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/33/title | Node 216 (PrimitiveInt) | "height" | "Height (Pixels)" | Allowed |
| /definitions/subgraphs/0/nodes/35/bgcolor | Node 198 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/35/color | Node 198 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/35/title | Node 198 (PrimitiveInt) | "Duration" | "Duration (Seconds)" | Allowed |
| /definitions/subgraphs/0/nodes/37/bgcolor | Node 205 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/37/color | Node 205 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/37/title | Node 205 (PrimitiveInt) | "Frame Rate(int)" | "Frame Rate (FPS)" | Allowed |
| /definitions/subgraphs/0/nodes/38/bgcolor | Node 252 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/38/color | Node 252 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /groups/0/color | Group 10 | "#3f789e" | "#35414A" | Allowed |
| /nodes/0/bgcolor | Node 39 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/0/color | Node 39 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/1/bgcolor | Node 68 (SaveVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/1/color | Node 68 (SaveVideo) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/1/title | Node 68 (SaveVideo) | (absent; ComfyUI default) | "Save Video" | Allowed |
| /nodes/2/bgcolor | Node 254 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /nodes/2/color | Node 254 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /nodes/2/title | Node 254 (MarkdownNote) | "Note: About LTX-2.5" | "Quick Start" | Allowed |
| /nodes/2/widgets_values/0 | Note 254 | "# LTX-2.5\n\nLTX-2.5 is Lightricks' open video generation model : fast, local-first, and built for production. Run it locally, fine-tune it for your own use case, or integrate it into your pipeline.\n\n**Key highlights:**\n\n- **Pixel Diffusion** : keyframes-first generation that builds every scene on a grid of high-fidelity keyframes for industry-leading pixel quality\n- **Diffusion Video Decoder** : sharper faces, legible text, fewer smears in fast motion\n- **Native multishot** : one generation yields multiple connected shots holding character, environment, lighting, voice, and style across cuts\n- **Custom Gemma 4 12B text encoder** : retains multiple subjects, actions, lighting, detail, and camera direction across complex prompts\n- **Dedicated Prompt Enhancer** : a lightweight model that expands short prompts into rich cinematic instructions at near-zero extra compute\n- **Auto Duration** : predicts the right clip length from the described action before diffusion begins\n- **Better distilled model** : carries far more quality, prompt adherence, and motion into a smaller, faster variant\n- Carried over from LTX-2.3: native 4K, synchronized audio-video\n\nOfficial model & files: https://huggingface.co/Lightricks/LTX-2.5\n## What this workflow does\n\nThis **First & Last Frame** workflow interpolates between two images. Load a first and a last frame, and the model generates the connected shots in between : holding character, environment, lighting, and style across the transition, with synchronized audio.\n\n## Subgraph parameters\n\nThe **First & Last Frame to Video (LTX-2.5)** node is a subgraph. Click the **Enter subgraph** button at the bottom of the node to open its internal graph, where you can inspect and fine-tune every step of the pipeline (conditioning, sampler, CFG guider, VAE decode, and more).\n\n\| Parameter \| What it does \|\n\|---\|---\|\n\| first_frame \| Starting image of the transition (load your own image in **Load First Frame**) \|\n\| last_frame \| Ending image of the transition (load your own image in **Load Last Frame**) \|\n\| prompt \| Text prompt describing the motion, scene, lighting, camera, and style \|\n\| prompt_enhance \| Toggle the built-in Prompt Enhancer: expands short prompts into rich cinematic instructions at near-zero extra compute \|\n\| duration \| Clip length in seconds (Auto Duration can predict it from the action) \|\n\| width / height \| Output resolution in pixels (e.g. 1280×720) \|\n\| seed \| Random seed : set a fixed value to reproduce the same result \|\n\| frame_rate \| Frames per second \|\n\| unet_name \| Main model: LTX-2.5 distilled transformer (ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors) \|\n\| video_vae \| Video VAE used for decoding (ltx-2.5-video-vae-bf16.safetensors) \|\n\| audio_vae \| Audio VAE that produces synchronized audio (ltx-2.5-audio-vae-bf16.safetensors) \|\n\| clip_name \| Text encoder: custom Gemma 4 12B with projection (gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors) \|\n\| prompt_enhance_model \| Model checkpoint used by the Prompt Enhancer \|\n\n## How to use\n\n1. Download the models listed in **Note: Model Links** and place them in ComfyUI's `models/` folder\n2. Replace the images in **Load First Frame** and **Load Last Frame** with your own start/end frames\n3. Write a prompt describing the transition, optionally toggle **prompt_enhance** for short prompts\n4. Set **duration** / **width** / **height** / **frame_rate** (defaults work well) and hit **Queue**\n5. To dive deeper, click **Enter subgraph** at the bottom of the main node : every internal step (conditioning, sampler, CFG, VAE decode) can be edited there\n" | "### What It Does\n\nGenerate the motion and sound that connect a starting image to an ending image.\n\n### How to Use\n\n1. Replace the images in **Load First Frame** and **Load Last Frame**.\n2. In **First & Last Frame to Video (LTX-2.5)**, describe the transition, set **duration** in seconds, and choose the frame rate. The saved setup takes its size from the resized first frame.\n3. Click **Run**. **Save Video** writes `ltx2.5_flf2v` files under `ComfyUI/output/video/`.\n\n### Setup and Reference\n\nInstall the [LTX-2.5 model files](https://huggingface.co/Lightricks/LTX-2.5) in ComfyUI’s `models/` folder. See the repository README for the file list and folders. Use **Enter subgraph** to inspect advanced controls.\n\n\| Parameter \| What it does \|\n\|---\|---\|\n\| first_frame \| Starting image of the transition (load your own image in **Load First Frame**) \|\n\| last_frame \| Ending image of the transition (load your own image in **Load Last Frame**) \|\n\| prompt \| Text prompt describing the motion, scene, lighting, camera, and style \|\n\| prompt_enhance \| Expand a short prompt before generation \|\n\| duration \| Clip length in seconds \|\n\| width / height \| Output resolution in pixels (e.g. 1280×720) \|\n\| seed \| Random seed : set a fixed value to reproduce the same result \|\n\| frame_rate \| Frames per second \|\n\| unet_name \| Main model: LTX-2.5 distilled transformer (ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors) \|\n\| video_vae \| Video VAE used for decoding (ltx-2.5-video-vae-bf16.safetensors) \|\n\| audio_vae \| Audio VAE that produces synchronized audio (ltx-2.5-audio-vae-bf16.safetensors) \|\n\| clip_name \| Text encoder: custom Gemma 4 12B with projection (gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors) \|\n\| prompt_enhance_model \| Model checkpoint used by the Prompt Enhancer \|" | Allowed |
| /nodes/2/widgets_values_named/text | Note 254 | "# LTX-2.5\n\nLTX-2.5 is Lightricks' open video generation model : fast, local-first, and built for production. Run it locally, fine-tune it for your own use case, or integrate it into your pipeline.\n\n**Key highlights:**\n\n- **Pixel Diffusion** : keyframes-first generation that builds every scene on a grid of high-fidelity keyframes for industry-leading pixel quality\n- **Diffusion Video Decoder** : sharper faces, legible text, fewer smears in fast motion\n- **Native multishot** : one generation yields multiple connected shots holding character, environment, lighting, voice, and style across cuts\n- **Custom Gemma 4 12B text encoder** : retains multiple subjects, actions, lighting, detail, and camera direction across complex prompts\n- **Dedicated Prompt Enhancer** : a lightweight model that expands short prompts into rich cinematic instructions at near-zero extra compute\n- **Auto Duration** : predicts the right clip length from the described action before diffusion begins\n- **Better distilled model** : carries far more quality, prompt adherence, and motion into a smaller, faster variant\n- Carried over from LTX-2.3: native 4K, synchronized audio-video\n\nOfficial model & files: https://huggingface.co/Lightricks/LTX-2.5\n## What this workflow does\n\nThis **First & Last Frame** workflow interpolates between two images. Load a first and a last frame, and the model generates the connected shots in between : holding character, environment, lighting, and style across the transition, with synchronized audio.\n\n## Subgraph parameters\n\nThe **First & Last Frame to Video (LTX-2.5)** node is a subgraph. Click the **Enter subgraph** button at the bottom of the node to open its internal graph, where you can inspect and fine-tune every step of the pipeline (conditioning, sampler, CFG guider, VAE decode, and more).\n\n\| Parameter \| What it does \|\n\|---\|---\|\n\| first_frame \| Starting image of the transition (load your own image in **Load First Frame**) \|\n\| last_frame \| Ending image of the transition (load your own image in **Load Last Frame**) \|\n\| prompt \| Text prompt describing the motion, scene, lighting, camera, and style \|\n\| prompt_enhance \| Toggle the built-in Prompt Enhancer: expands short prompts into rich cinematic instructions at near-zero extra compute \|\n\| duration \| Clip length in seconds (Auto Duration can predict it from the action) \|\n\| width / height \| Output resolution in pixels (e.g. 1280×720) \|\n\| seed \| Random seed : set a fixed value to reproduce the same result \|\n\| frame_rate \| Frames per second \|\n\| unet_name \| Main model: LTX-2.5 distilled transformer (ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors) \|\n\| video_vae \| Video VAE used for decoding (ltx-2.5-video-vae-bf16.safetensors) \|\n\| audio_vae \| Audio VAE that produces synchronized audio (ltx-2.5-audio-vae-bf16.safetensors) \|\n\| clip_name \| Text encoder: custom Gemma 4 12B with projection (gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors) \|\n\| prompt_enhance_model \| Model checkpoint used by the Prompt Enhancer \|\n\n## How to use\n\n1. Download the models listed in **Note: Model Links** and place them in ComfyUI's `models/` folder\n2. Replace the images in **Load First Frame** and **Load Last Frame** with your own start/end frames\n3. Write a prompt describing the transition, optionally toggle **prompt_enhance** for short prompts\n4. Set **duration** / **width** / **height** / **frame_rate** (defaults work well) and hit **Queue**\n5. To dive deeper, click **Enter subgraph** at the bottom of the main node : every internal step (conditioning, sampler, CFG, VAE decode) can be edited there\n" | "### What It Does\n\nGenerate the motion and sound that connect a starting image to an ending image.\n\n### How to Use\n\n1. Replace the images in **Load First Frame** and **Load Last Frame**.\n2. In **First & Last Frame to Video (LTX-2.5)**, describe the transition, set **duration** in seconds, and choose the frame rate. The saved setup takes its size from the resized first frame.\n3. Click **Run**. **Save Video** writes `ltx2.5_flf2v` files under `ComfyUI/output/video/`.\n\n### Setup and Reference\n\nInstall the [LTX-2.5 model files](https://huggingface.co/Lightricks/LTX-2.5) in ComfyUI’s `models/` folder. See the repository README for the file list and folders. Use **Enter subgraph** to inspect advanced controls.\n\n\| Parameter \| What it does \|\n\|---\|---\|\n\| first_frame \| Starting image of the transition (load your own image in **Load First Frame**) \|\n\| last_frame \| Ending image of the transition (load your own image in **Load Last Frame**) \|\n\| prompt \| Text prompt describing the motion, scene, lighting, camera, and style \|\n\| prompt_enhance \| Expand a short prompt before generation \|\n\| duration \| Clip length in seconds \|\n\| width / height \| Output resolution in pixels (e.g. 1280×720) \|\n\| seed \| Random seed : set a fixed value to reproduce the same result \|\n\| frame_rate \| Frames per second \|\n\| unet_name \| Main model: LTX-2.5 distilled transformer (ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors) \|\n\| video_vae \| Video VAE used for decoding (ltx-2.5-video-vae-bf16.safetensors) \|\n\| audio_vae \| Audio VAE that produces synchronized audio (ltx-2.5-audio-vae-bf16.safetensors) \|\n\| clip_name \| Text encoder: custom Gemma 4 12B with projection (gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors) \|\n\| prompt_enhance_model \| Model checkpoint used by the Prompt Enhancer \|" | Allowed |
| /nodes/4/bgcolor | Node 261 (ResolutionSelector) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/4/color | Node 261 (ResolutionSelector) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/4/title | Node 261 (ResolutionSelector) | (absent; ComfyUI default) | "Image Size (Ratio and Megapixels)" | Allowed |
| /nodes/5/bgcolor | Node 31 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/5/color | Node 31 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/7/bgcolor | Node 251 (cf70afc4-5a03-47ce-8210-734b1de6c6bc) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/7/color | Node 251 (cf70afc4-5a03-47ce-8210-734b1de6c6bc) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/7/title | Node 251 (cf70afc4-5a03-47ce-8210-734b1de6c6bc) | (absent; ComfyUI default) | "First & Last Frame to Video (LTX-2.5)" | Allowed |

## LTX Video 2.5 I2V.json

Result: **PASS** — 60 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:LTX Video 2.5 I2V.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: none.

Original SHA-256: `b091002c9b862ab8d49c6ca125efdaa6d2252c4debee2dbcc2743661c906dc0e`

Modified SHA-256: `bdd4f7fa59b0641a23684f48a8e4aa893b499c5ef4a73333fe703504bf0c2190`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 27 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/2/color | Group 3 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/3/color | Group 19 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/0/groups/4/color | Group 2 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/5/color | Group 7 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/6/color | Group 20 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/7/color | Group 21 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/8/color | Group 22 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/8/title | Group 22 | "Number conversion" | "Number Conversion" | Allowed |
| /definitions/subgraphs/0/groups/9/color | Group 6 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/2/bgcolor | Node 383 (PrimitiveBoolean) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/2/color | Node 383 (PrimitiveBoolean) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/2/title | Node 383 (PrimitiveBoolean) | "Boolean (Enable Prompt Enhance)" | "Use Prompt Enhancement" | Allowed |
| /definitions/subgraphs/0/nodes/3/bgcolor | Node 364 (CLIPTextEncode) | "#353" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/3/color | Node 364 (CLIPTextEncode) | "#232" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/4/bgcolor | Node 376 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/4/color | Node 376 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /definitions/subgraphs/0/nodes/7/bgcolor | Node 381 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/7/color | Node 381 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/0/nodes/7/title | Node 381 (PreviewAny) | (absent; ComfyUI default) | "Prompt Preview" | Allowed |
| /definitions/subgraphs/0/nodes/8/bgcolor | Node 362 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/8/color | Node 362 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/8/title | Node 362 (PrimitiveInt) | "Duration" | "Duration (Seconds)" | Allowed |
| /definitions/subgraphs/0/nodes/9/bgcolor | Node 363 (PrimitiveBoolean) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/9/color | Node 363 (PrimitiveBoolean) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/13/bgcolor | Node 372 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/13/color | Node 372 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/13/title | Node 372 (PrimitiveInt) | "Width" | "Width (Pixels)" | Allowed |
| /definitions/subgraphs/0/nodes/14/bgcolor | Node 373 (CLIPTextEncode) | "#535" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/14/color | Node 373 (CLIPTextEncode) | "#323" | "#235B74" | Allowed |
| /definitions/subgraphs/0/nodes/16/bgcolor | Node 360 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/16/color | Node 360 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/16/title | Node 360 (PrimitiveInt) | "Height" | "Height (Pixels)" | Allowed |
| /definitions/subgraphs/0/nodes/46/bgcolor | Node 361 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/46/color | Node 361 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/46/title | Node 361 (PrimitiveInt) | "Frame Rate" | "Frame Rate (FPS)" | Allowed |
| /definitions/subgraphs/0/nodes/49/title | Node 411 (ComfySwitchNode) | "RTX Switch" | "Use RTX Upscaling" | Allowed |
| /definitions/subgraphs/1/nodes/2/title | Node 4 (ComfyMathExpression) | "Duration (frames / fps)" | "Video Duration (Seconds)" | Allowed |
| /definitions/subgraphs/1/nodes/3/title | Node 5 (StringFormat) | "Video metadata summary" | "Video Details Summary" | Allowed |
| /groups/0/color | Group 29 | "#3f789e" | "#35414A" | Allowed |
| /nodes/0/bgcolor | Node 75 (SaveVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/0/color | Node 75 (SaveVideo) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/0/title | Node 75 (SaveVideo) | (absent; ComfyUI default) | "Save Video" | Allowed |
| /nodes/3/bgcolor | Node 395 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/3/color | Node 395 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/4/bgcolor | Node 408 (ResolutionSelector) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/4/color | Node 408 (ResolutionSelector) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/4/title | Node 408 (ResolutionSelector) | (absent; ComfyUI default) | "Image Size (Ratio and Megapixels)" | Allowed |
| /nodes/5/bgcolor | Node 399 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /nodes/5/color | Node 399 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /nodes/5/title | Node 399 (MarkdownNote) | "Note: About LTX-2.5" | "Quick Start" | Allowed |
| /nodes/5/widgets_values/0 | Note 399 | "# LTX-2.5\n\nLTX-2.5 is Lightricks' open video generation model : fast, local-first, and built for production. Run it locally, fine-tune it for your own use case, or integrate it into your pipeline.\n\n**Key highlights:**\n\n- **Pixel Diffusion** : keyframes-first generation that builds every scene on a grid of high-fidelity keyframes for industry-leading pixel quality\n- **Diffusion Video Decoder** : sharper faces, legible text, fewer smears in fast motion\n- **Native multishot** : one generation yields multiple connected shots holding character, environment, lighting, voice, and style across cuts\n- **Custom Gemma 4 12B text encoder** : retains multiple subjects, actions, lighting, detail, and camera direction across complex prompts\n- **Dedicated Prompt Enhancer** : a lightweight model that expands short prompts into rich cinematic instructions at near-zero extra compute\n- **Auto Duration** : predicts the right clip length from the described action before diffusion begins\n- **Better distilled model** : carries far more quality, prompt adherence, and motion into a smaller, faster variant\n- Carried over from LTX-2.3: native 4K, synchronized audio-video\n\nOfficial model & files: https://huggingface.co/Lightricks/LTX-2.5\n## What this workflow does\n\nThis **Image-to-Video** workflow animates a first frame into a video. Load a starting image, describe the motion in the prompt, and the model continues the scene while holding character, lighting, and style : with synchronized audio.\n\n## Subgraph parameters\n\nThe **Image to Video (LTX-2.5)** node is a subgraph. Click the **Enter subgraph** button at the bottom of the node to open its internal graph, where you can inspect and fine-tune every step of the pipeline (conditioning, sampler, CFG guider, VAE decode, and more).\n\n\| Parameter \| What it does \|\n\|---\|---\|\n\| first_frame \| Starting image that the video continues from (load your own image in **Load First Frame**) \|\n\| prompt \| Text prompt describing the motion, scene, lighting, camera, and style \|\n\| prompt_enhance \| Toggle the built-in Prompt Enhancer: expands short prompts into rich cinematic instructions at near-zero extra compute \|\n\| duration \| Clip length in seconds (Auto Duration can predict it from the action) \|\n\| width / height \| Output resolution in pixels (e.g. 1280×720) \|\n\| seed \| Random seed : set a fixed value to reproduce the same result \|\n\| frame_rate \| Frames per second \|\n\| unet_name \| Main model: LTX-2.5 distilled transformer (ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors) \|\n\| video_vae \| Video VAE used for decoding (ltx-2.5-video-vae-bf16.safetensors) \|\n\| audio_vae \| Audio VAE that produces synchronized audio (ltx-2.5-audio-vae-bf16.safetensors) \|\n\| clip_name \| Text encoder: custom Gemma 4 12B with projection (gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors) \|\n\| upscale_model \| Latent upscaler applied before decoding for higher-fidelity output \|\n\| prompt_enhance_model \| Model checkpoint used by the Prompt Enhancer \|\n\n## How to use\n\n1. Download the models listed in **Note: Model Links** and place them in ComfyUI's `models/` folder\n2. Replace the image in **Load First Frame** with your own starting frame\n3. Write a prompt describing the motion, optionally toggle **prompt_enhance** for short prompts\n4. Set **duration** / **width** / **height** / **frame_rate** (defaults work well) and hit **Queue**\n5. To dive deeper, click **Enter subgraph** at the bottom of the main node : every internal step (conditioning, sampler, CFG, VAE decode) can be edited there\n" | "### What It Does\n\nAnimate a starting image into a video with sound.\n\n### How to Use\n\n1. Replace the image in **Load First Frame**.\n2. In **Image to Video (LTX-2.5)**, describe the movement and sound. Set **duration** in seconds and choose the frame rate. The saved setup takes its size from the resized image.\n3. Click **Run**. Check **Video Details** and look for `LTX-2.5_i2v` files under `ComfyUI/output/video/`.\n\n### Setup and Reference\n\nInstall the [LTX-2.5 model files](https://huggingface.co/Lightricks/LTX-2.5) in ComfyUI’s `models/` folder. See the repository README for the file list and folders. Use **Enter subgraph** to inspect advanced controls.\n\n\| Parameter \| What it does \|\n\|---\|---\|\n\| first_frame \| Starting image that the video continues from (load your own image in **Load First Frame**) \|\n\| prompt \| Text prompt describing the motion, scene, lighting, camera, and style \|\n\| prompt_enhance \| Expand a short prompt before generation \|\n\| duration \| Clip length in seconds \|\n\| width / height \| Output resolution in pixels (e.g. 1280×720) \|\n\| seed \| Random seed : set a fixed value to reproduce the same result \|\n\| frame_rate \| Frames per second \|\n\| unet_name \| Main model: LTX-2.5 distilled transformer (ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors) \|\n\| video_vae \| Video VAE used for decoding (ltx-2.5-video-vae-bf16.safetensors) \|\n\| audio_vae \| Audio VAE that produces synchronized audio (ltx-2.5-audio-vae-bf16.safetensors) \|\n\| clip_name \| Text encoder: custom Gemma 4 12B with projection (gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors) \|\n\| upscale_model \| Latent upscaler applied before decoding for higher-fidelity output \|\n\| prompt_enhance_model \| Model checkpoint used by the Prompt Enhancer \|" | Allowed |
| /nodes/5/widgets_values_named/text | Note 399 | "# LTX-2.5\n\nLTX-2.5 is Lightricks' open video generation model : fast, local-first, and built for production. Run it locally, fine-tune it for your own use case, or integrate it into your pipeline.\n\n**Key highlights:**\n\n- **Pixel Diffusion** : keyframes-first generation that builds every scene on a grid of high-fidelity keyframes for industry-leading pixel quality\n- **Diffusion Video Decoder** : sharper faces, legible text, fewer smears in fast motion\n- **Native multishot** : one generation yields multiple connected shots holding character, environment, lighting, voice, and style across cuts\n- **Custom Gemma 4 12B text encoder** : retains multiple subjects, actions, lighting, detail, and camera direction across complex prompts\n- **Dedicated Prompt Enhancer** : a lightweight model that expands short prompts into rich cinematic instructions at near-zero extra compute\n- **Auto Duration** : predicts the right clip length from the described action before diffusion begins\n- **Better distilled model** : carries far more quality, prompt adherence, and motion into a smaller, faster variant\n- Carried over from LTX-2.3: native 4K, synchronized audio-video\n\nOfficial model & files: https://huggingface.co/Lightricks/LTX-2.5\n## What this workflow does\n\nThis **Image-to-Video** workflow animates a first frame into a video. Load a starting image, describe the motion in the prompt, and the model continues the scene while holding character, lighting, and style : with synchronized audio.\n\n## Subgraph parameters\n\nThe **Image to Video (LTX-2.5)** node is a subgraph. Click the **Enter subgraph** button at the bottom of the node to open its internal graph, where you can inspect and fine-tune every step of the pipeline (conditioning, sampler, CFG guider, VAE decode, and more).\n\n\| Parameter \| What it does \|\n\|---\|---\|\n\| first_frame \| Starting image that the video continues from (load your own image in **Load First Frame**) \|\n\| prompt \| Text prompt describing the motion, scene, lighting, camera, and style \|\n\| prompt_enhance \| Toggle the built-in Prompt Enhancer: expands short prompts into rich cinematic instructions at near-zero extra compute \|\n\| duration \| Clip length in seconds (Auto Duration can predict it from the action) \|\n\| width / height \| Output resolution in pixels (e.g. 1280×720) \|\n\| seed \| Random seed : set a fixed value to reproduce the same result \|\n\| frame_rate \| Frames per second \|\n\| unet_name \| Main model: LTX-2.5 distilled transformer (ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors) \|\n\| video_vae \| Video VAE used for decoding (ltx-2.5-video-vae-bf16.safetensors) \|\n\| audio_vae \| Audio VAE that produces synchronized audio (ltx-2.5-audio-vae-bf16.safetensors) \|\n\| clip_name \| Text encoder: custom Gemma 4 12B with projection (gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors) \|\n\| upscale_model \| Latent upscaler applied before decoding for higher-fidelity output \|\n\| prompt_enhance_model \| Model checkpoint used by the Prompt Enhancer \|\n\n## How to use\n\n1. Download the models listed in **Note: Model Links** and place them in ComfyUI's `models/` folder\n2. Replace the image in **Load First Frame** with your own starting frame\n3. Write a prompt describing the motion, optionally toggle **prompt_enhance** for short prompts\n4. Set **duration** / **width** / **height** / **frame_rate** (defaults work well) and hit **Queue**\n5. To dive deeper, click **Enter subgraph** at the bottom of the main node : every internal step (conditioning, sampler, CFG, VAE decode) can be edited there\n" | "### What It Does\n\nAnimate a starting image into a video with sound.\n\n### How to Use\n\n1. Replace the image in **Load First Frame**.\n2. In **Image to Video (LTX-2.5)**, describe the movement and sound. Set **duration** in seconds and choose the frame rate. The saved setup takes its size from the resized image.\n3. Click **Run**. Check **Video Details** and look for `LTX-2.5_i2v` files under `ComfyUI/output/video/`.\n\n### Setup and Reference\n\nInstall the [LTX-2.5 model files](https://huggingface.co/Lightricks/LTX-2.5) in ComfyUI’s `models/` folder. See the repository README for the file list and folders. Use **Enter subgraph** to inspect advanced controls.\n\n\| Parameter \| What it does \|\n\|---\|---\|\n\| first_frame \| Starting image that the video continues from (load your own image in **Load First Frame**) \|\n\| prompt \| Text prompt describing the motion, scene, lighting, camera, and style \|\n\| prompt_enhance \| Expand a short prompt before generation \|\n\| duration \| Clip length in seconds \|\n\| width / height \| Output resolution in pixels (e.g. 1280×720) \|\n\| seed \| Random seed : set a fixed value to reproduce the same result \|\n\| frame_rate \| Frames per second \|\n\| unet_name \| Main model: LTX-2.5 distilled transformer (ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors) \|\n\| video_vae \| Video VAE used for decoding (ltx-2.5-video-vae-bf16.safetensors) \|\n\| audio_vae \| Audio VAE that produces synchronized audio (ltx-2.5-audio-vae-bf16.safetensors) \|\n\| clip_name \| Text encoder: custom Gemma 4 12B with projection (gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors) \|\n\| upscale_model \| Latent upscaler applied before decoding for higher-fidelity output \|\n\| prompt_enhance_model \| Model checkpoint used by the Prompt Enhancer \|" | Allowed |
| /nodes/6/bgcolor | Node 398 (6e397a2b-68f7-48f6-8930-f3a5491a163c) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/6/color | Node 398 (6e397a2b-68f7-48f6-8930-f3a5491a163c) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/6/title | Node 398 (6e397a2b-68f7-48f6-8930-f3a5491a163c) | (absent; ComfyUI default) | "Image to Video (LTX-2.5)" | Allowed |
| /nodes/7/bgcolor | Node 413 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/7/color | Node 413 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/7/title | Node 413 (PreviewAny) | "Video Info" | "Video Details" | Allowed |

## LTX Video 2.5 T2V.json

Result: **PASS** — 57 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:LTX Video 2.5 T2V.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: none.

Original SHA-256: `f8214dbf055827fda7e550076e9b4eaff9f0f9af49460bff08f76dc582d900a2`

Modified SHA-256: `7394574735c0d7787a493c6bac5e0c30db6d60de433ba54b441de84fe4961d2e`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 6 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/color | Group 7 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/2/color | Group 2 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/3/color | Group 3 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/4/color | Group 21 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/5/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/6/color | Group 22 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/6/title | Group 22 | "Number conversion" | "Number Conversion" | Allowed |
| /definitions/subgraphs/0/groups/7/color | Group 19 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/0/groups/8/color | Group 27 | (absent; ComfyUI default) | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/18/bgcolor | Node 364 (CLIPTextEncode) | "#353" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/18/color | Node 364 (CLIPTextEncode) | "#232" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/19/bgcolor | Node 373 (CLIPTextEncode) | "#535" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/19/color | Node 373 (CLIPTextEncode) | "#323" | "#235B74" | Allowed |
| /definitions/subgraphs/0/nodes/22/bgcolor | Node 381 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/22/color | Node 381 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/0/nodes/22/title | Node 381 (PreviewAny) | (absent; ComfyUI default) | "Prompt Preview" | Allowed |
| /definitions/subgraphs/0/nodes/34/bgcolor | Node 360 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/34/color | Node 360 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/34/title | Node 360 (PrimitiveInt) | "Height" | "Height (Pixels)" | Allowed |
| /definitions/subgraphs/0/nodes/35/bgcolor | Node 361 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/35/color | Node 361 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/35/title | Node 361 (PrimitiveInt) | "Frame Rate" | "Frame Rate (FPS)" | Allowed |
| /definitions/subgraphs/0/nodes/36/bgcolor | Node 362 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/36/color | Node 362 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/36/title | Node 362 (PrimitiveInt) | "Duration" | "Duration (Seconds)" | Allowed |
| /definitions/subgraphs/0/nodes/37/bgcolor | Node 372 (PrimitiveInt) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/37/color | Node 372 (PrimitiveInt) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/37/title | Node 372 (PrimitiveInt) | "Width" | "Width (Pixels)" | Allowed |
| /definitions/subgraphs/0/nodes/38/bgcolor | Node 376 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/38/color | Node 376 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /definitions/subgraphs/0/nodes/40/bgcolor | Node 383 (PrimitiveBoolean) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/40/color | Node 383 (PrimitiveBoolean) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/40/title | Node 383 (PrimitiveBoolean) | "Boolean (Enable Prompt Enhance)" | "Use Prompt Enhancement" | Allowed |
| /nodes/0/bgcolor | Node 408 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /nodes/0/color | Node 408 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /nodes/1/bgcolor | Node 411 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /nodes/1/color | Node 411 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /nodes/2/bgcolor | Node 412 (MarkdownNote) | "#653" | "#30343B" | Allowed |
| /nodes/2/color | Node 412 (MarkdownNote) | "#432" | "#35414A" | Allowed |
| /nodes/2/title | Node 412 (MarkdownNote) | "Note: Model Links" | "Model Access" | Allowed |
| /nodes/2/widgets_values/0 | Note 412 | "Before you download all the models, please make sure you have granted access to [LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) first." | "Request access to the [LTX-2.5 model files](https://huggingface.co/Lightricks/LTX-2.5) before downloading them." | Allowed |
| /nodes/2/widgets_values_named/text | Note 412 | "Before you download all the models, please make sure you have granted access to [LTX-2.5](https://huggingface.co/Lightricks/LTX-2.5) first." | "Request access to the [LTX-2.5 model files](https://huggingface.co/Lightricks/LTX-2.5) before downloading them." | Allowed |
| /nodes/3/bgcolor | Node 75 (SaveVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/3/color | Node 75 (SaveVideo) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/3/title | Node 75 (SaveVideo) | (absent; ComfyUI default) | "Save Video" | Allowed |
| /nodes/4/bgcolor | Node 409 (ResolutionSelector) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/4/color | Node 409 (ResolutionSelector) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/4/title | Node 409 (ResolutionSelector) | (absent; ComfyUI default) | "Image Size (Ratio and Megapixels)" | Allowed |
| /nodes/5/bgcolor | Node 407 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /nodes/5/color | Node 407 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /nodes/5/title | Node 407 (MarkdownNote) | "Note: About LTX-2.5" | "Quick Start" | Allowed |
| /nodes/5/widgets_values/0 | Note 407 | "# LTX-2.5\n\nLTX-2.5 is Lightricks' open video generation model : fast, local-first, and built for production. Run it locally, fine-tune it for your own use case, or integrate it into your pipeline.\n\n**Key highlights:**\n\n- **Pixel Diffusion** : keyframes-first generation that builds every scene on a grid of high-fidelity keyframes for industry-leading pixel quality\n- **Diffusion Video Decoder** : sharper faces, legible text, fewer smears in fast motion\n- **Native multishot** : one generation yields multiple connected shots holding character, environment, lighting, voice, and style across cuts\n- **Custom Gemma 4 12B text encoder** : retains multiple subjects, actions, lighting, detail, and camera direction across complex prompts\n- **Dedicated Prompt Enhancer** : a lightweight model that expands short prompts into rich cinematic instructions at near-zero extra compute\n- **Auto Duration** : predicts the right clip length from the described action before diffusion begins\n- **Better distilled model** : carries far more quality, prompt adherence, and motion into a smaller, faster variant\n- Carried over from LTX-2.3: native 4K, synchronized audio-video\n\nOfficial model & files: https://huggingface.co/Lightricks/LTX-2.5\n## What this workflow does\n\nThis **Text-to-Video** workflow generates a video directly from a text prompt. Write your prompt, optionally enable the Prompt Enhancer, and the model renders a clip with cinematic pixel quality and synchronized audio.\n\n## Subgraph parameters\n\nThe **Text to Video (LTX-2.5)** node is a subgraph. Click the **Enter subgraph** button at the bottom of the node to open its internal graph, where you can inspect and fine-tune every step of the pipeline (conditioning, sampler, CFG guider, VAE decode, and more).\n\n\| Parameter \| What it does \|\n\|---\|---\|\n\| prompt \| Text prompt describing the scene, action, lighting, camera, and style \|\n\| prompt_enhance \| Toggle the built-in Prompt Enhancer: expands short prompts into rich cinematic instructions at near-zero extra compute \|\n\| duration \| Clip length in seconds (Auto Duration can predict it from the action) \|\n\| width / height \| Output resolution in pixels (e.g. 1280×720) \|\n\| seed \| Random seed : set a fixed value to reproduce the same result \|\n\| frame_rate \| Frames per second \|\n\| unet_name \| Main model: LTX-2.5 distilled transformer (ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors) \|\n\| video_vae \| Video VAE used for decoding (ltx-2.5-video-vae-bf16.safetensors) \|\n\| audio_vae \| Audio VAE that produces synchronized audio (ltx-2.5-audio-vae-bf16.safetensors) \|\n\| clip_name \| Text encoder: custom Gemma 4 12B with projection (gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors) \|\n\| upscale_model \| Latent upscaler applied before decoding for higher-fidelity output \|\n\| prompt_enhance_model \| Model checkpoint used by the Prompt Enhancer \|\n\n## How to use\n\n1. Download the models listed in **Note: Model Links** and place them in ComfyUI's `models/` folder\n2. Write your prompt, optionally toggle **prompt_enhance** for short prompts\n3. Set **duration** / **width** / **height** / **frame_rate** (defaults work well) and hit **Queue**\n4. To dive deeper, click **Enter subgraph** at the bottom of the main node : every internal step (conditioning, sampler, CFG, VAE decode) can be edited there\n" | "### What It Does\n\nGenerate a video with sound from a written description.\n\n### How to Use\n\n1. Describe the scene, action, and sound in **Text to Video (LTX-2.5)**.\n2. Choose the shape and size in **Image Size (Ratio and Megapixels)**. Set **duration** in seconds and choose the frame rate. Use **prompt_enhance** to expand your wording if desired.\n3. Click **Run**. **Save Video** writes `LTX_2.5_t2v` files under `ComfyUI/output/video/`.\n\n### Setup and Reference\n\nInstall the [LTX-2.5 model files](https://huggingface.co/Lightricks/LTX-2.5) in ComfyUI’s `models/` folder. See **Note: Model Links** for the file list. Use **Enter subgraph** to inspect advanced controls.\n\n\| Parameter \| What it does \|\n\|---\|---\|\n\| prompt \| Text prompt describing the scene, action, lighting, camera, and style \|\n\| prompt_enhance \| Expand a short prompt before generation \|\n\| duration \| Clip length in seconds \|\n\| width / height \| Output resolution in pixels (e.g. 1280×720) \|\n\| seed \| Random seed : set a fixed value to reproduce the same result \|\n\| frame_rate \| Frames per second \|\n\| unet_name \| Main model: LTX-2.5 distilled transformer (ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors) \|\n\| video_vae \| Video VAE used for decoding (ltx-2.5-video-vae-bf16.safetensors) \|\n\| audio_vae \| Audio VAE that produces synchronized audio (ltx-2.5-audio-vae-bf16.safetensors) \|\n\| clip_name \| Text encoder: custom Gemma 4 12B with projection (gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors) \|\n\| upscale_model \| Latent upscaler applied before decoding for higher-fidelity output \|\n\| prompt_enhance_model \| Model checkpoint used by the Prompt Enhancer \|" | Allowed |
| /nodes/5/widgets_values_named/text | Note 407 | "# LTX-2.5\n\nLTX-2.5 is Lightricks' open video generation model : fast, local-first, and built for production. Run it locally, fine-tune it for your own use case, or integrate it into your pipeline.\n\n**Key highlights:**\n\n- **Pixel Diffusion** : keyframes-first generation that builds every scene on a grid of high-fidelity keyframes for industry-leading pixel quality\n- **Diffusion Video Decoder** : sharper faces, legible text, fewer smears in fast motion\n- **Native multishot** : one generation yields multiple connected shots holding character, environment, lighting, voice, and style across cuts\n- **Custom Gemma 4 12B text encoder** : retains multiple subjects, actions, lighting, detail, and camera direction across complex prompts\n- **Dedicated Prompt Enhancer** : a lightweight model that expands short prompts into rich cinematic instructions at near-zero extra compute\n- **Auto Duration** : predicts the right clip length from the described action before diffusion begins\n- **Better distilled model** : carries far more quality, prompt adherence, and motion into a smaller, faster variant\n- Carried over from LTX-2.3: native 4K, synchronized audio-video\n\nOfficial model & files: https://huggingface.co/Lightricks/LTX-2.5\n## What this workflow does\n\nThis **Text-to-Video** workflow generates a video directly from a text prompt. Write your prompt, optionally enable the Prompt Enhancer, and the model renders a clip with cinematic pixel quality and synchronized audio.\n\n## Subgraph parameters\n\nThe **Text to Video (LTX-2.5)** node is a subgraph. Click the **Enter subgraph** button at the bottom of the node to open its internal graph, where you can inspect and fine-tune every step of the pipeline (conditioning, sampler, CFG guider, VAE decode, and more).\n\n\| Parameter \| What it does \|\n\|---\|---\|\n\| prompt \| Text prompt describing the scene, action, lighting, camera, and style \|\n\| prompt_enhance \| Toggle the built-in Prompt Enhancer: expands short prompts into rich cinematic instructions at near-zero extra compute \|\n\| duration \| Clip length in seconds (Auto Duration can predict it from the action) \|\n\| width / height \| Output resolution in pixels (e.g. 1280×720) \|\n\| seed \| Random seed : set a fixed value to reproduce the same result \|\n\| frame_rate \| Frames per second \|\n\| unet_name \| Main model: LTX-2.5 distilled transformer (ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors) \|\n\| video_vae \| Video VAE used for decoding (ltx-2.5-video-vae-bf16.safetensors) \|\n\| audio_vae \| Audio VAE that produces synchronized audio (ltx-2.5-audio-vae-bf16.safetensors) \|\n\| clip_name \| Text encoder: custom Gemma 4 12B with projection (gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors) \|\n\| upscale_model \| Latent upscaler applied before decoding for higher-fidelity output \|\n\| prompt_enhance_model \| Model checkpoint used by the Prompt Enhancer \|\n\n## How to use\n\n1. Download the models listed in **Note: Model Links** and place them in ComfyUI's `models/` folder\n2. Write your prompt, optionally toggle **prompt_enhance** for short prompts\n3. Set **duration** / **width** / **height** / **frame_rate** (defaults work well) and hit **Queue**\n4. To dive deeper, click **Enter subgraph** at the bottom of the main node : every internal step (conditioning, sampler, CFG, VAE decode) can be edited there\n" | "### What It Does\n\nGenerate a video with sound from a written description.\n\n### How to Use\n\n1. Describe the scene, action, and sound in **Text to Video (LTX-2.5)**.\n2. Choose the shape and size in **Image Size (Ratio and Megapixels)**. Set **duration** in seconds and choose the frame rate. Use **prompt_enhance** to expand your wording if desired.\n3. Click **Run**. **Save Video** writes `LTX_2.5_t2v` files under `ComfyUI/output/video/`.\n\n### Setup and Reference\n\nInstall the [LTX-2.5 model files](https://huggingface.co/Lightricks/LTX-2.5) in ComfyUI’s `models/` folder. See **Note: Model Links** for the file list. Use **Enter subgraph** to inspect advanced controls.\n\n\| Parameter \| What it does \|\n\|---\|---\|\n\| prompt \| Text prompt describing the scene, action, lighting, camera, and style \|\n\| prompt_enhance \| Expand a short prompt before generation \|\n\| duration \| Clip length in seconds \|\n\| width / height \| Output resolution in pixels (e.g. 1280×720) \|\n\| seed \| Random seed : set a fixed value to reproduce the same result \|\n\| frame_rate \| Frames per second \|\n\| unet_name \| Main model: LTX-2.5 distilled transformer (ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors) \|\n\| video_vae \| Video VAE used for decoding (ltx-2.5-video-vae-bf16.safetensors) \|\n\| audio_vae \| Audio VAE that produces synchronized audio (ltx-2.5-audio-vae-bf16.safetensors) \|\n\| clip_name \| Text encoder: custom Gemma 4 12B with projection (gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors) \|\n\| upscale_model \| Latent upscaler applied before decoding for higher-fidelity output \|\n\| prompt_enhance_model \| Model checkpoint used by the Prompt Enhancer \|" | Allowed |
| /nodes/6/bgcolor | Node 405 (8b4f085c-1bb3-4ecd-aeed-603a8d6d3970) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/6/color | Node 405 (8b4f085c-1bb3-4ecd-aeed-603a8d6d3970) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/6/title | Node 405 (8b4f085c-1bb3-4ecd-aeed-603a8d6d3970) | (absent; ComfyUI default) | "Text to Video (LTX-2.5)" | Allowed |

## Minimax H3 CharacterSheet 6p.json

Result: **PASS** — 63 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Minimax H3 CharacterSheet 6p.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: none.

Original SHA-256: `ff98ba38871a166c854613296f4bd9977d1feefb849610003b627de9f0d511ab`

Modified SHA-256: `052100f96b4b1d8b6ca7a65c0df11f58896451ea873c8e6c716dc001717db377`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 6 | "#8A8" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/0/bgcolor | Node 201 (ImageFromBatch) | "#593930" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/0/color | Node 201 (ImageFromBatch) | "#332922" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/0/title | Node 201 (ImageFromBatch) | "2  left side    (orbit 25%)" | "2  Left Side    (orbit 25%)" | Allowed |
| /definitions/subgraphs/0/nodes/1/bgcolor | Node 202 (ImageFromBatch) | "#593930" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/1/color | Node 202 (ImageFromBatch) | "#332922" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/1/title | Node 202 (ImageFromBatch) | "3  back         (orbit 50%)" | "3  Back         (orbit 50%)" | Allowed |
| /definitions/subgraphs/0/nodes/2/bgcolor | Node 203 (ImageFromBatch) | "#593930" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/2/color | Node 203 (ImageFromBatch) | "#332922" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/2/title | Node 203 (ImageFromBatch) | "4  right side   (orbit 75%)" | "4  Right Side   (orbit 75%)" | Allowed |
| /definitions/subgraphs/0/nodes/3/bgcolor | Node 205 (ImageFromBatch) | "#593930" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/3/color | Node 205 (ImageFromBatch) | "#332922" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/3/title | Node 205 (ImageFromBatch) | "6  face 3/4     (beat 3)" | "6  Face 3/4     (beat 3)" | Allowed |
| /definitions/subgraphs/0/nodes/4/bgcolor | Node 200 (ImageFromBatch) | "#593930" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/4/color | Node 200 (ImageFromBatch) | "#332922" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/4/title | Node 200 (ImageFromBatch) | "1  front        (orbit 0%)" | "1  Front        (orbit 0%)" | Allowed |
| /definitions/subgraphs/0/nodes/9/title | Node 216 (ImageStitch) | "Stack rows" | "Stack Rows" | Allowed |
| /definitions/subgraphs/0/nodes/10/bgcolor | Node 204 (ImageFromBatch) | "#593930" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/10/color | Node 204 (ImageFromBatch) | "#332922" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/10/title | Node 204 (ImageFromBatch) | "5  face front   (beat 2)" | "5  Face Front   (beat 2)" | Allowed |
| /definitions/subgraphs/1/nodes/1/bgcolor | Node 245 (ModelPatchTorchSettings) | "#000" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/1/color | Node 245 (ModelPatchTorchSettings) | "#222" | "#35414A" | Allowed |
| /definitions/subgraphs/1/nodes/3/bgcolor | Node 250 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/3/color | Node 250 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /definitions/subgraphs/1/nodes/3/title | Node 250 (MarkdownNote) | "Note: Speed Patches (updated)" | "Speed Settings Reference" | Allowed |
| /definitions/subgraphs/1/nodes/4/bgcolor | Node 246 (MiniMaxChunkFeedForward) | "#000" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/4/color | Node 246 (MiniMaxChunkFeedForward) | "#222" | "#35414A" | Allowed |
| /definitions/subgraphs/2/groups/0/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/2/groups/1/color | Group 2 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/2/groups/2/color | Group 3 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/2/groups/3/color | Group 4 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/2/groups/4/color | Group 5 | "#3f789e" | "#235B74" | Allowed |
| /definitions/subgraphs/2/groups/5/color | Group 106 | "#a1309b" | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/6/bgcolor | Node 247 (Fast Groups Bypasser (rgthree)) | "#000" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/6/color | Node 247 (Fast Groups Bypasser (rgthree)) | "#222" | "#715B2D" | Allowed |
| /definitions/subgraphs/2/nodes/6/title | Node 247 (Fast Groups Bypasser (rgthree)) | "Speed Ups (toggle on/off)" | "Speed Ups (Toggle On/Off)" | Allowed |
| /definitions/subgraphs/2/nodes/8/bgcolor | Node 248 (9c4f1e7a-3b2d-4a86-9f10-5d7c8e4b21af) | "#000" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/8/color | Node 248 (9c4f1e7a-3b2d-4a86-9f10-5d7c8e4b21af) | "#222" | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/15/bgcolor | Node 239 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/15/color | Node 239 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/15/title | Node 239 (PrimitiveStringMultiline) | "Prompt for orbiting - (Keep Picture 1's Style)" | "Prompt for Orbiting - (Keep Picture 1's Style)" | Allowed |
| /groups/0/color | Group 7 | "#b58b2a" | "#2B644C" | Allowed |
| /groups/1/color | Group 107 | "#b58b2a" | "#35414A" | Allowed |
| /nodes/0/title | Node 270 (69b3b298-5399-4e05-8e25-53cebfe3e588) | (absent; ComfyUI default) | "MiniMax H3 Character Sheet" | Allowed |
| /nodes/1/bgcolor | Node 137 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/1/color | Node 137 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/1/title | Node 137 (LoadImage) | (absent; ComfyUI default) | "Reference Image" | Allowed |
| /nodes/2/bgcolor | Node 142 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /nodes/2/color | Node 142 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /nodes/2/title | Node 142 (MarkdownNote) | "README — H3 Character Sheet Maker" | "Quick Start" | Allowed |
| /nodes/2/widgets_values/0 | Note 142 | "# H3 Character Sheet Maker\n\nTurn up to **9 reference images** into a clean six-view character sheet in a single generation.\n\nFeed it a face, an outfit, a weapon and a hat, and H3 will assemble them into one coherent character,\nthen show you that character from four sides plus two face close-ups.\n\n---\n\n## Why a video model\n\nSix separate image generations of the same character will disagree with each other — the jaw shifts,\nthe jacket changes, the palette drifts. Six frames from **one** video generation physically cannot,\nbecause they share a single denoising pass.\n\nThis workflow renders one continuous 360° orbit, pulls six frames out of it, and stitches them into a\nsheet. No hard cuts anywhere, so nothing gets a chance to reinvent itself between shots. The camera\ndoes all the moving; the character stays frozen.\n\n---\n\n## Quick start\n\n1. **Load your references.** Any mix of photos, drawings or anime art. The first one sets the style.\n2. **Fill in `Input Text (Prompt)`** — one line per image saying what to take and what to ignore.\n3. **Pick your size** on the Resolution Selector: aspect ratio, then megapixels.\n4. **Leave duration at 5.** Everything downstream is tuned to it.\n5. Queue. The finished sheet lands in `ComfyUI/output/charsheet/`.\n\n---\n\n## The two prompt boxes\n\nThey get joined together automatically, so you only ever touch the first one.\n\n**`Input Text (Prompt)`** — yours. Assign every image one job and one ignore list:\n\n```\n<Picture 1> - keep the photo style. Use the bald head, facial hair, physique.\n<Picture 2> - keep only the black outfit. Remove the hair, remove accessories.\n<Picture 3> - use the shield. It is attached to the man's back.\n```\n\nBeing blunt about what to *ignore* matters as much as what to keep. Backgrounds, poses and the wrong\nperson's face all travel across unless you rule them out by name.\n\nDescribe fabrics and materials **in words** too. Faces carry across on their own; wardrobe drifts.\n\"Black high-collared coat with silver buckles\" survives where \"the outfit from `<Picture 2>`\" wanders.\n\n**`Prompt for orbiting`** — the fixed half. Backdrop, lighting, lens, the A-pose, the statue lock and\nthe three beat timings. Leave it alone unless you're changing the shot structure, and if you do, see\n*Retiming* below.\n\n---\n\n## What you get\n\n\| # \| View \| Source \|\n\|---\|---\|---\|\n\| 1 \| Front \| orbit 0% \|\n\| 2 \| Left side \| orbit 25% \|\n\| 3 \| Back \| orbit 50% \|\n\| 4 \| Right side \| orbit 75% \|\n\| 5 \| Face, front \| beat 2 \|\n\| 6 \| Face, three-quarter \| beat 3 \|\n\nLaid out 3 wide × 2 tall with thin black gutters.\n\n---\n\n## Settings worth knowing\n\n**Duration — leave at 5.** That's 124 frames. Valid lengths are `17n + 5`: 5, 22, 39, 56, 73, 90,\n107, 124. Anything else rounds up. 124 puts the orbit at roughly 100°/s, an ordinary turntable speed.\nGo much shorter and the spin outruns the model — it smears past about 5° per frame.\n\n**Aspect ratio.** Portrait for people. 9:16 wastes the least frame on a standing figure.\n\n**Megapixels.** 0.5 to scout, 0.7 for normal use, 1.2+ when you want the face crops to hold up. Cost\nscales roughly linearly, so prove the composition cheap before you commit.\n\n**Speed-up nodes.** Sage Attention and caching both cost some prompt adherence here. Deliberately left out. Add them if you like.\n\n**Optional outputs.** Two extra save nodes are bypassed by default: every individual frame, and the\nraw video. Un-bypass either if you want to cherry-pick your own angles.\n\n---\n\n## Getting good results\n\n**Give it a back view if you have one.** With only front-facing references the entire back of your\ncharacter is invented. This is the single biggest quality lever in the workflow, and no amount of\nprompt tuning substitutes for it.\n\n**Watch for flutter.** Hair and cloth want to move. The fixed prompt already freezes them hard; if\nsomething still ripples, name the specific offender in your input box.\n\n**Assembling from many sources?** If the character is built from three or more images, consider two\nstages: run once to get a clean front view, then feed *that* render back in as `<Picture 1>` and\nbuild the sheet from it. A purpose-made reference beats a pile of contradictory ones.\n\n**Retiming.** The six grab points are locked to the beat timings in the fixed prompt. If you change\nthose times or the duration, open the subgraph and move the frame indexes to match, or the grabs will\nland mid-transition.\n\n---\n\n## Then what\n\nUse the character sheet how you would like. You can input it as a reference for future H3 video generation, use it for custom DnD character, use it for visualizing characters or props. " | "### What It Does\n\nMake a six-view character sheet from a single MiniMax H3 turntable video.\n\n### How to Use\n\n1. Start with one clear picture in **Reference Image**. The saved canvas is wired for one reference.\n2. In **Input Text (Prompt)**, say what to keep and what to leave out. Choose the shape and size. Keep the saved duration so the frame picks line up.\n3. Click **Run**. Find the sheet and turntable clip in `ComfyUI/output/charsheet/`.\n\n### Reference Examples and Advanced Settings\n\nMiniMax H3 can use up to nine reference images when wired for them. The sheet comes from one continuous turntable shot.\n\n## The two prompt boxes\n\nThey get joined together automatically, so you only ever touch the first one.\n\n**`Input Text (Prompt)`** — yours. Assign every image one job and one ignore list:\n\n```\n<Picture 1> - keep the photo style. Use the bald head, facial hair, physique.\n<Picture 2> - keep only the black outfit. Remove the hair, remove accessories.\n<Picture 3> - use the shield. It is attached to the man's back.\n```\n\nBeing blunt about what to *ignore* matters as much as what to keep. Backgrounds, poses and the wrong\nperson's face all travel across unless you rule them out by name.\n\nDescribe fabrics and materials **in words** too. Faces carry across on their own; wardrobe drifts.\n\"Black high-collared coat with silver buckles\" survives where \"the outfit from `<Picture 2>`\" wanders.\n\n**`Prompt for orbiting`** — the fixed half. Backdrop, lighting, lens, the A-pose, the statue lock and\nthe three beat timings. Leave it alone unless you're changing the shot structure, and if you do, see\n*Retiming* below.\n\n---\n\n## What you get\n\n\| # \| View \| Source \|\n\|---\|---\|---\|\n\| 1 \| Front \| orbit 0% \|\n\| 2 \| Left side \| orbit 25% \|\n\| 3 \| Back \| orbit 50% \|\n\| 4 \| Right side \| orbit 75% \|\n\| 5 \| Face, front \| beat 2 \|\n\| 6 \| Face, three-quarter \| beat 3 \|\n\nLaid out 3 wide × 2 tall with thin black gutters.\n\n---\n\n## Settings worth knowing\n\n**Duration — leave at 5.** That's 124 frames. Valid lengths are `17n + 5`: 5, 22, 39, 56, 73, 90,\n107, 124. Anything else rounds up. 124 puts the orbit at roughly 100°/s, an ordinary turntable speed.\nGo much shorter and the spin outruns the model — it smears past about 5° per frame.\n\n**Aspect ratio.** Portrait for people. 9:16 wastes the least frame on a standing figure.\n\n**Megapixels.** 0.5 to scout, 0.7 for normal use, 1.2+ when you want the face crops to hold up. Cost\nscales roughly linearly, so prove the composition cheap before you commit.\n\n**Speed settings.** Start with the saved controls. See **Speed Settings Reference** for advanced options.\n\n---\n\n## Getting good results\n\n**Give it a back view if you have one.** With only front-facing references the entire back of your\ncharacter is invented. This is the single biggest quality lever in the workflow, and no amount of\nprompt tuning substitutes for it.\n\n**Watch for flutter.** Hair and cloth want to move. The fixed prompt already freezes them hard; if\nsomething still ripples, name the specific offender in your input box.\n\n**Assembling from many sources?** If the character is built from three or more images, consider two\nstages: run once to get a clean front view, then feed *that* render back in as `<Picture 1>` and\nbuild the sheet from it. A purpose-made reference beats a pile of contradictory ones.\n\n**Retiming.** The six grab points are locked to the beat timings in the fixed prompt. If you change\nthose times or the duration, open the subgraph and move the frame indexes to match, or the grabs will\nland mid-transition.\n\n---\n\n## Then what\n\nUse the character sheet how you would like. You can input it as a reference for future H3 video generation, use it for custom DnD character, use it for visualizing characters or props." | Allowed |
| /nodes/2/widgets_values_named/text | Note 142 | "# H3 Character Sheet Maker\n\nTurn up to **9 reference images** into a clean six-view character sheet in a single generation.\n\nFeed it a face, an outfit, a weapon and a hat, and H3 will assemble them into one coherent character,\nthen show you that character from four sides plus two face close-ups.\n\n---\n\n## Why a video model\n\nSix separate image generations of the same character will disagree with each other — the jaw shifts,\nthe jacket changes, the palette drifts. Six frames from **one** video generation physically cannot,\nbecause they share a single denoising pass.\n\nThis workflow renders one continuous 360° orbit, pulls six frames out of it, and stitches them into a\nsheet. No hard cuts anywhere, so nothing gets a chance to reinvent itself between shots. The camera\ndoes all the moving; the character stays frozen.\n\n---\n\n## Quick start\n\n1. **Load your references.** Any mix of photos, drawings or anime art. The first one sets the style.\n2. **Fill in `Input Text (Prompt)`** — one line per image saying what to take and what to ignore.\n3. **Pick your size** on the Resolution Selector: aspect ratio, then megapixels.\n4. **Leave duration at 5.** Everything downstream is tuned to it.\n5. Queue. The finished sheet lands in `ComfyUI/output/charsheet/`.\n\n---\n\n## The two prompt boxes\n\nThey get joined together automatically, so you only ever touch the first one.\n\n**`Input Text (Prompt)`** — yours. Assign every image one job and one ignore list:\n\n```\n<Picture 1> - keep the photo style. Use the bald head, facial hair, physique.\n<Picture 2> - keep only the black outfit. Remove the hair, remove accessories.\n<Picture 3> - use the shield. It is attached to the man's back.\n```\n\nBeing blunt about what to *ignore* matters as much as what to keep. Backgrounds, poses and the wrong\nperson's face all travel across unless you rule them out by name.\n\nDescribe fabrics and materials **in words** too. Faces carry across on their own; wardrobe drifts.\n\"Black high-collared coat with silver buckles\" survives where \"the outfit from `<Picture 2>`\" wanders.\n\n**`Prompt for orbiting`** — the fixed half. Backdrop, lighting, lens, the A-pose, the statue lock and\nthe three beat timings. Leave it alone unless you're changing the shot structure, and if you do, see\n*Retiming* below.\n\n---\n\n## What you get\n\n\| # \| View \| Source \|\n\|---\|---\|---\|\n\| 1 \| Front \| orbit 0% \|\n\| 2 \| Left side \| orbit 25% \|\n\| 3 \| Back \| orbit 50% \|\n\| 4 \| Right side \| orbit 75% \|\n\| 5 \| Face, front \| beat 2 \|\n\| 6 \| Face, three-quarter \| beat 3 \|\n\nLaid out 3 wide × 2 tall with thin black gutters.\n\n---\n\n## Settings worth knowing\n\n**Duration — leave at 5.** That's 124 frames. Valid lengths are `17n + 5`: 5, 22, 39, 56, 73, 90,\n107, 124. Anything else rounds up. 124 puts the orbit at roughly 100°/s, an ordinary turntable speed.\nGo much shorter and the spin outruns the model — it smears past about 5° per frame.\n\n**Aspect ratio.** Portrait for people. 9:16 wastes the least frame on a standing figure.\n\n**Megapixels.** 0.5 to scout, 0.7 for normal use, 1.2+ when you want the face crops to hold up. Cost\nscales roughly linearly, so prove the composition cheap before you commit.\n\n**Speed-up nodes.** Sage Attention and caching both cost some prompt adherence here. Deliberately left out. Add them if you like.\n\n**Optional outputs.** Two extra save nodes are bypassed by default: every individual frame, and the\nraw video. Un-bypass either if you want to cherry-pick your own angles.\n\n---\n\n## Getting good results\n\n**Give it a back view if you have one.** With only front-facing references the entire back of your\ncharacter is invented. This is the single biggest quality lever in the workflow, and no amount of\nprompt tuning substitutes for it.\n\n**Watch for flutter.** Hair and cloth want to move. The fixed prompt already freezes them hard; if\nsomething still ripples, name the specific offender in your input box.\n\n**Assembling from many sources?** If the character is built from three or more images, consider two\nstages: run once to get a clean front view, then feed *that* render back in as `<Picture 1>` and\nbuild the sheet from it. A purpose-made reference beats a pile of contradictory ones.\n\n**Retiming.** The six grab points are locked to the beat timings in the fixed prompt. If you change\nthose times or the duration, open the subgraph and move the frame indexes to match, or the grabs will\nland mid-transition.\n\n---\n\n## Then what\n\nUse the character sheet how you would like. You can input it as a reference for future H3 video generation, use it for custom DnD character, use it for visualizing characters or props. " | "### What It Does\n\nMake a six-view character sheet from a single MiniMax H3 turntable video.\n\n### How to Use\n\n1. Start with one clear picture in **Reference Image**. The saved canvas is wired for one reference.\n2. In **Input Text (Prompt)**, say what to keep and what to leave out. Choose the shape and size. Keep the saved duration so the frame picks line up.\n3. Click **Run**. Find the sheet and turntable clip in `ComfyUI/output/charsheet/`.\n\n### Reference Examples and Advanced Settings\n\nMiniMax H3 can use up to nine reference images when wired for them. The sheet comes from one continuous turntable shot.\n\n## The two prompt boxes\n\nThey get joined together automatically, so you only ever touch the first one.\n\n**`Input Text (Prompt)`** — yours. Assign every image one job and one ignore list:\n\n```\n<Picture 1> - keep the photo style. Use the bald head, facial hair, physique.\n<Picture 2> - keep only the black outfit. Remove the hair, remove accessories.\n<Picture 3> - use the shield. It is attached to the man's back.\n```\n\nBeing blunt about what to *ignore* matters as much as what to keep. Backgrounds, poses and the wrong\nperson's face all travel across unless you rule them out by name.\n\nDescribe fabrics and materials **in words** too. Faces carry across on their own; wardrobe drifts.\n\"Black high-collared coat with silver buckles\" survives where \"the outfit from `<Picture 2>`\" wanders.\n\n**`Prompt for orbiting`** — the fixed half. Backdrop, lighting, lens, the A-pose, the statue lock and\nthe three beat timings. Leave it alone unless you're changing the shot structure, and if you do, see\n*Retiming* below.\n\n---\n\n## What you get\n\n\| # \| View \| Source \|\n\|---\|---\|---\|\n\| 1 \| Front \| orbit 0% \|\n\| 2 \| Left side \| orbit 25% \|\n\| 3 \| Back \| orbit 50% \|\n\| 4 \| Right side \| orbit 75% \|\n\| 5 \| Face, front \| beat 2 \|\n\| 6 \| Face, three-quarter \| beat 3 \|\n\nLaid out 3 wide × 2 tall with thin black gutters.\n\n---\n\n## Settings worth knowing\n\n**Duration — leave at 5.** That's 124 frames. Valid lengths are `17n + 5`: 5, 22, 39, 56, 73, 90,\n107, 124. Anything else rounds up. 124 puts the orbit at roughly 100°/s, an ordinary turntable speed.\nGo much shorter and the spin outruns the model — it smears past about 5° per frame.\n\n**Aspect ratio.** Portrait for people. 9:16 wastes the least frame on a standing figure.\n\n**Megapixels.** 0.5 to scout, 0.7 for normal use, 1.2+ when you want the face crops to hold up. Cost\nscales roughly linearly, so prove the composition cheap before you commit.\n\n**Speed settings.** Start with the saved controls. See **Speed Settings Reference** for advanced options.\n\n---\n\n## Getting good results\n\n**Give it a back view if you have one.** With only front-facing references the entire back of your\ncharacter is invented. This is the single biggest quality lever in the workflow, and no amount of\nprompt tuning substitutes for it.\n\n**Watch for flutter.** Hair and cloth want to move. The fixed prompt already freezes them hard; if\nsomething still ripples, name the specific offender in your input box.\n\n**Assembling from many sources?** If the character is built from three or more images, consider two\nstages: run once to get a clean front view, then feed *that* render back in as `<Picture 1>` and\nbuild the sheet from it. A purpose-made reference beats a pile of contradictory ones.\n\n**Retiming.** The six grab points are locked to the beat timings in the fixed prompt. If you change\nthose times or the duration, open the subgraph and move the frame indexes to match, or the grabs will\nland mid-transition.\n\n---\n\n## Then what\n\nUse the character sheet how you would like. You can input it as a reference for future H3 video generation, use it for custom DnD character, use it for visualizing characters or props." | Allowed |
| /nodes/3/bgcolor | Node 138 (PrimitiveStringMultiline) | "#533" | "#30343B" | Allowed |
| /nodes/3/color | Node 138 (PrimitiveStringMultiline) | "#322" | "#235B74" | Allowed |
| /nodes/4/bgcolor | Node 92 (SaveVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/4/color | Node 92 (SaveVideo) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/4/title | Node 92 (SaveVideo) | (absent; ComfyUI default) | "Save Video" | Allowed |
| /nodes/5/bgcolor | Node 218 (SaveImage) | "#353" | "#30343B" | Allowed |
| /nodes/5/color | Node 218 (SaveImage) | "#232" | "#2B644C" | Allowed |
| /nodes/5/title | Node 218 (SaveImage) | "SAVE CHARACTER SHEET" | "Save Character Sheet" | Allowed |
| /nodes/6/bgcolor | Node 115 (ResolutionSelector) | "#533" | "#30343B" | Allowed |
| /nodes/6/color | Node 115 (ResolutionSelector) | "#322" | "#715B2D" | Allowed |
| /nodes/6/title | Node 115 (ResolutionSelector) | "IMAGE SIZE (pick ratio + megapixels)" | "Image Size (Ratio and Megapixels)" | Allowed |

## Minimax H3 i2v.json

Result: **PASS** — 126 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Minimax H3 i2v.json`

Layout allowance: explicit root-only positions, sizes, and group bounds; embedded layouts remain protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: 372.

Original SHA-256: `65f61cbe68a20f340c21a6f49e76bccab874be6664d9ae4da0c77f982768df99`

Modified SHA-256: `57413f4a042e4900d7e89d3e37cc07c4ba7dcd0390923c0f63a69e05d4011324`

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
| /nodes/9 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 372, "type": "MarkdownNote", "pos": [-2340, 5080], "size": [480, 360], "flags": {}, "order": 9, "mode": 0, "inputs": [], "outputs": [], "title": "MiniMax H3 Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nAnimate a starting image into a video with MiniMax H3.\n\n### How to Use\n\n1. Load **First Frame**. In **Image to Video (MiniMax H3)**, describe the motion and set **seconds** and **megapixels** (image size).\n2. For an ending image, enable **Last Frame (Optional)** and turn on **Last Frame** in the video node. **Prompt Enhance** uses Ollama. Turn it off to keep your wording.\n3. Click **Run**. Watch **Generation Preview** and find `MiniMax_H3` files under `ComfyUI/output/video/`.\n\n**Turbo** and **RTX Upscale 2x** are optional. Use **Seed** to control variation or **LoRA Settings** to load a model add-on."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 371 | 372 | Allowed |

## Minimax H3 r2v.json

Result: **PASS** — 85 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Minimax H3 r2v.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: 407.

Original SHA-256: `86341377006c74d8feec0478595cd2bcf15ac46b1114050d35abec3c598ad367`

Modified SHA-256: `599de26750262d44d5dc0a250dec9a029ae290116e3c338087945f9c412534ec`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/nodes/0/bgcolor | Node 165 (SomethingToString) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/0/color | Node 165 (SomethingToString) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/0/title | Node 165 (SomethingToString) | "Duration" | "Duration to Text" | Allowed |
| /definitions/subgraphs/0/nodes/1/bgcolor | Node 167 (SomethingToString) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/1/color | Node 167 (SomethingToString) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/1/title | Node 167 (SomethingToString) | "Height" | "Height to Text" | Allowed |
| /definitions/subgraphs/0/nodes/5/bgcolor | Node 166 (SomethingToString) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/5/color | Node 166 (SomethingToString) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/5/title | Node 166 (SomethingToString) | "Width" | "Width to Text" | Allowed |
| /definitions/subgraphs/2/nodes/5/bgcolor | Node 365 (MiniMaxChunkFeedForward) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/5/color | Node 365 (MiniMaxChunkFeedForward) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/7/bgcolor | Node 364 (MiniMaxH3SigmaShift) | "#3f5159" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/7/color | Node 364 (MiniMaxH3SigmaShift) | "#2a363b" | "#35414A" | Allowed |
| /definitions/subgraphs/3/groups/0/color | Group 20 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/3/groups/0/title | Group 20 | "Prompt Enhance" | "Prompt Enhancement" | Allowed |
| /definitions/subgraphs/3/nodes/5/bgcolor | Node 334 (f84f8cfe-8943-4a81-aecb-1d67a74ad755) | "#533" | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/5/color | Node 334 (f84f8cfe-8943-4a81-aecb-1d67a74ad755) | "#322" | "#35414A" | Allowed |
| /definitions/subgraphs/3/nodes/6/bgcolor | Node 369 (PreviewImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/6/color | Node 369 (PreviewImage) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/3/nodes/6/title | Node 369 (PreviewImage) | (absent; ComfyUI default) | "Image Preview" | Allowed |
| /definitions/subgraphs/3/nodes/8/bgcolor | Node 378 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/8/color | Node 378 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /definitions/subgraphs/3/nodes/9/title | Node 379 (ComfySwitchNode) | "PE Switch" | "Prompt Enhancement Switch" | Allowed |
| /definitions/subgraphs/3/nodes/11/bgcolor | Node 382 (PrimitiveFloat) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/11/color | Node 382 (PrimitiveFloat) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/3/nodes/11/title | Node 382 (PrimitiveFloat) | "Float (duration)" | "Duration (Seconds)" | Allowed |
| /definitions/subgraphs/3/nodes/12/title | Node 385 (ComfyMathExpression) | "Actual duration = generated frames / 24fps" | "Actual Duration = Generated Frames / 24fps" | Allowed |
| /definitions/subgraphs/3/nodes/13/title | Node 386 (ImageFromBatch) | "Video 1: first frame" | "Video 1: First Frame" | Allowed |
| /definitions/subgraphs/3/nodes/14/title | Node 387 (ImageFromBatch) | "Video 1: last frame" | "Video 1: Last Frame" | Allowed |
| /definitions/subgraphs/3/nodes/15/title | Node 388 (ImageFromBatch) | "Video 2: first frame" | "Video 2: First Frame" | Allowed |
| /definitions/subgraphs/3/nodes/16/title | Node 389 (ImageFromBatch) | "Video 2: last frame" | "Video 2: Last Frame" | Allowed |
| /definitions/subgraphs/3/nodes/17/title | Node 390 (BatchImagesNode) | "Stills + Video 1 first/last (lazy branch)" | "Stills + Video 1 First/last (lazy Branch)" | Allowed |
| /definitions/subgraphs/3/nodes/18/title | Node 391 (GetImageSize) | "Count source pictures" | "Count Source Pictures" | Allowed |
| /definitions/subgraphs/3/nodes/19/title | Node 392 (GetImageSize) | "Count visual attachments" | "Count Visual Attachments" | Allowed |
| /definitions/subgraphs/3/nodes/21/title | Node 394 (ComfySwitchNode) | "Use Video 1 \| frames to H3" | "Use Video 1 \| Frames to H3" | Allowed |
| /definitions/subgraphs/3/nodes/22/title | Node 395 (ComfySwitchNode) | "Use Video 1 \| soundtrack to H3" | "Use Video 1 \| Soundtrack to H3" | Allowed |
| /definitions/subgraphs/3/nodes/23/title | Node 396 (ComfySwitchNode) | "Use Video 2 \| frames to H3" | "Use Video 2 \| Frames to H3" | Allowed |
| /definitions/subgraphs/3/nodes/24/title | Node 397 (ComfySwitchNode) | "Use Video 2 \| soundtrack to H3" | "Use Video 2 \| Soundtrack to H3" | Allowed |
| /definitions/subgraphs/3/nodes/25/title | Node 398 (BatchImagesNode) | "Video 1: first and final frames" | "Video 1: First and Final Frames" | Allowed |
| /definitions/subgraphs/3/nodes/26/title | Node 399 (BatchImagesNode) | "Video 2: first and final frames" | "Video 2: First and Final Frames" | Allowed |
| /definitions/subgraphs/3/nodes/27/title | Node 400 (ComfySwitchNode) | "Add Video 1 previews when enabled" | "Add Video 1 Previews when Enabled" | Allowed |
| /definitions/subgraphs/3/nodes/28/title | Node 401 (BatchImagesNode) | "Previous previews + Video 2 frames" | "Previous Previews + Video 2 Frames" | Allowed |
| /definitions/subgraphs/3/nodes/29/title | Node 402 (ComfySwitchNode) | "Add Video 2 previews when enabled" | "Add Video 2 Previews when Enabled" | Allowed |
| /definitions/subgraphs/3/nodes/31/title | Node 405 (ComfySwitchNode) | "RTX Switch" | "Use RTX Upscaling" | Allowed |
| /definitions/subgraphs/4/nodes/2/title | Node 4 (ComfyMathExpression) | "Duration (frames / fps)" | "Video Duration (Seconds)" | Allowed |
| /definitions/subgraphs/4/nodes/3/title | Node 5 (StringFormat) | "Video metadata summary" | "Video Details Summary" | Allowed |
| /groups/0/color | Group 18 | "#3f789e" | "#35414A" | Allowed |
| /groups/0/title | Group 18 | "ref2v" | "Reference to Video" | Allowed |
| /groups/1/color | Group 19 | "#3f789e" | "#D2B16F" | Allowed |
| /nodes/0/bgcolor | Node 362 (RandomNoise) | "#653" | "#30343B" | Allowed |
| /nodes/0/color | Node 362 (RandomNoise) | "#432" | "#35414A" | Allowed |
| /nodes/1/bgcolor | Node 352 (SaveVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/1/color | Node 352 (SaveVideo) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/1/title | Node 352 (SaveVideo) | (absent; ComfyUI default) | "Save Video" | Allowed |
| /nodes/2/bgcolor | Node 330 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 330 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/2/title | Node 330 (PreviewAny) | "AI Prompt" | "Enhanced Prompt Preview" | Allowed |
| /nodes/3/bgcolor | Node 354 (ResolutionSelector) | "#653" | "#30343B" | Allowed |
| /nodes/3/color | Node 354 (ResolutionSelector) | "#432" | "#715B2D" | Allowed |
| /nodes/3/title | Node 354 (ResolutionSelector) | "Resolution Selector (Size)" | "Resolution (Megapixels)" | Allowed |
| /nodes/4/bgcolor | Node 363 (ModelPreviewOverrideKJ) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/4/color | Node 363 (ModelPreviewOverrideKJ) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/4/title | Node 363 (ModelPreviewOverrideKJ) | (absent; ComfyUI default) | "Generation Preview" | Allowed |
| /nodes/5/bgcolor | Node 332 (LoadImage) | "#593930" | "#30343B" | Allowed |
| /nodes/5/color | Node 332 (LoadImage) | "#332922" | "#235B74" | Allowed |
| /nodes/6/bgcolor | Node 331 (LoadImage) | "#533" | "#30343B" | Allowed |
| /nodes/6/color | Node 331 (LoadImage) | "#322" | "#235B74" | Allowed |
| /nodes/7/bgcolor | Node 370 (LoadVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/7/color | Node 370 (LoadVideo) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/8/bgcolor | Node 372 (LoadAudio) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/8/color | Node 372 (LoadAudio) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/9/bgcolor | Node 373 (LoadAudio) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/9/color | Node 373 (LoadAudio) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/10/bgcolor | Node 374 (LoadVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/10/color | Node 374 (LoadVideo) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/11/bgcolor | Node 376 (LoadImage) | "#593930" | "#30343B" | Allowed |
| /nodes/11/color | Node 376 (LoadImage) | "#332922" | "#235B74" | Allowed |
| /nodes/12/bgcolor | Node 377 (8cf0b957-26c8-4cb5-a847-e4743a82563b) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/12/color | Node 377 (8cf0b957-26c8-4cb5-a847-e4743a82563b) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/12/title | Node 377 (8cf0b957-26c8-4cb5-a847-e4743a82563b) | (absent; ComfyUI default) | "Reference to Video (MiniMax H3)" | Allowed |
| /nodes/13/bgcolor | Node 406 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/13/color | Node 406 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/13/title | Node 406 (PreviewAny) | "Video Info" | "Video Details" | Allowed |
| /nodes/14 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 407, "type": "MarkdownNote", "pos": [-1460, 5560], "size": [480, 360], "flags": {}, "order": 14, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nMake a video using reference pictures, clips, or audio and a written instruction.\n\n### How to Use\n\n1. Start with `<Picture 1>`. Enable other reference nodes as needed. For a clip, also turn on its **Use Video 1** or **Use Video 2** switch.\n2. In **Reference to Video (MiniMax H3)**, say what to borrow from each reference. Use exact tags such as `<Picture 2>`, `<Video 1>`, or `<Audio 1>`. Set **seconds** and choose the output size.\n3. Click **Run**. Check **Generation Preview** and find the video in `ComfyUI/output/video/`. Turn off **Prompt Enhance** if Ollama is unavailable."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 406 | 407 | Allowed |

## Minimax H3 t2v.json

Result: **PASS** — 67 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Minimax H3 t2v.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: 375.

Original SHA-256: `a1a5ea7418348be77c3bfd634c893577176dad17d6e502cbd6f042ca94b7837f`

Modified SHA-256: `4a9e020fce91ff9dd56dd3f2b369b6fcc0d2c70da36e4384fdaa3cd80ac99fb4`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/color | Group 2 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/2/color | Group 3 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/3/color | Group 4 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/3/title | Group 4 | "Decoding and create video" | "Video and Audio Assembly" | Allowed |
| /definitions/subgraphs/0/groups/4/color | Group 18 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/4/title | Group 18 | "Prompt Enhance" | "Prompt Enhancement" | Allowed |
| /definitions/subgraphs/0/groups/5/color | Group 20 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/6/color | Group 24 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/14/bgcolor | Node 277 (PrimitiveFloat) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/14/color | Node 277 (PrimitiveFloat) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/14/title | Node 277 (PrimitiveFloat) | "Float (duration)" | "Duration (Seconds)" | Allowed |
| /definitions/subgraphs/0/nodes/18/title | Node 328 (ComfySwitchNode) | "PE Switch" | "Prompt Enhancement Switch" | Allowed |
| /definitions/subgraphs/0/nodes/25/bgcolor | Node 358 (PrimitiveBoolean) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/25/color | Node 358 (PrimitiveBoolean) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/25/title | Node 358 (PrimitiveBoolean) | "Turbo Boolean" | "Use Turbo" | Allowed |
| /definitions/subgraphs/0/nodes/29/bgcolor | Node 369 (646791c7-9adc-4da3-9a43-820a222b1a8e) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/29/color | Node 369 (646791c7-9adc-4da3-9a43-820a222b1a8e) | "#432" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/31/title | Node 373 (ComfySwitchNode) | "RTX Switch" | "Use RTX Upscaling" | Allowed |
| /definitions/subgraphs/1/nodes/1/bgcolor | Node 342 (MiniMaxChunkFeedForward) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/1/color | Node 342 (MiniMaxChunkFeedForward) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/1/nodes/3/bgcolor | Node 344 (MiniMaxH3SigmaShift) | "#3f5159" | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/3/color | Node 344 (MiniMaxH3SigmaShift) | "#2a363b" | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/1/bgcolor | Node 350 (MiniMaxChunkFeedForward) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/1/color | Node 350 (MiniMaxChunkFeedForward) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/3/bgcolor | Node 352 (MiniMaxH3SigmaShift) | "#3f5159" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/3/color | Node 352 (MiniMaxH3SigmaShift) | "#2a363b" | "#35414A" | Allowed |
| /definitions/subgraphs/3/nodes/0/bgcolor | Node 165 (SomethingToString) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/0/color | Node 165 (SomethingToString) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/3/nodes/0/title | Node 165 (SomethingToString) | "Duration" | "Duration to Text" | Allowed |
| /definitions/subgraphs/3/nodes/1/bgcolor | Node 167 (SomethingToString) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/1/color | Node 167 (SomethingToString) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/3/nodes/1/title | Node 167 (SomethingToString) | "Height" | "Height to Text" | Allowed |
| /definitions/subgraphs/3/nodes/5/bgcolor | Node 166 (SomethingToString) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/5/color | Node 166 (SomethingToString) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/3/nodes/5/title | Node 166 (SomethingToString) | "Width" | "Width to Text" | Allowed |
| /definitions/subgraphs/4/nodes/2/title | Node 4 (ComfyMathExpression) | "Duration (frames / fps)" | "Video Duration (Seconds)" | Allowed |
| /definitions/subgraphs/4/nodes/3/title | Node 5 (StringFormat) | "Video metadata summary" | "Video Details Summary" | Allowed |
| /groups/0/color | Group 15 | "#3f789e" | "#35414A" | Allowed |
| /groups/1/color | Group 17 | "#3f789e" | "#D2B16F" | Allowed |
| /groups/1/title | Group 17 | "Extra Settings" | "Creative Settings" | Allowed |
| /nodes/0/bgcolor | Node 300 (Power Lora Loader (rgthree)) | "#653" | "#30343B" | Allowed |
| /nodes/0/color | Node 300 (Power Lora Loader (rgthree)) | "#432" | "#715B2D" | Allowed |
| /nodes/0/title | Node 300 (Power Lora Loader (rgthree)) | (absent; ComfyUI default) | "LoRA Settings" | Allowed |
| /nodes/1/bgcolor | Node 293 (SeedNode) | "#653" | "#30343B" | Allowed |
| /nodes/1/color | Node 293 (SeedNode) | "#432" | "#715B2D" | Allowed |
| /nodes/1/title | Node 293 (SeedNode) | (absent; ComfyUI default) | "Seed" | Allowed |
| /nodes/2/bgcolor | Node 290 (SaveVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 290 (SaveVideo) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/2/title | Node 290 (SaveVideo) | (absent; ComfyUI default) | "Save Video" | Allowed |
| /nodes/3/bgcolor | Node 289 (e5f30591-fb92-4c19-ba9b-d9687794a624) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/3/color | Node 289 (e5f30591-fb92-4c19-ba9b-d9687794a624) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/3/title | Node 289 (e5f30591-fb92-4c19-ba9b-d9687794a624) | "Text to Video (MiniMax H3) TURBO" | "Text to Video (MiniMax H3)" | Allowed |
| /nodes/4/bgcolor | Node 295 (ModelPreviewOverrideKJ) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/4/color | Node 295 (ModelPreviewOverrideKJ) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/4/title | Node 295 (ModelPreviewOverrideKJ) | (absent; ComfyUI default) | "Generation Preview" | Allowed |
| /nodes/5/bgcolor | Node 363 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/5/color | Node 363 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/5/title | Node 363 (PreviewAny) | "Prompt Enhance Output" | "Enhanced Prompt Preview" | Allowed |
| /nodes/6/bgcolor | Node 370 (ResolutionSelector) | "#653" | "#30343B" | Allowed |
| /nodes/6/color | Node 370 (ResolutionSelector) | "#432" | "#715B2D" | Allowed |
| /nodes/6/title | Node 370 (ResolutionSelector) | (absent; ComfyUI default) | "Image Size (Ratio and Megapixels)" | Allowed |
| /nodes/7/bgcolor | Node 374 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/7/color | Node 374 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/7/title | Node 374 (PreviewAny) | (absent; ComfyUI default) | "Video Preview" | Allowed |
| /nodes/8 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 375, "type": "MarkdownNote", "pos": [-1820, 5080], "size": [480, 360], "flags": {}, "order": 8, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nGenerate a MiniMax H3 video from a written description.\n\n### How to Use\n\n1. In **Text to Video (MiniMax H3)**, describe the scene, movement, and sound. Set **Seconds** and choose an **Image Size (Ratio and Megapixels)**.\n2. Leave **Seed** as saved for a first run. **Turbo** selects a faster generation path. Turn off **Prompt Enhance** if you want to use your wording or if Ollama is unavailable.\n3. Click **Run**. Watch **Generation Preview** and find `MiniMax_H3` files in `ComfyUI/output/video/`."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 374 | 375 | Allowed |

## Qwen Image 2.1 Edit.json

Result: **PASS** — 31 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Qwen Image 2.1 Edit.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: 943.

Original SHA-256: `3168085c991af4f1724f787edb1cba985eac1215469302a0222a592dad4ea766`

Modified SHA-256: `a8fcc350ab1c9ac2435864ddb29fc273ae143aad424fd7560bd9eceb3b91a359`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 59 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/color | Group 60 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/0/groups/2/color | Group 61 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/3/color | Group 62 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/4/color | Group 63 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/5/color | Group 68 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/10/bgcolor | Node 875 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/10/color | Node 875 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/10/title | Node 875 (PrimitiveStringMultiline) | "Text (System Prompt)" | "System Prompt" | Allowed |
| /definitions/subgraphs/0/nodes/11/bgcolor | Node 876 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/11/color | Node 876 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/0/nodes/11/title | Node 876 (PreviewAny) | (absent; ComfyUI default) | "Prompt Preview" | Allowed |
| /definitions/subgraphs/0/nodes/15/title | Node 900 (ComfySwitchNode) | "Lora Switch" | "LoRA Switch" | Allowed |
| /definitions/subgraphs/0/nodes/17/title | Node 924 (ComfySwitchNode) | "Turbo?" | "Use Turbo" | Allowed |
| /definitions/subgraphs/0/nodes/24/bgcolor | Node 937 (PrimitiveBoolean) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/24/color | Node 937 (PrimitiveBoolean) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/24/title | Node 937 (PrimitiveBoolean) | "Turbo?" | "Use Turbo" | Allowed |
| /definitions/subgraphs/0/nodes/25/title | Node 938 (ComfySwitchNode) | "Turbo?" | "Use Turbo" | Allowed |
| /nodes/0/bgcolor | Node 932 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/0/color | Node 932 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/0/title | Node 932 (LoadImage) | (absent; ComfyUI default) | "Reference Image" | Allowed |
| /nodes/1/bgcolor | Node 933 (965076d7-0373-4029-b900-c9cd668f3b6f) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/1/color | Node 933 (965076d7-0373-4029-b900-c9cd668f3b6f) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/2/bgcolor | Node 934 (SeedNode) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 934 (SeedNode) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/2/title | Node 934 (SeedNode) | (absent; ComfyUI default) | "Seed" | Allowed |
| /nodes/3/bgcolor | Node 939 (SaveImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/3/color | Node 939 (SaveImage) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/3/title | Node 939 (SaveImage) | (absent; ComfyUI default) | "Save Image" | Allowed |
| /nodes/5 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 943, "type": "MarkdownNote", "pos": [1660, 1520], "size": [480, 360], "flags": {}, "order": 5, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nEdit an image with a written instruction while using the original as a reference.\n\n### How to Use\n\n1. Load the original in **Reference Image**.\n2. In **Qwen Image 2.1 Edit**, use **positive_prompt** to say what to change and what to keep. Leave the saved size for a first run. Use **custom_size** if you need a specific width and height.\n3. Click **Run**. **Save Image** writes the edited image to `ComfyUI/output/`."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 942 | 943 | Allowed |

## Qwen Image 2.1 Multi Angle.json

Result: **PASS** — 44 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Qwen Image 2.1 Multi Angle.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: 950.

Original SHA-256: `d7e0103c7f1c9ec8ef8e57b16dcaca574539384cbfa915a30d49df9b43952ee8`

Modified SHA-256: `c72f5bb07c2a09da38d67e343980dde3e32ff74328a45dfb49ed49fe24b07d98`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 59 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/color | Group 60 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/0/groups/2/color | Group 61 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/3/color | Group 62 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/4/color | Group 63 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/5/color | Group 68 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/10/bgcolor | Node 875 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/10/color | Node 875 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/10/title | Node 875 (PrimitiveStringMultiline) | "Text (System Prompt)" | "System Prompt" | Allowed |
| /definitions/subgraphs/0/nodes/11/bgcolor | Node 876 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/11/color | Node 876 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/0/nodes/11/title | Node 876 (PreviewAny) | (absent; ComfyUI default) | "Prompt Preview" | Allowed |
| /definitions/subgraphs/0/nodes/15/title | Node 900 (ComfySwitchNode) | "Lora Switch" | "LoRA Switch" | Allowed |
| /definitions/subgraphs/0/nodes/17/title | Node 924 (ComfySwitchNode) | "Turbo?" | "Use Turbo" | Allowed |
| /definitions/subgraphs/0/nodes/24/bgcolor | Node 937 (PrimitiveBoolean) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/24/color | Node 937 (PrimitiveBoolean) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/24/title | Node 937 (PrimitiveBoolean) | "Turbo?" | "Use Turbo" | Allowed |
| /definitions/subgraphs/0/nodes/25/title | Node 938 (ComfySwitchNode) | "Turbo?" | "Use Turbo" | Allowed |
| /nodes/0/bgcolor | Node 157 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /nodes/0/color | Node 157 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /nodes/0/title | Node 157 (MarkdownNote) | "KSampler settings" | "KSampler Settings" | Allowed |
| /nodes/0/widgets_values/0 | Note 157 | "You can test and find the best setting by yourself. The following table is for reference.\n\|   \| Qwen \| Comfy \|\n\|--------\|---------\|------------\|\n\| Steps  \| 40      \| 20         \|\n\| CFG    \| 4.0     \| 4.0       \|\n\n" | "Start with the saved settings. If you adjust sampling later, use this table to compare step counts and prompt guidance (CFG).\n\|   \| Qwen \| Comfy \|\n\|--------\|---------\|------------\|\n\| Steps  \| 40      \| 20         \|\n\| CFG    \| 4.0     \| 4.0       \|\n\n" | Allowed |
| /nodes/0/widgets_values_named/text | Note 157 | "You can test and find the best setting by yourself. The following table is for reference.\n\|   \| Qwen \| Comfy \|\n\|--------\|---------\|------------\|\n\| Steps  \| 40      \| 20         \|\n\| CFG    \| 4.0     \| 4.0       \|\n\n" | "Start with the saved settings. If you adjust sampling later, use this table to compare step counts and prompt guidance (CFG).\n\|   \| Qwen \| Comfy \|\n\|--------\|---------\|------------\|\n\| Steps  \| 40      \| 20         \|\n\| CFG    \| 4.0     \| 4.0       \|\n\n" | Allowed |
| /nodes/1/bgcolor | Node 9 (SaveImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/1/color | Node 9 (SaveImage) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/1/title | Node 9 (SaveImage) | (absent; ComfyUI default) | "Save Image" | Allowed |
| /nodes/2/bgcolor | Node 41 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 41 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/2/title | Node 41 (LoadImage) | (absent; ComfyUI default) | "Reference Image" | Allowed |
| /nodes/3/bgcolor | Node 175 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/3/color | Node 175 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/4/bgcolor | Node 943 (d7fa1d10-8749-46ff-bd56-d348dcb386f9) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/4/color | Node 943 (d7fa1d10-8749-46ff-bd56-d348dcb386f9) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/4/title | Node 943 (d7fa1d10-8749-46ff-bd56-d348dcb386f9) | (absent; ComfyUI default) | "Qwen Image 2.1 Multi Angle" | Allowed |
| /nodes/6/bgcolor | Node 946 (CameraAngle) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/6/color | Node 946 (CameraAngle) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/6/title | Node 946 (CameraAngle) | (absent; ComfyUI default) | "Camera Angle" | Allowed |
| /nodes/7/bgcolor | Node 949 (MarkdownNote) | "#653" | "#30343B" | Allowed |
| /nodes/7/color | Node 949 (MarkdownNote) | "#432" | "#35414A" | Allowed |
| /nodes/7/title | Node 949 (MarkdownNote) | (absent; ComfyUI default) | "Camera Angle Requirement" | Allowed |
| /nodes/7/widgets_values/0 | Note 949 | "Camera angle prompt requires Node 2.0\n" | "The camera-angle prompt requires Node 2.0." | Allowed |
| /nodes/7/widgets_values_named/text | Note 949 | "Camera angle prompt requires Node 2.0\n" | "The camera-angle prompt requires Node 2.0." | Allowed |
| /nodes/8 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 950, "type": "MarkdownNote", "pos": [-1400, -380], "size": [480, 360], "flags": {}, "order": 8, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nMake a new view of a reference image by changing the camera angle and zoom.\n\n### How to Use\n\n1. Load a picture in **Reference Image**.\n2. Set the horizontal angle, vertical angle, and zoom in **Camera Angle**. **Prompt Preview** shows the instruction built from those settings. The camera-angle prompt requires Node 2.0.\n3. Click **Run**. **Save Image** writes the new view under `ComfyUI/output/`."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 949 | 950 | Allowed |

## SeedVR2 Image Upscale.json

Result: **PASS** — 15 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:SeedVR2 Image Upscale.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: 77.

Original SHA-256: `9dcbef82f666cb0ba7cb028b6fb538db0bcaf8012c69df00b9db04ebe2940dca`

Modified SHA-256: `b21a14e34b2e4b0b98f2cbfc0f6a188334ba98ddaf90b9d691e09175e6faf922`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /nodes/0/bgcolor | Node 1 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/0/color | Node 1 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/0/title | Node 1 (LoadImage) | (absent; ComfyUI default) | "Reference Image" | Allowed |
| /nodes/1/bgcolor | Node 9 (SaveImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/1/color | Node 9 (SaveImage) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/1/title | Node 9 (SaveImage) | (absent; ComfyUI default) | "Save Image" | Allowed |
| /nodes/2/bgcolor | Node 66 (1970dcb4-982a-4c01-a373-4d239a3041e4) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 66 (1970dcb4-982a-4c01-a373-4d239a3041e4) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/2/title | Node 66 (1970dcb4-982a-4c01-a373-4d239a3041e4) | (absent; ComfyUI default) | "Upscale Image (SeedVR2 7B Int8)" | Allowed |
| /nodes/3/bgcolor | Node 76 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/3/color | Node 76 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/3/title | Node 76 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "Image Comparison" | Allowed |
| /nodes/4 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 77, "type": "MarkdownNote", "pos": [-360, -20], "size": [480, 360], "flags": {}, "order": 4, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nMake an image larger and compare it with the original.\n\n### How to Use\n\n1. Load the original in **Reference Image**.\n2. In **Upscale Image (SeedVR2 7B Int8)**, set **scale_multiplier**. A value of 2 doubles the width and height.\n3. Click **Run**. Check **Image Comparison** and find the enlarged image in `ComfyUI/output/seedvr2_after/`."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 76 | 77 | Allowed |

## SeedVR2 Video Upscale.json

Result: **PASS** — 18 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:SeedVR2 Video Upscale.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: none.

Original SHA-256: `9e5a218688e858279eb36e61c72f37863fd1f23af0e1bb41a8572ca47d14050c`

Modified SHA-256: `31507c7c61ef97dbd4cc697cf683735050699649694650535910712da82d80c2`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/17/bgcolor | Node 105 (PrimitiveBoolean) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/17/color | Node 105 (PrimitiveBoolean) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/17/title | Node 105 (PrimitiveBoolean) | "Boolean (Split Latent)" | "Split Latent" | Allowed |
| /nodes/0/bgcolor | Node 66 (1970dcb4-982a-4c01-a373-4d239a3041e4) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/0/color | Node 66 (1970dcb4-982a-4c01-a373-4d239a3041e4) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/0/title | Node 66 (1970dcb4-982a-4c01-a373-4d239a3041e4) | (absent; ComfyUI default) | "Upscale Video (SeedVR2 3B Int8)" | Allowed |
| /nodes/1/bgcolor | Node 73 (LoadVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/1/color | Node 73 (LoadVideo) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/1/title | Node 73 (LoadVideo) | (absent; ComfyUI default) | "Input Video" | Allowed |
| /nodes/2/bgcolor | Node 76 (SaveVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 76 (SaveVideo) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/2/title | Node 76 (SaveVideo) | (absent; ComfyUI default) | "Save Video" | Allowed |
| /nodes/3/bgcolor | Node 82 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /nodes/3/color | Node 82 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /nodes/3/title | Node 82 (MarkdownNote) | "Note: SeedVR2" | "Quick Start" | Allowed |
| /nodes/3/widgets_values/0 | Note 82 | "## SeedVR2\n\nOne-step video restoration / upscale (ICLR 2026). This workflow uses the **3B Int8** model for video upscaling.\n\n- Project: [SeedVR2](https://iceclear.github.io/projects/seedvr2/)\n- ComfyUI native support: [PR #14424](https://github.com/Comfy-Org/ComfyUI/pull/14424)\n\n### Subgraph parameters\n\n- **trim_video**: enable to cut a segment before upscaling\n- **trim_start_time / duration**: trim start (seconds) and length\n- **scale_multiplier**: upscale factor (default `2`)\n- **seed / sampler / scheduler / denoise**: sampling controls; `denoise=1` means full restore\n- **color_correction_method**: optional color match to original (default `none`)\n- **unet_name / vae_name**: model files to load\n\n### Tip: long videos\n\nIf the input is too long, turn on **trim_video**, upscale in shorter segments, then merge them. This helps avoid OOM / slowdowns on long clips.\n" | "### What It Does\n\nMake a video larger with SeedVR2. You can also process just a short segment.\n\n### How to Use\n\n1. Load the clip in **Input Video**.\n2. In **Upscale Video (SeedVR2 3B Int8)**, set **scale_multiplier**. A value of 2 doubles the width and height. To process only a segment, enable **trim_video** and set the start time and length in seconds.\n3. Click **Run**. **Save Video** writes `Upscaled_seedVR2` files under `ComfyUI/output/video/`.\n\n### Setup and Reference\n\nUses SeedVR2 3B Int8.\n\n- Project: [SeedVR2](https://iceclear.github.io/projects/seedvr2/)\n- ComfyUI native support: [PR #14424](https://github.com/Comfy-Org/ComfyUI/pull/14424)\n\n### Advanced Controls\n\n- **trim_video**: enable to cut a segment before upscaling\n- **trim_start_time / duration**: trim start (seconds) and length\n- **scale_multiplier**: upscale factor (default `2`)\n- **seed / sampler / scheduler / denoise**: sampling controls; `denoise=1` means full restore\n- **color_correction_method**: optional color match to original (default `none`)\n- **unet_name / vae_name**: model files to load\n\n### Tip: long videos\n\nIf the input is too long, turn on **trim_video**, upscale in shorter segments, then merge them. Shorter segments can reduce memory use and slowdowns." | Allowed |
| /nodes/3/widgets_values_named/text | Note 82 | "## SeedVR2\n\nOne-step video restoration / upscale (ICLR 2026). This workflow uses the **3B Int8** model for video upscaling.\n\n- Project: [SeedVR2](https://iceclear.github.io/projects/seedvr2/)\n- ComfyUI native support: [PR #14424](https://github.com/Comfy-Org/ComfyUI/pull/14424)\n\n### Subgraph parameters\n\n- **trim_video**: enable to cut a segment before upscaling\n- **trim_start_time / duration**: trim start (seconds) and length\n- **scale_multiplier**: upscale factor (default `2`)\n- **seed / sampler / scheduler / denoise**: sampling controls; `denoise=1` means full restore\n- **color_correction_method**: optional color match to original (default `none`)\n- **unet_name / vae_name**: model files to load\n\n### Tip: long videos\n\nIf the input is too long, turn on **trim_video**, upscale in shorter segments, then merge them. This helps avoid OOM / slowdowns on long clips.\n" | "### What It Does\n\nMake a video larger with SeedVR2. You can also process just a short segment.\n\n### How to Use\n\n1. Load the clip in **Input Video**.\n2. In **Upscale Video (SeedVR2 3B Int8)**, set **scale_multiplier**. A value of 2 doubles the width and height. To process only a segment, enable **trim_video** and set the start time and length in seconds.\n3. Click **Run**. **Save Video** writes `Upscaled_seedVR2` files under `ComfyUI/output/video/`.\n\n### Setup and Reference\n\nUses SeedVR2 3B Int8.\n\n- Project: [SeedVR2](https://iceclear.github.io/projects/seedvr2/)\n- ComfyUI native support: [PR #14424](https://github.com/Comfy-Org/ComfyUI/pull/14424)\n\n### Advanced Controls\n\n- **trim_video**: enable to cut a segment before upscaling\n- **trim_start_time / duration**: trim start (seconds) and length\n- **scale_multiplier**: upscale factor (default `2`)\n- **seed / sampler / scheduler / denoise**: sampling controls; `denoise=1` means full restore\n- **color_correction_method**: optional color match to original (default `none`)\n- **unet_name / vae_name**: model files to load\n\n### Tip: long videos\n\nIf the input is too long, turn on **trim_video**, upscale in shorter segments, then merge them. Shorter segments can reduce memory use and slowdowns." | Allowed |

## Song Gen v1.json

Result: **PASS** — 35 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Song Gen v1.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: 151.

Original SHA-256: `67f7255c93304847dcb038ae1e16890c2ad686b13aff4cc6860b3ebef4c8a54f`

Modified SHA-256: `f0b28773c9d8a6130c6671d373ebc8b90bd33da8d32d6f0d2a4a25c3e6959c8c`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/color | Group 2 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/0/groups/2/color | Group 3 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/5/bgcolor | Node 102 (PrimitiveNode) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/5/color | Node 102 (PrimitiveNode) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/5/title | Node 102 (PrimitiveNode) | "seed" | "Seed" | Allowed |
| /definitions/subgraphs/0/nodes/6/bgcolor | Node 99 (PrimitiveNode) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/6/color | Node 99 (PrimitiveNode) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/8/bgcolor | Node 127 (37579d01-e9be-4ab7-925f-14a3427a4beb) | "#353" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/8/color | Node 127 (37579d01-e9be-4ab7-925f-14a3427a4beb) | "#232" | "#35414A" | Allowed |
| /definitions/subgraphs/1/nodes/0/bgcolor | Node 111 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/0/color | Node 111 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/1/nodes/1/bgcolor | Node 123 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/1/color | Node 123 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/1/nodes/3/bgcolor | Node 137 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/3/color | Node 137 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/1/nodes/3/title | Node 137 (PreviewAny) | "TimeSig" | "Time Signature" | Allowed |
| /definitions/subgraphs/1/nodes/4/bgcolor | Node 113 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/4/color | Node 113 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/1/nodes/10/bgcolor | Node 121 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/10/color | Node 121 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/1/nodes/11/bgcolor | Node 120 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/11/color | Node 120 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/0/bgcolor | Node 139 (PreviewAny) | "#533" | "#30343B" | Allowed |
| /nodes/0/color | Node 139 (PreviewAny) | "#322" | "#594A72" | Allowed |
| /nodes/1/bgcolor | Node 140 (PreviewAny) | "#533" | "#30343B" | Allowed |
| /nodes/1/color | Node 140 (PreviewAny) | "#322" | "#594A72" | Allowed |
| /nodes/2/bgcolor | Node 142 (3ee53d33-cefe-4d1e-aa9b-e92ece4a0559) | "#353" | "#30343B" | Allowed |
| /nodes/2/color | Node 142 (3ee53d33-cefe-4d1e-aa9b-e92ece4a0559) | "#232" | "#715B2D" | Allowed |
| /nodes/2/title | Node 142 (3ee53d33-cefe-4d1e-aa9b-e92ece4a0559) | (absent; ComfyUI default) | "Generate Song" | Allowed |
| /nodes/3/bgcolor | Node 143 (SaveAudioAdvanced) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/3/color | Node 143 (SaveAudioAdvanced) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/3/title | Node 143 (SaveAudioAdvanced) | (absent; ComfyUI default) | "Save Audio" | Allowed |
| /nodes/4 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 151, "type": "MarkdownNote", "pos": [-100, 4740], "size": [480, 360], "flags": {}, "order": 4, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nTurn a song idea into audio with ACE-Step. Ollama prepares the style and lyrics from your description.\n\n### How to Use\n\n1. Start Ollama with the model selected in the workflow.\n2. In **Generate Song**, describe the genre, mood, instruments, and topic. Start with **batch_size** set to 1.\n3. Click **Run**. Check **Style** and **Lyrics** for the text used to make the song. Find the audio in `ComfyUI/output/audio/`."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 150 | 151 | Allowed |

## Video Metadata.json

Result: **PASS** — 11 changed fields; 0 unauthorized changes.

Original: `53eeee7ba97a9d9cd0e62dcf8064785cec990a07:Video Metadata.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: 8.

Original SHA-256: `0bdedb3fa971b553a221c7fb794165039c27e5bc120bc3abe7626053fc661e52`

Modified SHA-256: `d57864f80340c1dab63f5f5306593b904d07289c41797e51b2f7ef9a7b787150`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/nodes/2/title | Node 4 (ComfyMathExpression) | "Duration (frames / fps)" | "Video Duration (Seconds)" | Allowed |
| /definitions/subgraphs/0/nodes/3/title | Node 5 (StringFormat) | "Video metadata summary" | "Video Details Summary" | Allowed |
| /nodes/0/bgcolor | Node 2 (LoadVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/0/color | Node 2 (LoadVideo) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/0/title | Node 2 (LoadVideo) | (absent; ComfyUI default) | "Input Video" | Allowed |
| /nodes/1/title | Node 7 (53281abb-9f87-4d66-a6cc-9e979cf58034) | (absent; ComfyUI default) | "Video Metadata" | Allowed |
| /nodes/2/bgcolor | Node 6 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 6 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/2/title | Node 6 (PreviewAny) | "Video metadata" | "Video Details" | Allowed |
| /nodes/3 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 8, "type": "MarkdownNote", "pos": [-440, 80], "size": [480, 360], "flags": {}, "order": 3, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nRead a video’s dimensions, frame rate, frame count, duration, bit depth, and color space.\n\n### How to Use\n\n1. Load a file in **Input Video** and click **Run**.\n2. Read the result in **Video Details**. The workflow displays information on the canvas and leaves your video file as it is."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 7 | 8 | Allowed |
