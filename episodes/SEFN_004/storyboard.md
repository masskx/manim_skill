# SEFN Storyboard

| Time | Visual | Narration | Notes |
|---|---|---|---|
| 0-4s | Title SEFN, long sequence line with local grid dimming | Mamba can see far, but may lose 2D neighborhood | Pain-point hook |
| 4-12s | Spatial branch: `spatial -> AvgPool -> Conv-LN-ReLU -> Upsample -> S` | SEFN extracts a spatial hint from the pre-Mamba feature | Use green/yellow spatial map |
| 12-21s | After-Mamba feature expands, depthwise conv, splits into `x1` and `x2`; `S` fuses into `x1` | One branch gets spatial information, the other waits for modulation | No frequency or attention language |
| 21-28s | Formula `Y=W_o(GELU(Fuse(x_1,S))\odot x_2)` and gate pulse | GELU then pointwise product gates the feedforward output | Formula-led page |
| 28-34s | 3-line code card and CTA | Plug into SEM Block; comment SEFN for resources | Final page |
