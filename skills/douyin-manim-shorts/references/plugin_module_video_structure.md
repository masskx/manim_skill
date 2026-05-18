# Plug-in Module Video Structure

Use this fixed structure for 20-30 second deep learning plug-in module shorts. The default production target is 21-26 seconds: fast enough for Douyin, long enough for one real mechanism animation.

## Standard 5-Beat Structure

| Time | Beat | Goal |
|---|---|---|
| 0-3s | Pain-point hook | Make the viewer feel the module is useful. |
| 3-7s | Problem visualization | Show what goes wrong in tensors, features, domains, masks, or branches. |
| 7-15s | Core mechanism animation | Use Manim formulas, flow, curves, spectra, heatmaps, gates, residuals, or fusion. |
| 15-21s | Code insertion | Show the exact 3-5 line minimum usage and highlight the inserted line. |
| 21-26s | Resource-pack CTA | Promise the prepared PDF notes, PyTorch code, architecture figure, or demo package. |

Use the older six-scene structure below when a separate plug-position beat is needed. Otherwise, merge plug position into the mechanism or code beat.

## Scene 1: Hook, 0-3 seconds

- Visual: module name, one pain-point visual, or a before/after contrast.
- Voiceover: ask why a common model problem happens or state the practical payoff.
- Subtitle limit: 6-12 Chinese characters.
- Manim animation: fast title reveal, highlight flash, split-screen contrast, or one object snapping into focus.
- Avoid: greetings, paper history, author names, dense architecture diagrams, or abstract definitions.

## Scene 2: Problem, 3-7 seconds

- Visual: the baseline model path with the weakness highlighted.
- Voiceover: name the problem in user language, such as "small targets get ignored" or "channels all get treated the same".
- Subtitle limit: 8-14 Chinese characters.
- Manim animation: dim irrelevant blocks, red warning outline, bottleneck squeeze, noisy feature flow.
- Avoid: full benchmark tables, long task background, or formulas before the viewer knows the problem.

## Scene 3: Module Mechanism, 7-13 seconds

- Visual: simplified module block diagram with 2-3 internal steps.
- Voiceover: explain the mechanism as a transformation, not as source-code detail.
- Subtitle limit: 8-16 Chinese characters.
- Manim animation: staged reveal, arrows through blocks, branch split and merge, gate open/close, weight bar filling.
- Avoid: more than three simultaneous branches, tiny labels, full paper figure pasted into the frame, or long equations.

## Scene 4: Plug Position, 13-17 seconds

- Visual: backbone or network block with a bright insertion point.
- Voiceover: say where to insert the module and what tensor passes through it.
- Subtitle limit: 8-14 Chinese characters.
- Manim animation: module block slides into the model, arrow points to insertion position, local zoom from full architecture to module.
- Avoid: vague statements like "put it in the model" without location, crowded whole-network diagrams, or unclear input/output direction.

## Scene 5: Code Usage, 17-21 seconds

- Visual: 3-5 lines of code with Chinese comments.
- Voiceover: give the minimum usage pattern.
- Subtitle limit: 8-14 Chinese characters.
- Manim animation: typewriter reveal, line highlight, module call pulse, code-to-diagram arrow.
- Avoid: full class implementation, long imports, training loop code, optimizer settings, or unexplained parameters.

## Scene 6: CTA, 21-25 seconds

- Visual: module name, one-line takeaway, optional resource-pack prompt.
- Voiceover: summarize when to use it and invite comments or saves.
- Subtitle limit: 6-12 Chinese characters.
- Manim animation: final highlight, compact recap, checkmark list with two items, short hold of 0.6-1.5 seconds.
- Avoid: a long frozen outro, unrelated subscription speech, new technical details, or promises not supported by materials.

## Timing Notes

- The structure is fixed, but exact boundaries can move by 1-2 seconds if narration requires it.
- If the module is simple, end near 18-21 seconds rather than padding.
- If code usage is essential, allocate more time to Scene 5 and shorten the CTA.
- One video should teach one module and one adoption reason.
- Never turn the video into a full paper report. The default story is: pain point -> mechanism -> code -> resource pack.
- Use short voiceover lines. Avoid "本文提出" and "实验表明" unless the user specifically asks for academic reporting.

## Plug-in Module Voiceover Pattern

Prefer short, spoken Chinese lines:

```text
不是模型太弱，是特征偏了。
它不改主干，直接插在特征后。
低频看结构，高频看细节。
Gate 决定该补多少。
复制三行，就能接入。
PDF笔记、代码、架构图都整理好了。
```

Rules:

- Do not use paper-report phrasing such as "本文提出" or "大量实验表明".
- One spoken sentence should usually stay under 14 Chinese characters when possible.
- Put the pain point before the mechanism.
- Put the usage value before the CTA.
