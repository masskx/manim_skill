# AFDA 即插即用模块短视频 V2 分镜

V2 定位：讲 `AFDA.py` 这个轻量频域适配器，不讲完整 AFDAN 论文框架。核心表达是“插在特征图后面，低频看轮廓，高频看边缘，再用 gate 和轻量卷积做特征适配”。

| 时间段 | 屏幕画面 | 动画方式 | 屏幕文字 | 口播 | 使用素材来源 |
|---|---|---|---|---|---|
| 0-1.5s | 第一帧直接出现大标题。左侧 Source 特征清晰，右侧 Target 特征偏红、抖动、错位，旁边有警告标记。 | 标题快速 zoom in；Target 特征左右 shake；红色 warning flash。 | 换个数据集就崩？ / 医学分割跨域痛点 | 医学分割最怕什么？换个数据集，特征就偏了。 | 论文问题背景 + Manim 重绘 |
| 1.5-4s | Source -> Model -> Target，Target 输出 mask 发生错位。 | Source 正常流动；Target 箭头弯曲；输出 mask 红色闪烁并偏移。 | 特征分布偏了 | 医学分割最怕什么？换个数据集，特征就偏了。 | 论文任务背景 + Manim 重绘 |
| 4-7s | Conv Block -> Next Layer，中间突然插入 AFDA 卡片。底部小字 Plug-in Frequency Adapter。 | AFDA 从屏幕下方弹入，像插件一样“咔哒”插进网络；箭头重新连线。 | 插一个 AFDA | AFDA 的思路很直接：先插在特征后面。 | AFDA.py 插入方式 + Manim 重绘 |
| 7-13s | 输入 X 先拆成 Low / High。Low 生成 Gate，High 进入 Light Conv，最后与原 X residual add。 | 不一次摆满；按节拍依次出现 X -> Low/High -> Gate/Light Conv -> 融合 -> Output。每步有 flash 和流动点。 | 低频看轮廓 / 高频看边缘 / Gate 决定怎么补 | 低频看轮廓，高频看边缘，再用 gate 决定怎么补。 | AFDA.py 结构 + Manim 简化重绘 |
| 13-17s | Before: Conv Block -> Next Layer。After: Conv -> AFDA -> Next。 | Before 先出现并变暗；AFDA 从下方弹入；After 连线高亮。 | 接在特征后 | 主干不用大改，Conv 后面接一下就行。 | AFDA.py 最小接入方式 + Manim 重绘 |
| 17-21s | 代码卡片逐行显示 3 行最小调用。第三行 `feat = self.afda(feat)` 高亮。 | 代码像打字机逐行 pop-in；第三行黄色框和 flash。 | 复制 3 行就能用 | 代码也很简单，三行就能跑。 | 模块代码 |
| 21-24s | 三张资料卡片弹出：PDF 笔记、PyTorch 代码、架构图拆解。AFDA logo 居中。 | 资料卡片快速堆叠弹出；AFDA logo flash；最终 hold 约 0.55s。 | 代码+笔记已整理 / 评论区打 AFDA | AFDA 的代码和论文笔记，我已经整理好了。 | 论文 PDF / 模块代码 / 架构图 |

## V2 视觉原则

- 开场不黑屏，第一帧必须有标题和 Source/Target 对比。
- 每 2-3 秒至少一次视觉变化：zoom、shake、flash、模块插入、代码逐行出现。
- 白底论文架构图本版不直接使用，机制全部用 Manim 简化重绘。
- 主标题控制在 12 个中文字以内，字幕尽量口语化。
- `episodes/afda_001/audio/voiceover.wav` 是 V1 旧音频，V2 不挂载，需重新 TTS。
