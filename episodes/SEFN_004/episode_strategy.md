# SEFN Episode Strategy

## Module Type Judgment

SEFN is a spatially-enhanced feedforward module with local spatial gating.

## Justification

The paper names it Spatially-Enhanced Feedforward Network and states that it complements local spatial information for SSMs. The code implements a feedforward-style expansion, depthwise convolution, a separate spatial branch, branch fusion, and `GELU(x1) * x2` modulation.

## Structures Not To Reuse

- No frequency spectrum.
- No wavelet low/high split.
- No residual-return formula.
- No attention QKV or attention matrix.
- No radar-camera or multi-view fusion phrasing.

## Unique Narrative

Mamba sees far, but SEFN reminds it where local pixels sit. The video explains how SEFN injects a pre-Mamba spatial clue into the after-Mamba feedforward path.

## Core Animation Spine

1. Show Mamba/SSM has long-range view but weak 2D local awareness.
2. Show `spatial` goes through pool, Conv-LN-ReLU, and upsample to become `S`.
3. Show after-Mamba feature splits into `x1` and `x2`.
4. Fuse `S` into `x1`, then `GELU(x1) * x2`.
5. Show the 3-line plug-in code and CTA.

## Core Formula

`Y = W_o(GELU(Fuse(x_1, S)) \odot x_2)`

## Visual Metaphor

Spatial map as a local coordinate hint that adjusts one feedforward lane before gating the other lane.

## Differences From Recent Videos

Compared with WMVF, SEFN is not a two-frequency decomposition or residual fusion module. Its signature is pre-Mamba spatial information guiding a post-Mamba feedforward gate.
