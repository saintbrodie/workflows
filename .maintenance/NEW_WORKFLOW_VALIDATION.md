# Workflow Presentation Validation

This comparison checks JSON structure and unchanged saved data. It does not prove runtime functionality or visual quality.

Visual inspection is a separate user review. No workflow execution was performed by this validator.

## Image Edit Arena.json

Result: **PASS** — 153 changed fields; 0 unauthorized changes.

Original: `8e97d16:Image Edit Arena.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: disabled.

Instructional note addition allowance: 898.

Original SHA-256: `236a3c96ed6a3b08df45471a0dd460633a0348dc066faed19390a6e18578e533`

Modified SHA-256: `825b5f90ee9c49d5016514d13920bdc8423538e110557b51fef02b9d2f0c4db7`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 17 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/color | Group 18 | "#3f789e" | "#235B74" | Allowed |
| /definitions/subgraphs/0/groups/2/color | Group 19 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/11/bgcolor | Node 74 (CLIPTextEncode) | "#353" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/11/color | Node 74 (CLIPTextEncode) | "#232" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/11/title | Node 74 (CLIPTextEncode) | "CLIP Text Encode (Positive Prompt)" | "Positive Prompt" | Allowed |
| /definitions/subgraphs/1/groups/0/color | Group 34 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/1/groups/1/color | Group 35 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/1/groups/2/color | Group 36 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/1/groups/3/color | Group 37 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/1/groups/4/color | Group 38 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/1/nodes/9/title | Node 479 (PrimitiveStringMultiline) | "Text (System Prompt)" | "System Prompt" | Allowed |
| /definitions/subgraphs/1/nodes/10/bgcolor | Node 480 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/10/color | Node 480 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/1/nodes/10/title | Node 480 (PreviewAny) | (absent; ComfyUI default) | "Preview" | Allowed |
| /definitions/subgraphs/2/groups/0/color | Group 39 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/2/groups/1/color | Group 40 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/2/groups/2/color | Group 5 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/2/groups/3/color | Group 6 | "#444" | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/3/bgcolor | Node 4 (TextEncodeFibo2) | "#533" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/3/color | Node 4 (TextEncodeFibo2) | "#322" | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/6/bgcolor | Node 25 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/6/color | Node 25 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/2/nodes/6/title | Node 25 (PreviewAny) | (absent; ComfyUI default) | "Preview" | Allowed |
| /definitions/subgraphs/2/nodes/7/bgcolor | Node 26 (BatchImagesNode) | "#533" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/7/color | Node 26 (BatchImagesNode) | "#322" | "#35414A" | Allowed |
| /definitions/subgraphs/2/nodes/9/title | Node 12 (PrimitiveStringMultiline) | "String (System Prompt VGL)" | "System Prompt (VGL)" | Allowed |
| /definitions/subgraphs/2/nodes/11/bgcolor | Node 791 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /definitions/subgraphs/2/nodes/11/color | Node 791 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /definitions/subgraphs/3/groups/0/color | Group 41 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/3/groups/1/color | Group 42 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/3/groups/2/color | Group 43 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/3/groups/3/color | Group 44 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/3/groups/4/color | Group 45 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/3/nodes/10/title | Node 802 (PrimitiveStringMultiline) | "Text (System Prompt)" | "System Prompt" | Allowed |
| /definitions/subgraphs/3/nodes/11/bgcolor | Node 803 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/3/nodes/11/color | Node 803 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/3/nodes/11/title | Node 803 (PreviewAny) | (absent; ComfyUI default) | "Preview" | Allowed |
| /definitions/subgraphs/4/groups/0/color | Group 50 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/4/groups/1/color | Group 51 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/4/groups/2/color | Group 52 | "#444" | "#D2B16F" | Allowed |
| /definitions/subgraphs/4/groups/3/color | Group 53 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/4/nodes/2/bgcolor | Node 830 (TextEncodeMOSSImageEdit) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/4/nodes/2/color | Node 830 (TextEncodeMOSSImageEdit) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/4/nodes/3/bgcolor | Node 831 (TextEncodeMOSSImageEdit) | "#353" | "#30343B" | Allowed |
| /definitions/subgraphs/4/nodes/3/color | Node 831 (TextEncodeMOSSImageEdit) | "#232" | "#35414A" | Allowed |
| /definitions/subgraphs/5/groups/0/color | Group 54 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/5/groups/1/color | Group 55 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/5/groups/2/color | Group 56 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/5/groups/3/color | Group 57 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/5/groups/4/color | Group 58 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/5/nodes/9/title | Node 854 (PrimitiveStringMultiline) | "Text (System Prompt)" | "System Prompt" | Allowed |
| /definitions/subgraphs/5/nodes/10/bgcolor | Node 855 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/5/nodes/10/color | Node 855 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/5/nodes/10/title | Node 855 (PreviewAny) | (absent; ComfyUI default) | "Preview" | Allowed |
| /definitions/subgraphs/6/groups/0/color | Group 59 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/6/groups/1/color | Group 60 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/6/groups/2/color | Group 61 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/6/groups/3/color | Group 62 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/6/groups/4/color | Group 63 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/6/nodes/10/title | Node 875 (PrimitiveStringMultiline) | "Text (System Prompt)" | "System Prompt" | Allowed |
| /definitions/subgraphs/6/nodes/11/bgcolor | Node 876 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/6/nodes/11/color | Node 876 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/6/nodes/11/title | Node 876 (PreviewAny) | (absent; ComfyUI default) | "Preview" | Allowed |
| /definitions/subgraphs/7/groups/0/color | Group 2 | "#8A8" | "#235B74" | Allowed |
| /definitions/subgraphs/7/groups/1/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/7/groups/2/color | Group 3 | "#a1309b" | "#235B74" | Allowed |
| /definitions/subgraphs/7/groups/3/color | Group 4 | "#b58b2a" | "#235B74" | Allowed |
| /definitions/subgraphs/7/groups/4/color | Group 66 | "#c15f3c" | "#D2B16F" | Allowed |
| /definitions/subgraphs/7/groups/5/color | Group 67 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/7/nodes/1/bgcolor | Node 106 (Note) | "#353" | "#30343B" | Allowed |
| /definitions/subgraphs/7/nodes/1/color | Node 106 (Note) | "#232" | "#35414A" | Allowed |
| /definitions/subgraphs/7/nodes/7/bgcolor | Node 90 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/7/nodes/7/color | Node 90 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /definitions/subgraphs/7/nodes/8/bgcolor | Node 100 (Note) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/7/nodes/8/color | Node 100 (Note) | "#432" | "#35414A" | Allowed |
| /definitions/subgraphs/7/nodes/9/bgcolor | Node 101 (Note) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/7/nodes/9/color | Node 101 (Note) | "#432" | "#35414A" | Allowed |
| /definitions/subgraphs/7/nodes/10/bgcolor | Node 107 (Note) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/7/nodes/10/color | Node 107 (Note) | "#432" | "#35414A" | Allowed |
| /definitions/subgraphs/7/nodes/14/bgcolor | Node 103 (Note) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/7/nodes/14/color | Node 103 (Note) | "#432" | "#35414A" | Allowed |
| /definitions/subgraphs/7/nodes/15/bgcolor | Node 102 (Note) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/7/nodes/15/color | Node 102 (Note) | "#432" | "#35414A" | Allowed |
| /definitions/subgraphs/7/nodes/17/bgcolor | Node 104 (Note) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/7/nodes/17/color | Node 104 (Note) | "#432" | "#35414A" | Allowed |
| /definitions/subgraphs/7/nodes/19/bgcolor | Node 105 (Note) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/7/nodes/19/color | Node 105 (Note) | "#432" | "#35414A" | Allowed |
| /groups/0/color | Group 64 | "#3f789e" | "#35414A" | Allowed |
| /groups/1/color | Group 65 | "#3f789e" | "#35414A" | Allowed |
| /nodes/0/bgcolor | Node 8 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/0/color | Node 8 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/0/title | Node 8 (LoadImage) | (absent; ComfyUI default) | "Reference Image" | Allowed |
| /nodes/1/bgcolor | Node 41 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/1/color | Node 41 (PrimitiveStringMultiline) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/2/bgcolor | Node 42 (PrimitiveFloat) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 42 (PrimitiveFloat) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/2/title | Node 42 (PrimitiveFloat) | "megapixels" | "Resolution (Megapixels)" | Allowed |
| /nodes/3/bgcolor | Node 787 (1aaba576-0186-451e-b125-fc5280f3e20c) | "#3f5159" | "#30343B" | Allowed |
| /nodes/3/color | Node 787 (1aaba576-0186-451e-b125-fc5280f3e20c) | "#2a363b" | "#715B2D" | Allowed |
| /nodes/3/title | Node 787 (1aaba576-0186-451e-b125-fc5280f3e20c) | (absent; ComfyUI default) | "Image Edit (FLUX.2 Klein 9B Distilled)" | Allowed |
| /nodes/4/bgcolor | Node 788 (SeedNode) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/4/color | Node 788 (SeedNode) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/4/title | Node 788 (SeedNode) | (absent; ComfyUI default) | "Seed" | Allowed |
| /nodes/5/bgcolor | Node 789 (7a0e755e-a4b3-4dcc-b62f-f784c7c4b57e) | "#535" | "#30343B" | Allowed |
| /nodes/5/color | Node 789 (7a0e755e-a4b3-4dcc-b62f-f784c7c4b57e) | "#323" | "#715B2D" | Allowed |
| /nodes/6/bgcolor | Node 792 (5bc45cfb-735c-468d-ba12-fc6058c819ef) | "#653" | "#30343B" | Allowed |
| /nodes/6/color | Node 792 (5bc45cfb-735c-468d-ba12-fc6058c819ef) | "#432" | "#715B2D" | Allowed |
| /nodes/7/bgcolor | Node 807 (f42b8c78-4269-4c93-af27-385ebc1e7406) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/7/color | Node 807 (f42b8c78-4269-4c93-af27-385ebc1e7406) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/9/bgcolor | Node 810 (PreviewImage) | "#353" | "#30343B" | Allowed |
| /nodes/9/color | Node 810 (PreviewImage) | "#232" | "#594A72" | Allowed |
| /nodes/9/title | Node 810 (PreviewImage) | "Moss Image" | "Moss Image Preview" | Allowed |
| /nodes/10/bgcolor | Node 811 (PreviewImage) | "#3f5159" | "#30343B" | Allowed |
| /nodes/10/color | Node 811 (PreviewImage) | "#2a363b" | "#594A72" | Allowed |
| /nodes/10/title | Node 811 (PreviewImage) | "Klein Image" | "Klein Image Preview" | Allowed |
| /nodes/11/bgcolor | Node 812 (PreviewImage) | "#535" | "#30343B" | Allowed |
| /nodes/11/color | Node 812 (PreviewImage) | "#323" | "#594A72" | Allowed |
| /nodes/11/title | Node 812 (PreviewImage) | "Qwen 2.1 Turbo Image" | "Qwen 2.1 Turbo Image Preview" | Allowed |
| /nodes/12/bgcolor | Node 813 (PreviewImage) | "#653" | "#30343B" | Allowed |
| /nodes/12/color | Node 813 (PreviewImage) | "#432" | "#594A72" | Allowed |
| /nodes/12/title | Node 813 (PreviewImage) | "Fibo2 Image" | "Fibo2 Image Preview" | Allowed |
| /nodes/13/bgcolor | Node 814 (PreviewImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/13/color | Node 814 (PreviewImage) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/13/title | Node 814 (PreviewImage) | "Qwen 2.1 Image" | "Qwen 2.1 Image Preview" | Allowed |
| /nodes/14/bgcolor | Node 840 (3c6cc534-2c19-4f16-aa64-87eb3ef87cc5) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/14/color | Node 840 (3c6cc534-2c19-4f16-aa64-87eb3ef87cc5) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/16/bgcolor | Node 843 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/16/color | Node 843 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/16/title | Node 843 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "Image Comparison" | Allowed |
| /nodes/18/bgcolor | Node 880 (55691f74-b079-4912-9345-425e666a7827) | "#535" | "#30343B" | Allowed |
| /nodes/18/color | Node 880 (55691f74-b079-4912-9345-425e666a7827) | "#323" | "#715B2D" | Allowed |
| /nodes/19/bgcolor | Node 881 (PreviewImage) | "#535" | "#30343B" | Allowed |
| /nodes/19/color | Node 881 (PreviewImage) | "#323" | "#594A72" | Allowed |
| /nodes/19/title | Node 881 (PreviewImage) | "Qwen 2.1 Turbo Image" | "Qwen 2.1 Turbo Image Preview" | Allowed |
| /nodes/20/bgcolor | Node 882 (a08d596d-845c-4d30-927d-f49f1c87b1a7) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/20/color | Node 882 (a08d596d-845c-4d30-927d-f49f1c87b1a7) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/22/bgcolor | Node 884 (PreviewImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/22/color | Node 884 (PreviewImage) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/22/title | Node 884 (PreviewImage) | "Qwen 2.1 Image" | "Qwen 2.1 Image Preview" | Allowed |
| /nodes/24/bgcolor | Node 886 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/24/color | Node 886 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/24/title | Node 886 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "Image Comparison" | Allowed |
| /nodes/25/bgcolor | Node 889 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/25/color | Node 889 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/25/title | Node 889 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "Image Comparison" | Allowed |
| /nodes/28/bgcolor | Node 896 (1cae195d-1cf7-4206-bdb5-524ef894e6cb) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/28/color | Node 896 (1cae195d-1cf7-4206-bdb5-524ef894e6cb) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/29/bgcolor | Node 897 (PreviewImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/29/color | Node 897 (PreviewImage) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/29/title | Node 897 (PreviewImage) | "Krea2 Edit image" | "Krea-2 Edit Preview" | Allowed |
| /nodes/30 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 898, "type": "MarkdownNote", "pos": [360, -640], "size": [480, 360], "flags": {}, "order": 30, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nCompare how several image models apply the same edit to one reference image.\n\n### How to Use\n\n1. Load the original in **Reference Image**. In **Positive Prompt**, say what to change and what to keep.\n2. Start with the saved **Resolution (Megapixels)** and **Seed**. Click **Run** to generate results from the connected models.\n3. Check the named preview cards or drag the sliders in **Image Comparison**. This workflow previews results on the canvas."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 897 | 898 | Allowed |

## InfiniteTalk Lip Sync.json

Result: **PASS** — 75 changed fields; 0 unauthorized changes.

Original: `8e97d16:InfiniteTalk Lip Sync.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: disabled.

