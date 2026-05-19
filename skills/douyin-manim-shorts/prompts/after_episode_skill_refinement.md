请根据本次视频制作过程，反向优化当前旧短视频制作 skill。

注意：
- 不要新建新的 skill；
- 不要删除旧 skill；
- 不要重写整个 skill；
- 只做增量优化；
- 保留旧 skill 原有能力；
- 本次优化必须来自真实制作过程中的问题和经验；
- 不要把单个视频的具体内容硬编码进 skill；
- 只沉淀可复用规则、模板、QA、脚本和流程。

请按以下流程执行。

一、定位旧 skill

先搜索并定位当前项目已有的短视频制作 skill。

重点查找：
- SKILL.md
- workflow.md
- prompt_commands.md
- visual_rules.md
- layout_rules.md
- qa_checklist.md
- templates/
- examples/
- references/
- scripts/

请输出：
1. 旧 skill 路径；
2. 当前 skill 核心文件；
3. 本次准备修改哪些文件；
4. 为什么修改这些文件。

二、复盘本次视频任务

请阅读本次 episode 目录中的文件：

- brief.md
- storyboard.md
- voiceover.txt
- subtitles.srt
- scene.py
- renders/contact_sheet.jpg
- qa_report.md
- renders/final_with_bgm.mp4，如果存在

请总结：

1. 本次视频做对了什么；
2. 本次视频哪里失败了；
3. 哪些问题是偶发问题；
4. 哪些问题是后续视频也可能反复出现的问题；
5. 哪些经验应该写进 skill；
6. 哪些内容只是当前模块特有，不能写进通用 skill。

三、提取可复用经验

请把本次经验分成三类：

A. 必须写入 skill 的硬规则  
例如：
- voiceover.txt 必须存在；
- 公式必须匹配 module_type；
- 非频域模块禁止复用 FFT；
- 最后 5 秒必须检查 CTA 重叠；
- 字幕不能低于安全区；
- 代码必须使用当前模块类名。

B. 可以写入模板的结构  
例如：
- module_brief 字段；
- storyboard 结构；
- voiceover 结构；
- scene.py 辅助函数；
- QA 报告字段；
- BGM 配置字段。

C. 只作为案例记录的经验  
例如：
- 某个模块的特殊视觉；
- 某个错误案例；
- 某次参数选择；
- 某个具体公式。

四、增量更新旧 skill

请把 A/B/C 三类经验分别写入旧 skill 的合适位置：

A 类硬规则：
写入 SKILL.md、workflow.md、qa_checklist.md 或 rules 文件。

B 类模板：
写入 templates/、prompt_commands.md、scene template 或 brief template。

C 类案例：
写入 examples/、case_studies/ 或 references/。

要求：
- 不要把当前模块名称硬编码成默认模板；
- 不要让后续视频都套用当前模块结构；
- 新规则必须支持多个模块类型；
- 更新内容要清楚、可执行；
- 不要重复写已有规则，如果已有类似规则，请合并和精简。

五、更新 QA 机制

请检查旧 skill 的 QA 是否覆盖本次问题。

如果没有，请补充检查项：

- 是否生成 voiceover.txt；
- voiceover.txt 是否非空；
- subtitles.srt 是否与 voiceover 匹配；
- 当前模块名是否正确；
- 上一个模块名是否残留；
- 当前公式是否匹配 module_type；
- 是否残留上一条视频公式；
- scene.py 是否残留旧模块标签；
- 最后 5 秒是否有文字重叠；
- CTA 是否分两行且不重叠；
- final_with_bgm.mp4 是否 has_audio；
- BGM 是否盖过人声；
- contact_sheet 是否存在；
- 每帧是否有明确主视觉。

六、更新防退化规则

请加入或维护一段“防退化规则”。

后续每次生成视频，必须避免：

1. 套壳上一条视频；
2. 缺失口播稿；
3. 公式与模块不匹配；
4. 代码类名不是当前模块；
5. CTA keyword 错误；
6. 最后几帧文字重叠；
7. BGM 缺失或盖过人声；
8. contact sheet 缺失；
9. QA 报告只写成功不写问题；
10. 把单个模块的视觉结构误当成通用模板。

七、生成 Skill 更新日志

请在旧 skill 中维护一个 changelog 或 skill_evolution.md。

每次优化都追加一条记录：

日期：
本次 episode：
发现的问题：
新增规则：
修改模板：
修改脚本：
仍待改进：
是否已通过 QA：

不要覆盖历史记录，只追加。

八、必要时更新脚本

如果本次问题可以用脚本自动检查，请更新或新增脚本。

优先考虑：
- qa_video.py
- check_episode_consistency.py
- check_template_leakage.py
- register_bgm.py
- mix_audio.py

但不要为了写脚本而写脚本。
如果暂时无法自动检查，就在 qa_checklist.md 中加入人工检查项。

九、提交 Git

完成 skill 更新后：

1. 运行 git status；
2. 检查不要提交大型 mp4、wav、Manim cache、临时渲染；
3. 如有必要更新 .gitignore；
4. 只提交 skill 文档、模板、脚本、prompt、QA 规则、changelog；
5. 执行：

git add <相关文件>
git commit -m "Refine video skill from latest episode feedback"
git push

十、最终输出报告

请告诉我：

1. 本次复盘的 episode 是哪个；
2. 旧 skill 路径是什么；
3. 修改了哪些文件；
4. 新增了哪些硬规则；
5. 新增或修改了哪些模板；
6. 新增或修改了哪些 QA；
7. 哪些经验只记录为案例，没有写成通用规则；
8. 是否更新 skill_evolution.md；
9. 是否提交 Git；
10. commit hash 是什么；
11. 下一次生成视频前，我需要额外提供哪些 brief 信息。