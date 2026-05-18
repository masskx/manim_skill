# Material Input Rules

Use these rules in Deep Learning Plug-in Module Video Mode. The goal is to turn real source materials into a short, evidence-grounded video brief without pretending the materials say more than they do.

## Paper PDF

Extract:

- Paper title.
- Module name and full name if both exist.
- The problem the module tries to solve.
- Where the module is inserted in the model or pipeline.
- Module structure: main branches, blocks, operators, gates, attention paths, or data flow.
- Suitable tasks or model families.
- Limitations, assumptions, or stated failure cases.

Rules:

- Prefer the abstract, method section, module figure, ablation section, and conclusion.
- Do not summarize the whole paper. Extract only what supports a 15-25 second module explainer.
- Separate paper claims from your own interpretation.
- If a conclusion is not present in the paper, do not invent it.
- If the paper gives benchmark numbers, use them only when the user asks for a metric-focused video; otherwise emphasize mechanism and plug-in usage.

## Module Code

Extract:

- Class name.
- Initialization parameters and useful defaults.
- `forward` input and output.
- Minimum calling pattern.
- A 3-5 line core code snippet suitable for the video.

Rules:

- Prefer PyTorch semantics when code is in `torch.nn.Module`.
- Identify shape assumptions such as `B, C, H, W`, sequence length, channel count, or hidden dimension.
- Identify whether the module is residual, attention-like, convolutional, normalization-like, gating-based, or feature-fusion based.
- Keep implementation details for the brief, not the final spoken script.
- If the real code is long, create pseudocode and label it as simplified.

## White-Background Architecture Figure

Use the figure as:

- The main visual reference.
- A cropped local zoom of the key module.
- A source for redrawing a simplified Manim block diagram.
- A place to add an arrow showing the plug-in position.

Do not:

- Put the entire paper figure into the vertical frame at full density.
- Cover the figure with many decorative words.
- Use tiny labels that are unreadable on a phone.
- Treat the figure as proof of a claim not supported by the paper.

Recommended approach:

1. First show a simplified module block diagram.
2. Then zoom into the original figure region that matches the module.
3. Use one highlight box, one arrow, and at most three numbered callouts.
4. If the figure is too complex, redraw it as a clean Manim diagram and cite it as a simplified reconstruction.

## Missing Materials

If materials are incomplete:

- Missing PDF: infer only from code and user-provided description; mark paper fields as `unknown`.
- Missing code: explain mechanism from paper and figure, but do not invent a calling API.
- Missing figure: use a simplified Manim block diagram based on paper/code structure.
- Missing module name: use the class name if available, otherwise ask for the intended module name.
- Missing limitations: write `not stated in provided materials` instead of guessing.

Reasonable completion is allowed for presentation glue, such as short hook wording, simplified visual metaphors, and scene pacing. It is not allowed for scientific claims, reported improvements, benchmark conclusions, or exact module behavior.