Instructional note addition allowance: 318.

Original SHA-256: `810e5a8fe20e719be515ca6b0d5e5a17f99d1382bf335899ceb0b82510fb20e4`

Modified SHA-256: `9cd4267a0e26ec1305a4d1b8ca3c8ad74a8609af1e8513756308cf8e0a46eb11`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 1 | "#88A" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/color | Group 3 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/title | Group 3 | "Video2video" | "Video to Video" | Allowed |
| /definitions/subgraphs/0/groups/2/color | Group 4 | "#a1309b" | "#235B74" | Allowed |
| /definitions/subgraphs/0/nodes/0/bgcolor | Node 239 (MarkdownNote) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/0/color | Node 239 (MarkdownNote) | "#432" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/0/title | Node 239 (MarkdownNote) | "Model links" | "Model Links" | Allowed |
| /definitions/subgraphs/0/nodes/4/bgcolor | Node 238 (CLIPVisionLoader) | "#355" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/4/color | Node 238 (CLIPVisionLoader) | "#233" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/9/bgcolor | Node 245 (INTConstant) | "#29699c" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/9/color | Node 245 (INTConstant) | "#1b4669" | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/9/title | Node 245 (INTConstant) | "Width" | "Width (Pixels)" | Allowed |
| /definitions/subgraphs/0/nodes/10/bgcolor | Node 246 (INTConstant) | "#29699c" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/10/color | Node 246 (INTConstant) | "#1b4669" | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/10/title | Node 246 (INTConstant) | "Height" | "Height (Pixels)" | Allowed |
| /definitions/subgraphs/0/nodes/14/bgcolor | Node 237 (WanVideoClipVisionEncode) | "#355" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/14/color | Node 237 (WanVideoClipVisionEncode) | "#233" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/16/bgcolor | Node 270 (INTConstant) | "#29699c" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/16/color | Node 270 (INTConstant) | "#1b4669" | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/16/title | Node 270 (INTConstant) | "Max frames" | "Maximum Frames" | Allowed |
| /definitions/subgraphs/0/nodes/19/bgcolor | Node 130 (WanVideoDecode) | "#533" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/19/color | Node 130 (WanVideoDecode) | "#322" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/25/bgcolor | Node 293 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/25/color | Node 293 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/0/nodes/25/title | Node 293 (PreviewAny) | (absent; ComfyUI default) | "Preview" | Allowed |
| /definitions/subgraphs/0/nodes/27/bgcolor | Node 194 (MultiTalkWav2VecEmbeds) | "#535" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/27/color | Node 194 (MultiTalkWav2VecEmbeds) | "#323" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/30/bgcolor | Node 302 (MarkdownNote) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/30/color | Node 302 (MarkdownNote) | "#432" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/30/title | Node 302 (MarkdownNote) | "Wav2vec2 safetensors" | "Vocal Separation Model" | Allowed |
| /definitions/subgraphs/0/nodes/32/bgcolor | Node 305 (MarkdownNote) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/32/color | Node 305 (MarkdownNote) | "#432" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/32/title | Node 305 (MarkdownNote) | "Wav2vec2 safetensors" | "Wav2Vec2 Model Files" | Allowed |
| /definitions/subgraphs/0/nodes/33/bgcolor | Node 120 (MultiTalkModelLoader) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/33/color | Node 120 (MultiTalkModelLoader) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/35/bgcolor | Node 129 (WanVideoVAELoader) | "#533" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/35/color | Node 129 (WanVideoVAELoader) | "#322" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/36/bgcolor | Node 122 (WanVideoModelLoader) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/36/color | Node 122 (WanVideoModelLoader) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/38/bgcolor | Node 192 (WanVideoImageToVideoMultiTalk) | "#533" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/38/color | Node 192 (WanVideoImageToVideoMultiTalk) | "#322" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/39/bgcolor | Node 138 (WanVideoLoraSelect) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/39/color | Node 138 (WanVideoLoraSelect) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/40/bgcolor | Node 134 (WanVideoBlockSwap) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/40/color | Node 134 (WanVideoBlockSwap) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/41/bgcolor | Node 177 (WanVideoTorchCompileSettings) | "#335" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/41/color | Node 177 (WanVideoTorchCompileSettings) | "#223" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/48/bgcolor | Node 241 (WanVideoTextEncodeCached) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/48/color | Node 241 (WanVideoTextEncodeCached) | "#432" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/49/bgcolor | Node 234 (Note) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/49/color | Node 234 (Note) | "#432" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/50/bgcolor | Node 263 (Note) | "#653" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/50/color | Node 263 (Note) | "#432" | "#35414A" | Allowed |
| /groups/0/color | Group 5 | "#3f789e" | "#D2B16F" | Allowed |
| /groups/0/title | Group 5 | "Trim" | "Optional Trimming" | Allowed |
| /nodes/0/bgcolor | Node 125 (LoadAudio) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/0/color | Node 125 (LoadAudio) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/0/title | Node 125 (LoadAudio) | (absent; ComfyUI default) | "Input Audio" | Allowed |
| /nodes/1/bgcolor | Node 314 (4edf8a39-6846-49b6-929a-d324d86cf7e8) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/1/color | Node 314 (4edf8a39-6846-49b6-929a-d324d86cf7e8) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/1/title | Node 314 (4edf8a39-6846-49b6-929a-d324d86cf7e8) | (absent; ComfyUI default) | "Lip Sync (InfiniteTalk)" | Allowed |
| /nodes/2/bgcolor | Node 312 (SaveVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 312 (SaveVideo) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/2/title | Node 312 (SaveVideo) | (absent; ComfyUI default) | "Save Video" | Allowed |
| /nodes/5/bgcolor | Node 317 (PrimitiveFloat) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/5/color | Node 317 (PrimitiveFloat) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/5/title | Node 317 (PrimitiveFloat) | "Length" | "Trim Duration (Seconds)" | Allowed |
| /nodes/6/bgcolor | Node 315 (Note) | "#653" | "#30343B" | Allowed |
| /nodes/6/color | Node 315 (Note) | "#432" | "#35414A" | Allowed |
| /nodes/6/title | Node 315 (Note) | (absent; ComfyUI default) | "Lip Sync Tips" | Allowed |
| /nodes/7/bgcolor | Node 309 (LoadVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/7/color | Node 309 (LoadVideo) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/7/title | Node 309 (LoadVideo) | (absent; ComfyUI default) | "Input Video" | Allowed |
| /nodes/8 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 318, "type": "MarkdownNote", "pos": [-840, -1480], "size": [480, 360], "flags": {}, "order": 8, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nMake the speaker in a video move their lips to match a new audio track.\n\n### How to Use\n\n1. Load the clip in **Input Video** and the speech track in **Input Audio**.\n2. Set the aspect ratio in **Lip Sync (InfiniteTalk)** to match your video. Start with the saved settings. Raise **audio_scale** if you need a stronger effect.\n3. Click **Run**. **Save Video** writes files with the `InfiniteTalk` prefix under `ComfyUI/output/`.\n\n### Setup and Notes\n\nIf the audio runs longer than the clip, the result extends from the last video frame. See **Model Links** inside the lip-sync node for setup."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 317 | 318 | Allowed |

## Klein Inpaint.json

Result: **PASS** — 28 changed fields; 0 unauthorized changes.

Original: `8e97d16:Klein Inpaint.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: enabled.

Instructional note addition allowance: none.

Original SHA-256: `e5fe55b411591bc302506517001afcfa49010fa9228bd4d91cd7ac606c0104ce`

Modified SHA-256: `5bca89653a4047c1791b183ab42943387236fba701e1af8f39b19df7a8dd6f43`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 5 | "#957646" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/0/title | Group 5 | "02  SCALE + MASK PREPARATION" | "02 · Scale and Prepare Mask" | Allowed |
| /definitions/subgraphs/0/groups/1/color | Group 6 | "#52745e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/title | Group 6 | "03  PROMPT + SAMPLER" | "03 · Prompt and Sampling" | Allowed |
| /definitions/subgraphs/0/groups/2/color | Group 4 | "#6b5580" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/2/title | Group 4 | "04  OUTPUT" | "04 · Render Result" | Allowed |
| /definitions/subgraphs/0/nodes/5/bgcolor | Node 7 (CLIPTextEncode) | "#314d3c" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/5/color | Node 7 (CLIPTextEncode) | "#24372e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/6/bgcolor | Node 8 (CLIPTextEncode) | "#533" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/6/color | Node 8 (CLIPTextEncode) | "#322" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/21/bgcolor | Node 27 (RandomNoise) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/21/color | Node 27 (RandomNoise) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/0/bgcolor | Node 97 (MarkdownNote) | "#000" | "#30343B" | Allowed |
| /nodes/0/color | Node 97 (MarkdownNote) | "#222" | "#35414A" | Allowed |
| /nodes/0/title | Node 97 (MarkdownNote) | (absent; ComfyUI default) | "Quick Start" | Allowed |
| /nodes/0/widgets_values/0 | Note 97 | "Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)\n\n## Model links (for local users)\n\n**text_encoders**\n\n- [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors)\n\n**diffusion_models**\n\n- [lux-2-klein-base-4b-fp8.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4b-fp8/resolve/main/flux-2-klein-base-4b-fp8.safetensors)\n\n**vae**\n\n- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors)\n\n\nModel Storage Location\n\n```\n📂 ComfyUI/\n├── 📂 models/\n│   ├── 📂 text_encoders/\n│   │      └── qwen_3_4b.safetensors\n│   ├── 📂 diffusion_models/\n│   │      └── lux-2-klein-base-4b-fp8.safetensors\n│   └── 📂 vae/\n│          └── flux2-vae.safetensors\n```\n\n## Report issue\n\nNote: please update ComfyUI first ([guide](https://docs.comfy.org/zh-CN/installation/update_comfyui)) and prepare the required models. Desktop/Cloud ship stable builds; nightly-supported models may not be included yet, please wait for the next stable release.\n\n- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)\n- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)\n- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)\n\n" | "### What It Does\n\nReplace or repair a painted region of an image with FLUX.2 Klein.\n\n### How to Use\n\n1. Load the original in **Source Image + Paint Mask**. Open the image’s mask editor and paint the area you want to change.\n2. Describe what should appear in the painted area in **Inpaint Image (FLUX.2 Klein)**. Start with the saved settings.\n3. Click **Run**. Check **Image Comparison** and find the saved image under `ComfyUI/output/`.\n\n### Model Setup and Help\n\nGuide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)\n\n## Model links (for local users)\n\n**text_encoders**\n\n- [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors)\n\n**diffusion_models**\n\n- [lux-2-klein-base-4b-fp8.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4b-fp8/resolve/main/flux-2-klein-base-4b-fp8.safetensors)\n\n**vae**\n\n- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors)\n\n\nModel Storage Location\n\n```\n📂 ComfyUI/\n├── 📂 models/\n│   ├── 📂 text_encoders/\n│   │      └── qwen_3_4b.safetensors\n│   ├── 📂 diffusion_models/\n│   │      └── lux-2-klein-base-4b-fp8.safetensors\n│   └── 📂 vae/\n│          └── flux2-vae.safetensors\n```\n\n## Report issue\n\nNote: please update ComfyUI first ([guide](https://docs.comfy.org/zh-CN/installation/update_comfyui)) and prepare the required models. Desktop/Cloud ship stable builds; nightly-supported models may not be included yet, please wait for the next stable release.\n\n- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)\n- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)\n- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)\n\n" | Allowed |
| /nodes/0/widgets_values_named/text | Note 97 | "Guide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)\n\n## Model links (for local users)\n\n**text_encoders**\n\n- [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors)\n\n**diffusion_models**\n\n- [lux-2-klein-base-4b-fp8.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4b-fp8/resolve/main/flux-2-klein-base-4b-fp8.safetensors)\n\n**vae**\n\n- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors)\n\n\nModel Storage Location\n\n```\n📂 ComfyUI/\n├── 📂 models/\n│   ├── 📂 text_encoders/\n│   │      └── qwen_3_4b.safetensors\n│   ├── 📂 diffusion_models/\n│   │      └── lux-2-klein-base-4b-fp8.safetensors\n│   └── 📂 vae/\n│          └── flux2-vae.safetensors\n```\n\n## Report issue\n\nNote: please update ComfyUI first ([guide](https://docs.comfy.org/zh-CN/installation/update_comfyui)) and prepare the required models. Desktop/Cloud ship stable builds; nightly-supported models may not be included yet, please wait for the next stable release.\n\n- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)\n- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)\n- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)\n\n" | "### What It Does\n\nReplace or repair a painted region of an image with FLUX.2 Klein.\n\n### How to Use\n\n1. Load the original in **Source Image + Paint Mask**. Open the image’s mask editor and paint the area you want to change.\n2. Describe what should appear in the painted area in **Inpaint Image (FLUX.2 Klein)**. Start with the saved settings.\n3. Click **Run**. Check **Image Comparison** and find the saved image under `ComfyUI/output/`.\n\n### Model Setup and Help\n\nGuide: [Subgraph](https://docs.comfy.org/interface/features/subgraph)\n\n## Model links (for local users)\n\n**text_encoders**\n\n- [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors)\n\n**diffusion_models**\n\n- [lux-2-klein-base-4b-fp8.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-klein-base-4b-fp8/resolve/main/flux-2-klein-base-4b-fp8.safetensors)\n\n**vae**\n\n- [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors)\n\n\nModel Storage Location\n\n```\n📂 ComfyUI/\n├── 📂 models/\n│   ├── 📂 text_encoders/\n│   │      └── qwen_3_4b.safetensors\n│   ├── 📂 diffusion_models/\n│   │      └── lux-2-klein-base-4b-fp8.safetensors\n│   └── 📂 vae/\n│          └── flux2-vae.safetensors\n```\n\n## Report issue\n\nNote: please update ComfyUI first ([guide](https://docs.comfy.org/zh-CN/installation/update_comfyui)) and prepare the required models. Desktop/Cloud ship stable builds; nightly-supported models may not be included yet, please wait for the next stable release.\n\n- Cannot run / runtime errors: [ComfyUI/issues](https://github.com/comfyanonymous/ComfyUI/issues)\n- UI / frontend issues: [ComfyUI_frontend/issues](https://github.com/Comfy-Org/ComfyUI_frontend/issues)\n- Workflow issues: [workflow_templates/issues](https://github.com/Comfy-Org/workflow_templates/issues)\n\n" | Allowed |
| /nodes/1/bgcolor | Node 146 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/1/color | Node 146 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/2/bgcolor | Node 147 (38f1ecb7-317c-4f39-a118-8a1d0d947593) | "#353" | "#30343B" | Allowed |
| /nodes/2/color | Node 147 (38f1ecb7-317c-4f39-a118-8a1d0d947593) | "#232" | "#715B2D" | Allowed |
| /nodes/2/title | Node 147 (38f1ecb7-317c-4f39-a118-8a1d0d947593) | "Flux Klein Inpainting" | "Inpaint Image (FLUX.2 Klein)" | Allowed |
| /nodes/3/bgcolor | Node 148 (SaveImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/3/color | Node 148 (SaveImage) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/3/title | Node 148 (SaveImage) | "Save Native Klein Inpaint" | "Save Image" | Allowed |
| /nodes/4/bgcolor | Node 150 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/4/color | Node 150 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/4/title | Node 150 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "Image Comparison" | Allowed |

## Krea2 Character Creator.json

Result: **PASS** — 63 changed fields; 0 unauthorized changes.

Original: `8e97d16:Krea2 Character Creator.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: disabled.

Instructional note addition allowance: 497.

Original SHA-256: `e37763e85386e3340ddfadbfaf60b3cf5b3ed97d136848e1d6e57451ca0abea2`

Modified SHA-256: `7e252d3a2d090e20af6b1bb8dca5e289416fec3d0f59e936bdb4508c8899c212`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /definitions/subgraphs/0/groups/0/color | Group 1 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/color | Group 5 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/1/title | Group 5 | "Group" | "User Prompt" | Allowed |
| /definitions/subgraphs/0/groups/2/color | Group 6 | "#3f789e" | "#35414A" | Allowed |
| /definitions/subgraphs/0/groups/3/color | Group 7 | "#3f789e" | "#235B74" | Allowed |
| /definitions/subgraphs/0/groups/4/color | Group 8 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/0/groups/5/color | Group 9 | "#3f789e" | "#D2B16F" | Allowed |
| /definitions/subgraphs/0/nodes/2/bgcolor | Node 346 (PrimitiveStringMultiline) | "#533" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/2/color | Node 346 (PrimitiveStringMultiline) | "#322" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/3/bgcolor | Node 347 (CLIPTextEncode) | "#353" | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/3/color | Node 347 (CLIPTextEncode) | "#232" | "#35414A" | Allowed |
| /definitions/subgraphs/0/nodes/6/bgcolor | Node 350 (PrimitiveBoolean) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/6/color | Node 350 (PrimitiveBoolean) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /definitions/subgraphs/0/nodes/6/title | Node 350 (PrimitiveBoolean) | "Boolean (Enable LoRA?)" | "Use LoRA" | Allowed |
| /definitions/subgraphs/0/nodes/10/bgcolor | Node 377 (PreviewImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/0/nodes/10/color | Node 377 (PreviewImage) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/0/nodes/10/title | Node 377 (PreviewImage) | (absent; ComfyUI default) | "Image Preview" | Allowed |
| /definitions/subgraphs/1/nodes/0/bgcolor | Node 479 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/0/color | Node 479 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /definitions/subgraphs/1/nodes/4/bgcolor | Node 457 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /definitions/subgraphs/1/nodes/4/color | Node 457 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /groups/0/color | Group 17 | "#3f789e" | "#35414A" | Allowed |
| /groups/0/title | Group 17 | "Post" | "Image Finishing" | Allowed |
| /groups/1/color | Group 18 | "#8e5ea2" | "#35414A" | Allowed |
| /nodes/2/bgcolor | Node 440 (PrimitiveInt) | "#355" | "#30343B" | Allowed |
| /nodes/2/color | Node 440 (PrimitiveInt) | "#233" | "#715B2D" | Allowed |
| /nodes/3/bgcolor | Node 441 (PrimitiveInt) | "#355" | "#30343B" | Allowed |
| /nodes/3/color | Node 441 (PrimitiveInt) | "#233" | "#715B2D" | Allowed |
| /nodes/4/bgcolor | Node 437 (ResolutionSelector) | "#355" | "#30343B" | Allowed |
| /nodes/4/color | Node 437 (ResolutionSelector) | "#233" | "#715B2D" | Allowed |
| /nodes/4/title | Node 437 (ResolutionSelector) | (absent; ComfyUI default) | "Image Size (Ratio and Megapixels)" | Allowed |
| /nodes/8/bgcolor | Node 436 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/8/color | Node 436 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/8/title | Node 436 (PreviewAny) | (absent; ComfyUI default) | "Prompt Preview" | Allowed |
| /nodes/9/bgcolor | Node 461 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/9/color | Node 461 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/9/title | Node 461 (Image Comparer (rgthree)) | (absent; ComfyUI default) | "Image Comparison" | Allowed |
| /nodes/10/bgcolor | Node 443 (SaveImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/10/color | Node 443 (SaveImage) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/10/title | Node 443 (SaveImage) | (absent; ComfyUI default) | "Save Image" | Allowed |
| /nodes/13/bgcolor | Node 482 (VAELoader) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/13/color | Node 482 (VAELoader) | (absent; ComfyUI default) | "#35414A" | Allowed |
| /nodes/13/title | Node 482 (VAELoader) | "Flux 2 VAE" | "FLUX.2 VAE" | Allowed |
| /nodes/15/bgcolor | Node 484 (CLIPTextEncode) | "#353" | "#30343B" | Allowed |
| /nodes/15/color | Node 484 (CLIPTextEncode) | "#232" | "#235B74" | Allowed |
| /nodes/21/bgcolor | Node 491 (FluxGuidance) | "#355" | "#30343B" | Allowed |
| /nodes/21/color | Node 491 (FluxGuidance) | "#233" | "#715B2D" | Allowed |
| /nodes/22/bgcolor | Node 493 (PrimitiveInt) | "#355" | "#30343B" | Allowed |
| /nodes/22/color | Node 493 (PrimitiveInt) | "#233" | "#715B2D" | Allowed |
| /nodes/25/bgcolor | Node 492 (EmptyFlux2LatentImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/25/color | Node 492 (EmptyFlux2LatentImage) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/26/bgcolor | Node 438 (7d177234-99df-4feb-bfed-b753341d6ea9) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/26/color | Node 438 (7d177234-99df-4feb-bfed-b753341d6ea9) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/27/bgcolor | Node 496 (PreviewImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/27/color | Node 496 (PreviewImage) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/28/bgcolor | Node 459 (7610828d-a7e7-4981-b042-bf0c982bb071) | "#355" | "#30343B" | Allowed |
| /nodes/28/color | Node 459 (7610828d-a7e7-4981-b042-bf0c982bb071) | "#233" | "#235B74" | Allowed |
| /nodes/28/title | Node 459 (7610828d-a7e7-4981-b042-bf0c982bb071) | (absent; ComfyUI default) | "Expand Character Prompt" | Allowed |
| /nodes/29/bgcolor | Node 488 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/29/color | Node 488 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/29/title | Node 488 (LoadImage) | "Identity Reference — use a clear face/head crop" | "Identity Reference" | Allowed |
| /nodes/30 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 497, "type": "MarkdownNote", "pos": [-2060, 800], "size": [480, 360], "flags": {}, "order": 30, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nGenerate a base photo with Krea-2, then use FLUX.2 Klein to apply an identity reference.\n\n### How to Use\n\n1. Enter a character description in **Expand Character Prompt**. **Prompt Preview** shows the expanded wording when Ollama is running.\n2. Load a clear face or head crop in **Identity Reference**. Use **Identity Edit Instruction** to say what to borrow, and **Image Size (Ratio and Megapixels)** to set the base photo size.\n3. Click **Run**. Check **Klein Identity Edit Preview**. **Save Image** writes the finished image to `ComfyUI/output/`."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 496 | 497 | Allowed |

## Opal Hammer Detection.json

Result: **PASS** — 20 changed fields; 0 unauthorized changes.

Original: `8e97d16:Opal Hammer Detection.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: disabled.

Instructional note addition allowance: 8.

Original SHA-256: `725050054667701b1d4fbc914b10fde5a5e9cf3d6f88fe5070a9fa4b2382e10d`

Modified SHA-256: `eac45d6eb6030d21fdb6ba2b1dd774af8878bb2f5ba62c091e5d14c76cb59729`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /nodes/0/bgcolor | Node 1 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/0/color | Node 1 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/0/title | Node 1 (LoadImage) | (absent; ComfyUI default) | "Image 1" | Allowed |
| /nodes/2/bgcolor | Node 3 (OpalHammerDetect) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 3 (OpalHammerDetect) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/2/title | Node 3 (OpalHammerDetect) | (absent; ComfyUI default) | "Detect with Opal Hammer" | Allowed |
| /nodes/3/bgcolor | Node 4 (PreviewImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/3/color | Node 4 (PreviewImage) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/3/title | Node 4 (PreviewImage) | (absent; ComfyUI default) | "Receipt Preview" | Allowed |
| /nodes/4/bgcolor | Node 5 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/4/color | Node 5 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/4/title | Node 5 (PreviewAny) | (absent; ComfyUI default) | "Detection Summary" | Allowed |
| /nodes/5/bgcolor | Node 6 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/5/color | Node 6 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/5/title | Node 6 (LoadImage) | (absent; ComfyUI default) | "Image 2" | Allowed |
| /nodes/6/bgcolor | Node 7 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/6/color | Node 7 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/6/title | Node 7 (PreviewAny) | (absent; ComfyUI default) | "Manifest Path" | Allowed |
| /nodes/7 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 8, "type": "MarkdownNote", "pos": [-580, 2180], "size": [480, 360], "flags": {}, "order": 7, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nCheck a pair of images with Opal Hammer and see a receipt and summary for the detection run.\n\n### How to Use\n\n1. Load the two images in **Image 1** and **Image 2**. Make sure **Detect with Opal Hammer** points to your running Opal Hammer server.\n2. Start with the saved settings and click **Run**.\n3. Check **Receipt Preview** and **Detection Summary**. The installed node writes results under `ComfyUI/output/opal_hammer/` and includes the folder in the summary.\n\n### Setup and Notes\n\nThe saved **Manifest Path** preview is available only with node versions that expose that output."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 7 | 8 | Allowed |

## Opal Hammer Processing.json

Result: **PASS** — 22 changed fields; 0 unauthorized changes.

Original: `8e97d16:Opal Hammer Processing.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: disabled.

Instructional note addition allowance: 14.

Original SHA-256: `4ec495ae54c8b769149b13c56820839647f39cdde76c53cf75c3126da66aa987`

Modified SHA-256: `b642501894d5e53bcf387b40a6ae243ee03ab6f96fb2fd2dafe26ebe8a5728d8`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /nodes/0/bgcolor | Node 1 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/0/color | Node 1 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/0/title | Node 1 (LoadImage) | (absent; ComfyUI default) | "Image 1" | Allowed |
| /nodes/1/bgcolor | Node 5 (OpalHammerProcess) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/1/color | Node 5 (OpalHammerProcess) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/1/title | Node 5 (OpalHammerProcess) | (absent; ComfyUI default) | "Process with Opal Hammer" | Allowed |
| /nodes/2/bgcolor | Node 6 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 6 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/2/title | Node 6 (PreviewAny) | "Summary" | "Processing Summary" | Allowed |
| /nodes/3/bgcolor | Node 7 (PreviewAny) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/3/color | Node 7 (PreviewAny) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/3/title | Node 7 (PreviewAny) | "Manimfest Path" | "Manifest Path" | Allowed |
| /nodes/4/bgcolor | Node 9 (LoadImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/4/color | Node 9 (LoadImage) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/4/title | Node 9 (LoadImage) | (absent; ComfyUI default) | "Image 2" | Allowed |
| /nodes/6/bgcolor | Node 12 (PreviewImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/6/color | Node 12 (PreviewImage) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/7/bgcolor | Node 13 (PreviewImage) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/7/color | Node 13 (PreviewImage) | (absent; ComfyUI default) | "#594A72" | Allowed |
| /nodes/7/title | Node 13 (PreviewImage) | "Receipt" | "Receipt Preview" | Allowed |
| /nodes/8 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 14, "type": "MarkdownNote", "pos": [-740, 2880], "size": [480, 360], "flags": {}, "order": 8, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nSend a pair of images to Opal Hammer for processing and review the returned images and receipts.\n\n### How to Use\n\n1. Load the two images in **Image 1** and **Image 2**. Make sure **Process with Opal Hammer** points to your running Opal Hammer server.\n2. Start with the saved settings and click **Run**.\n3. Check **Processed Image**, **Receipt Preview**, and **Processing Summary**. The installed node writes results under `ComfyUI/output/opal_hammer/` and includes the folder in the summary.\n\n### Setup and Notes\n\nThe saved **Manifest Path** preview is available only with node versions that expose that output."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 13 | 14 | Allowed |

## RTX Video Upscale.json

Result: **PASS** — 11 changed fields; 0 unauthorized changes.

Original: `8e97d16:RTX Video Upscale.json`

Layout allowance: none; all positions, sizes, and group bounds are protected.

Instructional note text allowance: disabled.

Instructional note addition allowance: 6.

Original SHA-256: `b473b2ad59cd9c67fac3d519ce6d08deeba08fd25d474e24d99bad154b7e4448`

Modified SHA-256: `8775ffe4a1a3be2b15822db8b0cbcc4a163d31309e0123f28e617a5eaceeee11`

| JSON Pointer | Object | Before | After | Result |
| --- | --- | --- | --- | --- |
| /nodes/0/bgcolor | Node 1 (LoadVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/0/color | Node 1 (LoadVideo) | (absent; ComfyUI default) | "#235B74" | Allowed |
| /nodes/0/title | Node 1 (LoadVideo) | (absent; ComfyUI default) | "Input Video" | Allowed |
| /nodes/2/bgcolor | Node 3 (RTXVideoSuperResolution) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/2/color | Node 3 (RTXVideoSuperResolution) | (absent; ComfyUI default) | "#715B2D" | Allowed |
| /nodes/2/title | Node 3 (RTXVideoSuperResolution) | (absent; ComfyUI default) | "RTX Video Upscale" | Allowed |
| /nodes/4/bgcolor | Node 5 (SaveVideo) | (absent; ComfyUI default) | "#30343B" | Allowed |
| /nodes/4/color | Node 5 (SaveVideo) | (absent; ComfyUI default) | "#2B644C" | Allowed |
| /nodes/4/title | Node 5 (SaveVideo) | (absent; ComfyUI default) | "Save Video" | Allowed |
| /nodes/5 | Authorized instructional note addition | (absent; ComfyUI default) | {"id": 6, "type": "MarkdownNote", "pos": [-660, 5540], "size": [480, 360], "flags": {}, "order": 5, "mode": 0, "inputs": [], "outputs": [], "title": "Quick Start", "properties": {}, "widgets_values": ["### What It Does\n\nEnlarge a video using NVIDIA RTX Video Super Resolution and assemble it with the source audio.\n\n### How to Use\n\n1. Load the clip in **Input Video**.\n2. In **RTX Video Upscale**, choose the resize mode and scale. Start with the saved quality settings on an RTX-compatible device.\n3. Click **Run**. **Save Video** writes the result under `ComfyUI/output/video/`."], "color": "#35414A", "bgcolor": "#30343B"} | Allowed |
| /last_node_id | Authorized instructional note addition | 5 | 6 | Allowed |
