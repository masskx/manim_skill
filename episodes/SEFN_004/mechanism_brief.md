# SEFN Mechanism Brief

1. Current module full name and abbreviation:
   Spatially-Enhanced Feedforward Network, SEFN.

2. Core problem:
   SSM/Mamba brings long-range modelling, but the paper states that SSM has insufficient 2D spatial awareness. SEFN complements local spatial dependencies and refines representation after SMB/Mamba.

3. Input tensor:
   `x`, the feature after Mamba/SMB-style modelling, shaped like `B, C, H, W`.

4. Output tensor:
   A projected feature map with `dim` channels and the same expected spatial resolution as `x`.

5. Key internal branches:
   - Main feedforward branch: `project_in -> dwconv -> chunk(x1, x2)`.
   - Spatial branch: `spatial -> avg_pool -> Conv-LN-ReLU -> Conv-LN-ReLU -> upsample`.
   - Fusion/gating: `cat(x1, y) -> fusion -> dwconv_afterfusion -> GELU -> multiply x2`.

6. Information each branch extracts:
   - `x1`: one hidden branch to be spatially informed.
   - `x2`: the branch being modulated.
   - `spatial`: local spatial information from feature representations before the SEM/Mamba block.

7. Mechanism inventory:
   - Frequency transform: No.
   - Wavelet decomposition: No.
   - Attention: No explicit attention.
   - Gating: Yes, via `GELU(x1) * x2`.
   - Multi-scale processing: Limited local spatial pooling/downsample and upsample, but not a generic multi-scale pyramid.
   - Residual learning: Not inside the provided SEFN class.
   - Feature reconstruction: Yes, feature refinement for image restoration representation.

8. True core formula:
   `Y = W_o(GELU(Fuse(DW(W_i(X))_1, S)) \odot DW(W_i(X))_2)`

9. Best single formula for video:
   `Y = W_o(GELU(Fuse(x_1, S)) \odot x_2)`

10. Animation metaphor:
    The pre-Mamba spatial feature becomes a local map that lights up the after-Mamba feedforward lane before a multiplicative gate.

11. Difference from previous episodes:
    Do not use WMVF's frequency split, low/high branches, wavelet language, or residual return. SEFN is a spatial feedforward gate, not a frequency fusion block.

12. Previous-episode structures not allowed:
    FFT, Low/High frequency, wavelet decomposition, radar/camera fusion, residual `Y=X+...`, and attention heatmap narration.

## Authenticity Gate

| Mechanism shown in video | Exists in code/paper | Evidence location | Allowed to show |
|---|---|---|---|
| Spatial branch from pre-Mamba feature | Yes | Paper Sec. 3.2 and `forward(self, x, spatial)` | Yes |
| AvgPool + Conv-LN-ReLU + Upsample | Yes | `self.avg_pool`, `self.conv`, `self.upsample` | Yes |
| Feedforward branch split | Yes | `self.dwconv(x).chunk(2, dim=1)` | Yes |
| Fusion with spatial indicator | Yes | `self.fusion(torch.cat((x1, y), dim=1))` | Yes |
| Multiplicative gate | Yes | `x = F.gelu(x1) * x2` | Yes |
| Residual add | No in SEFN class | Not present in `SEFN.forward` | No |
| Frequency or wavelet split | No | Not present | No |
| QKV attention | No | Not present | No |
