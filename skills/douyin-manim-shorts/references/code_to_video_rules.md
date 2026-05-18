# Code To Video Rules

Use these rules when turning plug-in module code into short-video content.

## Main Goal

Show the minimum usable call pattern, not the full implementation.

## Rules

1. Show only the minimum usage.
   - Include module creation and one forward call.
   - Skip imports unless they are necessary for understanding.
   - Do not show a full class definition.

2. Keep code to 3-5 lines.
   - If it does not fit, make a simplified pseudocode snippet.
   - Label simplified snippets clearly.
   - Code must remain readable on a phone screen.

3. Add Chinese comments.
   - Each comment should explain why the line exists.
   - Keep comments short enough for a phone screen.

4. Prefer direct plug-in calls.
   - Good: `x = CBAM(channels)(x)  # 插到特征后面`
   - Good: `out = block(x) + x  # 保留残差`
   - Avoid showing a whole training loop.

5. Extract only the key code idea.
   - Class name.
   - Required constructor arguments.
   - Input/output shape.
   - Forward path summary.

6. Do not teach the full source code.
   - Skip internal helper functions.
   - Skip parameter initialization unless it matters to the module's core idea.
   - Skip every branch detail if a clean block diagram communicates it better.

7. Highlight the line that actually inserts or calls the module.
   - Use a yellow border, glow, underline, or pulse.
   - Voiceover should say the value plainly: "复制三行，就能接入" or "改一行就能试".
   - Do not let the code panel touch the left or right screen edge.

## Snippet Format

Use this style:

```python
module = ModuleName(dim=64)      # 创建即插即用模块
x = module(x)                   # 输入特征, 输出增强特征
out = head(x)                   # 后面接原任务头
```

If the true API is different, use the true API. Do not force `Module(...)(x)` when it is inaccurate.

Preferred adoption-style snippet:

```python
self.afda = AFDA(channels)      # 对齐通道
feat = backbone(x)              # 提取特征
feat = self.afda(feat)          # 频域适配
```

## Pseudocode Format

Use pseudocode when real code is too long:

```python
x = backbone(x)                 # 提取基础特征
x = module(x)                   # 插入模块增强特征
y = classifier(x)               # 原任务头不变
```

Mark this as "简化用法" in the script and storyboard.
