# Paper To Video Rules

Use these rules when converting a paper PDF into short-video language for a deep learning plug-in module.

## Core Principle

Do not make a miniature paper review. Make a practical module explainer.

The short should follow:

```text
pain point -> module mechanism -> insertion method -> code usage
```

## Rules

1. Do not copy the abstract.
   - Abstracts are usually too broad, formal, and claim-heavy.
   - Rewrite in terms a deep learning user can act on.

2. Do not stack formulas.
   - Use zero formulas by default.
   - Use at most one compact formula only if it clarifies the mechanism.
   - Prefer arrows, blocks, gates, and tensor flow.

3. Do not explain the whole paper.
   - Skip related work, full experimental design, dataset lists, and most benchmark tables.
   - Mention metrics only when the video is specifically about performance evidence.

4. Extract one core insight.
   - Good: "CBAM lets the network decide which channel and spatial region deserve attention."
   - Bad: "This paper proposes a comprehensive attention mechanism and validates it on many tasks."

5. Translate the contribution into user language.
   - "Improves representational power" can become "helps the model look at more useful features."
   - "Lightweight module" can become "can be inserted without redesigning the whole backbone."
   - "Ablation validates effectiveness" can become "the paper tests the module separately from the backbone."

6. Preserve scientific caution.
   - Say "the paper reports..." for reported claims.
   - Say "suitable for..." only when the paper, code, or user materials support it.
   - If limitations are not stated, write "not stated in provided materials".

## Short-Video Rewrite Pattern

Use this pattern:

```text
Pain: [common model/user problem]
Mechanism: [the module changes information flow by ...]
Plug: [insert it after/before/inside ...]
Code: [minimal call]
Takeaway: [when a user should consider it]
```

## Anti-Patterns

- Starting with the full paper title.
- Listing all contributions.
- Reading the abstract aloud.
- Showing the full method figure for the entire video.
- Treating reported benchmark improvement as universal truth.
- Claiming the module is "best" without evidence in the provided materials.
