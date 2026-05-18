# AFDA V2 Visual Notes

- V2 目标：从课程 PPT 感改成快节奏短视频剪辑感。
- 本版 `scene.py` 不挂载 `audio/voiceover.wav`，因为该文件对应 V1 口播。
- 重新 TTS 时，应使用 `voiceover.txt` 的 V2 文案，并覆盖或另存为新的 `audio/voiceover.wav`。
- 画面节奏点：
  - 0s：第一帧直接出现强钩子和 Source/Target 对比。
  - 1.5s：进入分布偏移和 mask 错位。
  - 4s：AFDA 插件弹入网络。
  - 7s：机制拆解开始，逐步出现 Low / High / Gate / Light Conv。
  - 13s：Before/After 插入位置对比。
  - 17s：三行代码逐行出现。
  - 21s：资料包 CTA。
- 事实边界：只讲 `AFDA.py` 中轻量频域适配器的即插即用用法，不扩展成完整 AFDAN 训练框架。
