# ComfyUI workflows

Model downloads and custom-node requirements for the **22 workflow JSON files in the repository root**. Files in `archive/` and the external Stability Matrix workflow folder are excluded. Audited on November 13, 2026, including nodes inside subgraphs.

## Setup

1. Install or update [ComfyUI](https://github.com/Comfy-Org/ComfyUI) and its frontend ([update guide](https://docs.comfy.org/installation/update_comfyui)). These workflows use recent native model support and subgraphs; saved core-node metadata includes version **0.45.0**. This is an observed version, not a tested minimum.
2. Install the custom-node packs needed by your chosen workflow from the table below. [ComfyUI Manager](https://github.com/Comfy-Org/ComfyUI-Manager) can install missing packs; for manual installation, follow each pack's instructions and install dependencies into **ComfyUI's Python environment**. Restart afterward.
3. Download the models for that workflow. Folder paths below are relative to `ComfyUI/models/`. With Stability Matrix, equivalent shared model directories configured through `extra_model_paths.yaml` also work.
4. Refresh the model list, reselect any renamed files in their loader nodes, and replace the saved example images, videos, and audio with your own inputs. Open subgraphs to check their loaders too.

The tables describe **saved loader selections**, including selectable branches. Download only the branches you will use. Notes embedded in the JSON sometimes describe older defaults; those note-only models are not added to this requirements list. Bypassing/removing an optional branch can remove its model requirement, but its custom node pack may still be needed to load the unmodified graph cleanly.

## Extensions

| Pack / install link | Nodes used here | Workflows |
| --- | --- | --- |
| [rgthree-comfy](https://github.com/rgthree/rgthree-comfy) | Image Comparer, Fast Groups Bypasser, Power Lora Loader | Ideogram4; Klein Edit, Face Maker, Headswap; SeedVR2 Image; MiniMax CharacterSheet, i2v, t2v |
| [ComfyUI-KJNodes](https://github.com/kijai/ComfyUI-KJNodes) | Ideogram4PromptBuilderKJ, DrawMaskOnImage, MiniMaxChunkFeedForward, preview/attention/VRAM utilities | Ideogram4; Klein Face Maker; all MiniMax workflows |
| [comfyui-ollama](https://github.com/stavsap/comfyui-ollama) | OllamaConnectivityV2, OllamaChat, OllamaGenerateV2, OllamaOptionsV2 | Ideogram4; Klein Edit/Headswap; Krea2; MiniMax except CharacterSheet; Song Gen |
| [Comfyroll Custom Nodes](https://github.com/Suzie1/ComfyUI_Comfyroll_CustomNodes) | CR Prompt List, CR Split String, CR String To Combo, CR String To Number | Klein Dataset Maker; Song Gen |
| [ComfyUI-Easy-Use](https://github.com/yolain/ComfyUI-Easy-Use) | easy positive, easy multiAngle | Klein Face Maker; Qwen Multi Angle |
| [VideoHelperSuite](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite) | VHS_LoadVideo | Bernini Video Editing |
| [SeedVR2 Video Upscaler](https://github.com/numz/ComfyUI-SeedVR2_VideoUpscaler) | SeedVR2LoadDiTModel, SeedVR2LoadVAEModel, SeedVR2VideoUpscaler | Ideogram4 Playground only; the separate SeedVR2 workflows use native ComfyUI nodes |
| [NVIDIA VFX / RTX Nodes](https://github.com/Comfy-Org/ComfyUI_Nvidia_VFX_Nodes) | RTXVideoSuperResolution | All MiniMax workflows; older package ID: comfyui_nvidia_rtx_nodes |
| [Spectrum MiniMax H3](https://github.com/xmarre/ComfyUI-Spectrum-MiniMax-H3) | SpectrumApplyMiniMaxH3 | MiniMax i2v and t2v |

SAM3.1, FLUX.2 Klein, Bernini/Wan, Ideogram4, Krea2, LTX 2.5, MiniMax H3, Qwen Image 2.1, native SeedVR2, and ACE-Step loaders are marked as **ComfyUI core** in these graphs. Do not install unrelated model-wrapper extensions solely because a workflow uses one of those model families. `MarkdownNote`, `Note`, and `PrimitiveNode` are frontend features; UUID-named nodes are embedded subgraphs.

### Additional software and hardware

- **Ollama:** install [Ollama](https://ollama.com/download) and pull the exact tags listed [below](#ollama-models). The saved server is `http://127.0.0.1:11434` or `http://localhost:11434`.
- **FlashAttention:** Ideogram4 includes `PatchFlashAttentionKJ`; install a compatible [FlashAttention](https://github.com/Dao-AILab/flash-attention) build, or bypass that patch node and reconnect the model path.
- **SageAttention:** the MiniMax workflows other than CharacterSheet select `auto` in `PathchSageAttentionKJ`. Install [SageAttention](https://github.com/thu-ml/SageAttention), or set those patch nodes to `disabled`.
- **NVIDIA RTX upscaling:** all MiniMax workflows include RTX Video Super Resolution. Follow the [NVIDIA node installation requirements](https://github.com/Comfy-Org/ComfyUI_Nvidia_VFX_Nodes#requirements), including its `nvidia-vfx` dependency, an RTX GPU, and compatible CUDA-enabled PyTorch. Replace/bypass that branch on unsupported hardware.
- **Video I/O:** follow [VideoHelperSuite's FFmpeg setup](https://github.com/Kosinkadink/ComfyUI-VideoHelperSuite) for Bernini; [FFmpeg downloads](https://ffmpeg.org/download.html) are available separately if your video backend requires them.
- **GPU selection:** Ideogram4's SeedVR2 custom loader is saved with `cuda:1` as its main device and `cuda:0` for offloading. On a single-GPU system, change the main device to your available GPU and choose a supported offload setting. Other loaders may also retain machine-specific device choices.

## Workflow index

| Workflow | Model section | Custom-node packs |
| --- | --- | --- |
| [Background Removal (SAM3).json](<Background%20Removal%20%28SAM3%29.json>) | [SAM3.1](#sam31) | None |
| [Bernini Video Editing.json](<Bernini%20Video%20Editing.json>) | [Bernini](#bernini) | VideoHelperSuite |
| [Ideogram4 Playground.json](<Ideogram4%20Playground.json>) | [Ideogram4 + shared upscaler](#ideogram4) | KJNodes, rgthree, Ollama, SeedVR2 Video Upscaler |
| [Klein Dataset Maker.json](<Klein%20Dataset%20Maker.json>) | [Klein](#flux2-klein) | Comfyroll |
| [Klein Edit.json](<Klein%20Edit.json>) | [Klein + Z-Image refiner](#flux2-klein) | rgthree, Ollama |
| [Klein Face Maker.json](<Klein%20Face%20Maker.json>) | [Klein + SAM3.1](#flux2-klein) | KJNodes, Easy Use, rgthree |
| [Klein Headswap.json](<Klein%20Headswap.json>) | [Klein + Z-Image refiner](#flux2-klein) | rgthree, Ollama |
| [Krea2 Turbo.json](<Krea2%20Turbo.json>) | [Krea2 + shared upscaler](#krea2) | Ollama |
| [LTX Video 2.5 FLF2V.json](<LTX%20Video%202.5%20FLF2V.json>) | [LTX 2.5](#ltx-25) | None |
| [LTX Video 2.5 I2V.json](<LTX%20Video%202.5%20I2V.json>) | [LTX 2.5](#ltx-25) | None |
| [LTX Video 2.5 T2V.json](<LTX%20Video%202.5%20T2V.json>) | [LTX 2.5](#ltx-25) | None |
| [Minimax H3 CharacterSheet 6p.json](<Minimax%20H3%20CharacterSheet%206p.json>) | [MiniMax H3](#minimax-h3) | KJNodes, RTX Nodes, rgthree |
| [Minimax H3 i2v.json](<Minimax%20H3%20i2v.json>) | [MiniMax H3](#minimax-h3) | KJNodes, RTX Nodes, rgthree, Ollama, Spectrum |
| [Minimax H3 r2v.json](<Minimax%20H3%20r2v.json>) | [MiniMax H3](#minimax-h3) | KJNodes, RTX Nodes, Ollama |
| [Minimax H3 t2v.json](<Minimax%20H3%20t2v.json>) | [MiniMax H3](#minimax-h3) | KJNodes, RTX Nodes, rgthree, Ollama, Spectrum |
| [Minimax_H3_r2v.json](<Minimax_H3_r2v.json>) | [MiniMax H3](#minimax-h3) | KJNodes, RTX Nodes, Ollama |
| [MiniMax_H3_Ref2V_v4_AutoRoles.json](<MiniMax_H3_Ref2V_v4_AutoRoles.json>) | [MiniMax H3](#minimax-h3) | KJNodes, RTX Nodes, Ollama |
| [Qwen Image 2.1 Edit.json](<Qwen%20Image%202.1%20Edit.json>) | [Qwen Image 2.1](#qwen-image-21) | None |
| [Qwen Image 2.1 Multi Angle.json](<Qwen%20Image%202.1%20Multi%20Angle.json>) | [Qwen Image 2.1](#qwen-image-21) | Easy Use |
| [SeedVR2 Image Upscale.json](<SeedVR2%20Image%20Upscale.json>) | [Native SeedVR2](#native-seedvr2) | rgthree |
| [SeedVR2 Video Upscale.json](<SeedVR2%20Video%20Upscale.json>) | [Native SeedVR2](#native-seedvr2) | None |
| [Song Gen v1.json](<Song%20Gen%20v1.json>) | [ACE-Step](#ace-step--song-gen) | Comfyroll, Ollama |

## SAM3.1

Used by Background Removal and the masking branch in Klein Face Maker.

| Folder under `models/` | Model / download | Used by / notes |
| --- | --- | --- |
| `checkpoints/` | [sam3.1_multiplex_fp16.safetensors](https://huggingface.co/Comfy-Org/sam3.1/resolve/main/checkpoints/sam3.1_multiplex_fp16.safetensors) | SAM3.1 checkpoint |

## Bernini

The saved graph selects the INT8 high/low-noise pair and a rank-32 LightX2V LoRA; its note links older FP8 / rank-64 alternatives.

| Folder under `models/` | Model / download | Used by / notes |
| --- | --- | --- |
| `diffusion_models/` | [wan2.2_bernini_r_high_noise_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Bernini-R/resolve/main/diffusion_models/wan2.2_bernini_r_high_noise_int8_convrot.safetensors) | Both files required |
| `diffusion_models/` | [wan2.2_bernini_r_low_noise_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Bernini-R/resolve/main/diffusion_models/wan2.2_bernini_r_low_noise_int8_convrot.safetensors) | Both files required |
| `text_encoders/` | [umt5_xxl_fp8_e4m3fn_scaled.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/text_encoders/umt5_xxl_fp8_e4m3fn_scaled.safetensors) | Wan text encoder |
| `vae/` | [Wan2_1_VAE_bf16.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan2_1_VAE_bf16.safetensors) | Saved VAE selection |
| `loras/Wan2.1/` | [Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors](https://huggingface.co/Kijai/WanVideo_comfy/resolve/main/Wan21_T2V_14B_lightx2v_cfg_step_distill_lora_rank32.safetensors) | Used by both noise stages |

## Ideogram4

Includes conditional/unconditional model paths, Ollama prompt helpers, a skin-contrast pass, and the custom SeedVR2 upscaling branch.

| Folder under `models/` | Model / download | Used by / notes |
| --- | --- | --- |
| `diffusion_models/` | [ideogram4_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Ideogram-4/resolve/main/diffusion_models/ideogram4_fp8_scaled.safetensors) | Saved Ideogram4 model |
| `diffusion_models/` | [ideogram4_unconditional_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Ideogram-4/resolve/main/diffusion_models/ideogram4_unconditional_fp8_scaled.safetensors) | Saved Ideogram4 model |
| `text_encoders/` | [qwen3vl_8b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Ideogram-4/resolve/main/text_encoders/qwen3vl_8b_fp8_scaled.safetensors) | Ideogram4 text encoder |
| `vae/` | [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) | Shared with Klein |
| `SEEDVR2/` | [seedvr2_ema_7b_sharp-Q4_K_M.gguf](https://huggingface.co/cmeka/SeedVR2-GGUF/resolve/main/seedvr2_ema_7b_sharp-Q4_K_M.gguf) | Custom SeedVR2 branch; not the native SeedVR2 format |
| `SEEDVR2/` | [ema_vae_fp16.safetensors](https://huggingface.co/numz/SeedVR2_comfyUI/resolve/main/ema_vae_fp16.safetensors) | Custom SeedVR2 branch VAE |

Also download the [shared skin-contrast upscaler](#shared-skin-contrast-upscaler) and the [Ideogram4 Ollama model](#ollama-models). The custom SeedVR2 extension uses `models/SEEDVR2/`; it supports GGUF itself, so this graph does not require a separate ComfyUI-GGUF node pack.

## FLUX.2 Klein

Dataset Maker, Edit, and Headswap select the **KV FP8** model. Face Maker selects the regular **9B FP8** model. All four use the same text encoder and VAE.

| Folder under `models/` | Model / download | Used by / notes |
| --- | --- | --- |
| `diffusion_models/` | [flux-2-klein-9b-kv-fp8.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-kv-fp8/resolve/main/flux-2-klein-9b-kv-fp8.safetensors) | Dataset Maker, Edit, Headswap |
| `diffusion_models/` | [flux-2-klein-9b-fp8.safetensors](https://huggingface.co/black-forest-labs/FLUX.2-klein-9b-fp8/resolve/main/flux-2-klein-9b-fp8.safetensors) | Face Maker |
| `text_encoders/` | [qwen_3_8b_fp8mixed.safetensors](https://huggingface.co/Comfy-Org/flux2-klein-9B/resolve/main/split_files/text_encoders/qwen_3_8b_fp8mixed.safetensors) | All Klein workflows |
| `vae/` | [flux2-vae.safetensors](https://huggingface.co/Comfy-Org/flux2-dev/resolve/main/split_files/vae/flux2-vae.safetensors) | All Klein workflows |
| `loras/flux2_klein_9b/` | [Flux2-Klein-9B-consistency-V2.safetensors](https://huggingface.co/dx8152/Flux2-Klein-9B-Consistency/resolve/main/Flux2-Klein-9B-consistency-V2.safetensors) | Klein Edit consistency branch |
| `loras/flux2_klein_9b/` | [head_swap_flux-klein_9b_000003500.safetensors](https://civitai.com/models/2027766?modelVersionId=2610018) | Klein Headswap: BFS / Focus Head version |

Klein Face Maker also needs the [SAM3.1 checkpoint](#sam31). Klein Edit and Headswap also contain the Z-Image branch below and [Ollama helpers](#ollama-models). Some Klein notes still link the base/non-KV model; use the saved loader selections above.

## Z-Image refiner

Additional model branch inside Klein Edit and Klein Headswap.

| Folder under `models/` | Model / download | Used by / notes |
| --- | --- | --- |
| `diffusion_models/` | [z_image_turbo_bf16.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_bf16.safetensors) | Klein Edit |
| `diffusion_models/` | [z_image_turbo_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/diffusion_models/z_image_turbo_int8_convrot.safetensors) | Klein Headswap |
| `text_encoders/` | [qwen_3_4b.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/text_encoders/qwen_3_4b.safetensors) | Both |
| `vae/` | [ae.safetensors](https://huggingface.co/Comfy-Org/z_image_turbo/resolve/main/split_files/vae/ae.safetensors) | Both |
| `loras/Z-Image_Turbo/` | [NiceGirls_UltraReal_-_v1-0_Z-Image_Turbo.safetensors](https://civitai.com/models/1862761?modelVersionId=2465980) | Published filename is `nicegirls_Zimage.safetensors`: reselect it or rename to the saved name |

Headswap also retains a `ZImage/NiceGirls_UltraReal_-_v1-0_Z-Image_Turbo.safetensors` path inside its subgraph definition. Check the exposed LoRA widget and internal loader if either path is missing; use the same model rather than downloading two copies. Pixel-art LoRA links appear only in old notes and are not selected by these saved loaders.

## Krea2

Saved selections for Krea2 Turbo, including its two adapters.

| Folder under `models/` | Model / download | Used by / notes |
| --- | --- | --- |
| `diffusion_models/` | [krea2_turbo_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/diffusion_models/krea2_turbo_int8_convrot.safetensors) | Saved diffusion model |
| `text_encoders/` | [qwen3vl_4b_fp8_scaled.safetensors](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/text_encoders/qwen3vl_4b_fp8_scaled.safetensors) | Saved text encoder |
| `vae/` | [wan_2.1_vae.safetensors](https://huggingface.co/Comfy-Org/Wan_2.1_ComfyUI_repackaged/resolve/main/split_files/vae/wan_2.1_vae.safetensors) | Saved VAE filename; see discrepancy below |
| `loras/Krea2/` | [nicegirls_krea2.safetensors](https://civitai.com/models/1862761?modelVersionId=3075498) | NiceGirls UltraReal, Krea2 version |
| `loras/Krea2/` | [krea2filterbypass3.safetensors](https://civitai.com/models/2728234?modelVersionId=3067151) | 3vector version; exact local file hash matches this release |

**VAE discrepancy:** the graph selects `wan_2.1_vae.safetensors`, while the embedded Krea2 instructions specify [qwen_image_vae.safetensors](https://huggingface.co/Comfy-Org/Krea-2/resolve/main/vae/qwen_image_vae.safetensors). These are distinct filenames; if following the official Krea2 setup, download its VAE into `models/vae/` and explicitly reselect it. The saved Wan selection has not been runtime-tested here.

Also see the [shared skin-contrast upscaler](#shared-skin-contrast-upscaler) and [Ollama](#ollama-models). `krea2_warmpastel.safetensors` is an old note-only reference, not a saved loader requirement.

## LTX 2.5

Shared models for FLF2V, I2V, and T2V. [Lightricks' model repository](https://huggingface.co/Lightricks/LTX-2.5) currently requires accepting its download conditions.

| Folder under `models/` | Model / download | Used by / notes |
| --- | --- | --- |
| `diffusion_models/` | [ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/diffusion_models/ltx-2.5-22b-distilled-transformer-comfy-int8-convrot.safetensors) | All three |
| `text_encoders/` | [gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/text_encoders/gemma4-12b-with-proj-ltx-2.5-comfy-int8-convrot.safetensors) | All three |
| `vae/` | [ltx-2.5-video-vae-bf16.safetensors](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/vae/ltx-2.5-video-vae-bf16.safetensors) | All three |
| `vae/` | [ltx-2.5-audio-vae-bf16.safetensors](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/vae/ltx-2.5-audio-vae-bf16.safetensors) | All three |
| `text_encoders/` | [gemma4_e2b_it_bf16.safetensors](https://huggingface.co/Comfy-Org/gemma-4/resolve/main/text_encoders/gemma4_e2b_it_bf16.safetensors) | FLF2V and T2V prompt-enhancement branch |
| `text_encoders/` | [gemma4_e2b_it_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/gemma-4/resolve/main/text_encoders/gemma4_e2b_it_int8_convrot.safetensors) | I2V prompt-enhancement branch |
| `latent_upscale_models/` | [ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors](https://huggingface.co/Lightricks/LTX-2.5/resolve/main/latent_upscale_models/ltx-2.5-latent-spatial-upscaler-x2-bf16-1.0.safetensors) | I2V and T2V upscale branch |

The old Gemma-3 model-directory and vocoder filenames in metadata/notes are not selected by the current loaders. These three graphs use native ComfyUI LTX nodes; they do not reference the separate ComfyUI-LTXVideo extension.

## MiniMax H3

Shared model family for all six MiniMax workflows. Saved selections use the INT8 text encoder and INT8 video VAE, even where old notes suggest NVFP4 / FP16 versions.

| Folder under `models/` | Model / download | Used by / notes |
| --- | --- | --- |
| `diffusion_models/` | [minimax_h3_fl2va_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_fl2va_pruned_int8_convrot.safetensors) | i2v and t2v |
| `diffusion_models/` | [minimax_h3_ref2va_pruned_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/diffusion_models/minimax_h3_ref2va_pruned_int8_convrot.safetensors) | CharacterSheet and all reference-to-video variants |
| `text_encoders/` | [qwen3vl_32b_minimax_h3_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/text_encoders/qwen3vl_32b_minimax_h3_int8_convrot.safetensors) | All six |
| `vae/` | [minimax_h3_video_vae_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_video_vae_int8_convrot.safetensors) | All six |
| `vae/` | [minimax_h3_audio_vae_fp32.safetensors](https://huggingface.co/Comfy-Org/MiniMax-H3/resolve/main/vae/minimax_h3_audio_vae_fp32.safetensors) | All six |
| `vae_approx/` | [taeh3.safetensors](https://github.com/madebyollin/taehv/raw/main/safetensors/taeh3.safetensors) | Temporal tiny VAE from madebyollin; matches the local file hash; all except CharacterSheet |
| `loras/` | [minimax_h3_fl2v_lightx2v_turbo_8step_v1.0_resized_avg_rank_24_bf16.safetensors](https://huggingface.co/Kijai/MiniMax-H3_comfy/resolve/main/loras/minimax_h3_fl2v_lightx2v_turbo_8step_v1.0_resized_avg_rank_24_bf16.safetensors) | CharacterSheet; exposed 8-step choice in i2v/t2v |
| `loras/` | [minimax_h3_fl2v_lightx2v_turbo_4step_v0.1_comfy_resized_avg_rank_21_bf16.safetensors](https://huggingface.co/Kijai/MiniMax-H3_comfy/resolve/main/loras/minimax_h3_fl2v_lightx2v_turbo_4step_v0.1_comfy_resized_avg_rank_21_bf16.safetensors) | Internal 4-step branch in i2v/t2v; one copy is bypassed |
| `loras/` | [minimax_h3_ref2v_turbo_8step_v1.1_768p_comfyui_bf16.safetensors](https://huggingface.co/lightx2v/Minimax-h3-Turbo/resolve/main/minimax_h3_ref2v_turbo_8step_v1.1_768p_comfyui_bf16.safetensors) | Minimax H3 r2v and MiniMax_H3_Ref2V_v4_AutoRoles |
| `loras/` | [minimax_h3_ref2v_lightx2v_turbo_4step_v0.1_resized_avg_rank_20_bf16.safetensors](https://huggingface.co/Kijai/MiniMax-H3_comfy/resolve/main/loras/minimax_h3_ref2v_lightx2v_turbo_4step_v0.1_resized_avg_rank_20_bf16.safetensors) | Minimax_H3_r2v (underscore filename) |

**Check the sampling preset:** CharacterSheet saves a FL2V acceleration LoRA alongside a Ref2VA base, and i2v/t2v expose an 8-step LoRA while their nested definitions retain a 4-step choice. The table records these selections rather than claiming every combination is validated. Match the LoRA to the base model and intended step count when choosing a branch.

All six include NVIDIA RTX upscaling; all except CharacterSheet also include Ollama and SageAttention. Only i2v/t2v reference Spectrum. The tiny VAE is for previews and does not replace either full VAE. The local temporal `taeh3.safetensors` has SHA-256 `4fd022bfcab08772fe0536b17ea1a3bbb5625be11e397868d1c5d891863d4c13`; Kijai also publishes a different 2D decoder under the same filename, so use the linked temporal file to reproduce this setup.

## Qwen Image 2.1

Both Edit and Multi Angle contain regular/turbo model branches and a local prompt-enhancement encoder.

| Folder under `models/` | Model / download | Used by / notes |
| --- | --- | --- |
| `diffusion_models/` | [qwen_image_2.1_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_int8_convrot.safetensors) | Both workflows |
| `diffusion_models/` | [qwen_image_2.1_turbo_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/diffusion_models/qwen_image_2.1_turbo_int8_convrot.safetensors) | Both workflows |
| `text_encoders/` | [qwen3vl_8b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3vl_8b_int8_convrot.safetensors) | Both workflows |
| `text_encoders/` | [qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors](https://huggingface.co/Comfy-Org/Qwen-Image-2.1/resolve/main/text_encoders/qwen3.5_9b_qwen_image_2.1_pe_i2i.int8_convrot.safetensors) | Both workflows |
| `vae/` | [texture_fix_vae_for_qwen_image_2.1_bf16.safetensors](https://huggingface.co/madebyollin/texture-fix-vae-for-qwen-image-2.1/resolve/main/texture_fix_vae_for_qwen_image_2.1_bf16.safetensors) | Saved VAE choice in both workflows |
| `loras/Qwen/` | [Fusion_2000.safetensors](https://civitai.com/models/2548669?modelVersionId=3363920) | Edit fusion LoRA; also retained in Multi Angle subgraph definition |
| `loras/Qwen/` | [multiple_angles_step1000.safetensors](https://huggingface.co/akhaliq/Qwen-Image-2.1-Multiple-Angles-LoRA/resolve/main/multiple_angles_step1000.safetensors) | Multi Angle exposed LoRA choice |

Multi Angle exposes the multiple-angles adapter, while its nested definition still names Fusion. Check the exposed widget after import; use the selected branch's adapter. The default Qwen VAE linked in old notes is an alternative, not the saved Texture-Fix VAE.

## Native SeedVR2

The standalone Image and Video Upscale workflows use core ComfyUI loaders, unlike Ideogram4's custom GGUF branch.

| Folder under `models/` | Model / download | Used by / notes |
| --- | --- | --- |
| `diffusion_models/` | [seedvr2_7b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/diffusion_models/seedvr2_7b_int8_convrot.safetensors) | Image Upscale |
| `diffusion_models/` | [seedvr2_3b_int8_convrot.safetensors](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/diffusion_models/seedvr2_3b_int8_convrot.safetensors) | Video Upscale |
| `vae/` | [seedvr2_ema_vae_fp16.safetensors](https://huggingface.co/Comfy-Org/SeedVR2/resolve/main/vae/seedvr2_ema_vae_fp16.safetensors) | Both |

## ACE-Step / Song Gen

Song Gen v1 uses ACE-Step 1.5 XL Turbo with two text encoders, plus Ollama to prepare text.

| Folder under `models/` | Model / download | Used by / notes |
| --- | --- | --- |
| `diffusion_models/` | [acestep_v1.5_xl_turbo_bf16.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/diffusion_models/acestep_v1.5_xl_turbo_bf16.safetensors) | Song Gen |
| `text_encoders/` | [qwen_0.6b_ace15.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_0.6b_ace15.safetensors) | Both required by DualCLIPLoader |
| `text_encoders/` | [qwen_4b_ace15.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/text_encoders/qwen_4b_ace15.safetensors) | Both required by DualCLIPLoader |
| `vae/` | [ace_1.5_vae.safetensors](https://huggingface.co/Comfy-Org/ace_step_1.5_ComfyUI_files/resolve/main/split_files/vae/ace_1.5_vae.safetensors) | Song Gen |

## Shared skin-contrast upscaler

Used by Ideogram4 Playground and Krea2 Turbo.

| Folder under `models/` | Model / download | Used by / notes |
| --- | --- | --- |
| `upscale_models/` | [1xSkinContrast-High-SuperUltraCompact.pth](https://openmodeldb.info/models/1x-SkinContrast-High-SuperUltraCompact) | OpenModelDB page includes the author's download link |

## Ollama models

Ollama stores these models separately from `ComfyUI/models/`. Pull only the tags used by the workflows you want to run. You can choose a different installed model in the connectivity node, but prompt/image capabilities and results may change.

| Saved tag / model page | Workflows |
| --- | --- |
| [gemma4:26b-a4b-it-q8_0](https://ollama.com/library/gemma4:26b-a4b-it-q8_0) | Ideogram4 Playground |
| [gemma4:e4b](https://ollama.com/library/gemma4:e4b) | Klein Edit |
| [huihui_ai/qwen3.6-abliterated:35b](https://ollama.com/huihui_ai/qwen3.6-abliterated:35b) | Klein Headswap, Krea2 Turbo, MiniMax except CharacterSheet, Song Gen |

```sh
ollama pull gemma4:26b-a4b-it-q8_0
ollama pull gemma4:e4b
ollama pull huihui_ai/qwen3.6-abliterated:35b
```

Start Ollama before queueing any graph that uses its nodes. Ensure the connectivity node points to the host where Ollama actually runs.

## Before the first run

- Check every model and LoRA dropdown, including exposed subgraph widgets. Preserve the listed LoRA subfolders or reselect the file from its actual location. Windows `\` separators in saved paths correspond to `/` subfolders in these tables.
- Check GPU device selections and attention backends against your hardware. No universal VRAM minimum is claimed: model precision, resolution, frame count, offloading, and simultaneous Ollama use all affect memory requirements.
- Replace missing example inputs. This repository contains workflow graphs; model weights and source media must be obtained separately.
- If a model download is gated, sign in and accept the publisher's terms on its model page. Civitai may require login for downloads.
- These requirements were checked against workflow JSON, installed pack metadata, Hugging Face file listings, Civitai version metadata, and upstream project documentation. **The workflows were not executed as part of this README audit.**
