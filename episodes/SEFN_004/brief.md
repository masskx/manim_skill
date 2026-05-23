# SEFN Episode Brief

## Episode

- module_name: SEFN
- module_abbr: SEFN
- full_name: Spatially-Enhanced Feedforward Network
- paper_title: SEM-Net: Efficient Pixel Modelling for image inpainting with Spatially Enhanced SSM
- episode_slug: SEFN_004
- video_type: deep learning plug-in module short
- source_paper_or_code: SEFN paper PDF + `materials/SEFN(CV,WACV2025).py`
- module_type: Spatially-enhanced feedforward / local spatial gating / CNN feature modulation
- pain_point: SSM/Mamba can capture long-range dependencies, but its 1D sequence modelling weakens 2D local spatial awareness for pixel-level restoration.
- target_tasks: image inpainting, low-level vision restoration, SSM/Mamba-based vision blocks
- core_mechanism: SEFN uses the feature before the Mamba block as `spatial`, downsamples it, applies two Conv-LN-ReLU blocks, upsamples it as a spatial indicator, fuses that indicator into one feedforward branch, then uses `GELU(x1) * x2` to modulate the output.
- key_formula: `Y = W_o(GELU(Fuse(DW(X)_1, S)) \odot DW(X)_2)`
- visual_metaphor: Mamba after-feature is split into two lanes; the pre-Mamba spatial feature becomes a local map that adjusts only the first lane before a multiplicative gate.
- min_integration_code: `self.sefn = SEFN(dim, 2, True); y = mamba_block(x); out = self.sefn(y, x)`
- cta_keyword: SEFN
- target_duration_seconds: 24
- visual_style: dark tech, cyan/yellow/green accents, large Manim mechanism animation
- voiceover_tone: short Douyin-style Chinese, practical, mechanism-first
- cta: 评论区打 SEFN，拿 PDF 笔记、PyTorch 代码和架构图拆解

## Source Materials

- paper_pdf_path: episodes/SEFN_004/materials/SEFN(CV,WACV2025).pdf
- code_path: episodes/SEFN_004/materials/SEFN(CV,WACV2025).py
- architecture_image_path: episodes/SEFN_004/materials/Snipaste_2026-05-23_11-47-15.jpg
- extra_images:
  - episodes/SEFN_004/materials/pdf2code (1).png
  - episodes/SEFN_004/materials/pdf2code (2).png
  - episodes/SEFN_004/materials/pdf2code (3).png
  - episodes/SEFN_004/materials/pdf2code (4).png

## Extracted Facts

- class_name: SEFN
- constructor: `SEFN(dim, ffn_expansion_factor, bias)`
- forward_signature: `forward(self, x, spatial)`
- input_shape: `x` and `spatial` are feature maps, typically `B, C, H, W`.
- output_shape: same channel count as `dim`; spatial size follows the input feature map after project-out.
- plug_position: after the Mamba/SMB feature modelling inside an SEM block, while using the pre-Mamba feature as `spatial`.
- suitable_tasks:
  - image inpainting
  - low-level image restoration
  - vision SSM blocks that need extra local spatial awareness
- limitations:
  - The provided plug-in code is the SEFN component, not the full SEM-Net.
  - The video should not claim standalone benchmark gains without running the full paper setup.
  - `spatial` should be a compatible feature map with the same spatial scale after the SEFN upsample step.

## Module Steps

1. `project_in(x)` expands the after-Mamba feature to two hidden branches.
2. The `spatial` feature is average-pooled, processed by Conv-LN-ReLU blocks, then upsampled.
3. `dwconv(x)` is split into `x1` and `x2`.
4. `x1` is concatenated with the spatial indicator and fused by `fusion`, then refined by a depthwise convolution.
5. `GELU(x1) * x2` gates the second feedforward branch.
6. `project_out` maps the hidden feature back to `dim`.

## BGM

- bgm_style: tech_fast
- bgm_auto_select: true
- bgm_path: episodes/SEFN_004/audio/bgm.wav
- bgm_volume: 0.12
- voiceover_volume: 1.0
- sfx_volume: 0.25
- music_mood: modern tech electronic
- music_energy: medium
