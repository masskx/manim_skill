from __future__ import annotations

from pathlib import Path

import numpy as np
from manim import *


config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 7.2
config.frame_height = 12.8
config.background_color = "#0E121B"


FONT = "Microsoft YaHei"
BG = "#0E121B"
PANEL = "#151B27"
TEXT = "#F4F7FB"
MUTED = "#9DA8B8"
CYAN = "#55D7F7"
YELLOW = "#F5C84C"
GREEN = "#75D783"
PINK = "#FF6B9A"
RED = "#EF476F"


class SEFNModuleShort(Scene):
    def fit(self, mob: Mobject, width: float = 6.1) -> Mobject:
        if mob.width > width:
            mob.scale_to_fit_width(width)
        return mob

    def text(self, value: str, size: int = 34, color: str = TEXT, weight=NORMAL) -> Text:
        t = Text(value, font=FONT, font_size=size, color=color, weight=weight)
        return self.fit(t)

    def title(self, value: str, color: str = TEXT) -> Text:
        return self.text(value, 50, color, BOLD).move_to([0, 3.25, 0])

    def subtitle(self, value: str) -> VGroup:
        label = self.text(value, 31, TEXT, BOLD)
        box = SurroundingRectangle(label, buff=0.15, corner_radius=0.12, stroke_width=0)
        box.set_fill(BLACK, opacity=0.58)
        return VGroup(box, label).move_to([0, -3.05, 0]).set_z_index(9)

    def chip(self, value: str, color: str = CYAN, width: float = 1.5) -> VGroup:
        box = RoundedRectangle(
            width=width,
            height=0.56,
            corner_radius=0.12,
            stroke_width=2.2,
            stroke_color=color,
            fill_color=PANEL,
            fill_opacity=0.96,
        )
        label = self.text(value, 23, color, BOLD)
        self.fit(label, width - 0.18)
        label.move_to(box)
        return VGroup(box, label)

    def grid(self, color: str = CYAN, rows: int = 4, cols: int = 4, cell: float = 0.31) -> VGroup:
        g = VGroup()
        for r in range(rows):
            for c in range(cols):
                sq = Square(side_length=cell, stroke_color=color, stroke_width=1.1)
                sq.set_fill(color, opacity=0.08 + 0.04 * ((r + c) % 2))
                sq.move_to([(c - (cols - 1) / 2) * cell, ((rows - 1) / 2 - r) * cell, 0])
                g.add(sq)
        return g

    def edge_arrow(self, start: Mobject, end: Mobject, color: str = CYAN) -> Arrow:
        return Arrow(
            start.get_right() + RIGHT * 0.05,
            end.get_left() + LEFT * 0.05,
            buff=0,
            color=color,
            stroke_width=3,
            max_tip_length_to_length_ratio=0.18,
        )

    def clear(self, group: Mobject) -> None:
        self.play(FadeOut(group), run_time=0.25)

    def construct(self):
        episode_dir = Path(__file__).resolve().parent
        voiceover = episode_dir / "audio" / "voiceover.wav"
        if not voiceover.exists():
            raise FileNotFoundError(f"Missing voiceover audio: {voiceover}")
        self.add_sound(str(voiceover))

        phase = ValueTracker(0)
        phase.add_updater(lambda m, dt: m.increment_value(dt))
        bg_grid = NumberPlane(
            x_range=(-4, 4, 0.8),
            y_range=(-6.5, 6.5, 0.8),
            background_line_style={"stroke_color": "#253047", "stroke_width": 1, "stroke_opacity": 0.16},
            axis_config={"stroke_opacity": 0},
        )
        halo = always_redraw(
            lambda: Circle(radius=2.5 + 0.08 * np.sin(phase.get_value()), color=CYAN, stroke_width=2)
            .set_opacity(0.07)
            .move_to([0, 0.05, 0])
        )
        wave = always_redraw(
            lambda: ParametricFunction(
                lambda u: np.array([u, -3.75 + 0.06 * np.sin(2.2 * u + phase.get_value()), 0]),
                t_range=(-3.2, 3.2),
                color=GREEN,
                stroke_width=2,
            ).set_opacity(0.24)
        )
        self.add(phase, bg_grid, halo, wave)

        # 0-2.6s: strong hook.
        title = self.title("Mamba 丢局部？", YELLOW)
        sefn = self.chip("SEFN", CYAN, 1.35).move_to([0, 1.65, 0])
        grid = self.grid(CYAN, 4, 4, 0.34).move_to([-0.72, 0.1, 0])
        lost = self.grid(RED, 2, 2, 0.28).move_to([1.15, 0.1, 0]).set_opacity(0.75)
        sub = self.subtitle("Mamba 看得远，但会丢局部")
        hook = VGroup(title, sefn, grid, lost, sub)
        self.play(FadeIn(title, scale=0.96), FadeIn(grid), run_time=0.45)
        self.play(FadeIn(lost), FadeIn(sefn, scale=1.1), FadeIn(sub), run_time=0.55)
        self.wait(1.15)
        self.clear(hook)

        # 2.6-8.0s: spatial branch, then compress to S.
        title = self.title("空间提示 S", GREEN)
        spatial = self.chip("spatial", GREEN, 1.45).move_to([-2.25, 0.35, 0])
        pool = self.chip("Pool", YELLOW, 1.15).move_to([-0.72, 0.35, 0])
        conv = self.chip("Conv", CYAN, 1.15).move_to([0.72, 0.35, 0])
        s = self.chip("S", GREEN, 1.0).move_to([2.15, 0.35, 0])
        arrows = VGroup(self.edge_arrow(spatial, pool, YELLOW), self.edge_arrow(pool, conv, CYAN), self.edge_arrow(conv, s, GREEN))
        sub = self.subtitle("池化加卷积，做成空间提示")
        branch = VGroup(title, spatial, pool, conv, s, arrows, sub)
        self.play(FadeIn(title), FadeIn(spatial), FadeIn(sub), run_time=0.4)
        self.play(FadeIn(pool), GrowArrow(arrows[0]), run_time=0.45)
        self.play(FadeIn(conv), GrowArrow(arrows[1]), run_time=0.45)
        self.play(FadeIn(s), GrowArrow(arrows[2]), Circumscribe(s, color=GREEN), run_time=0.7)
        self.wait(1.45)
        s_token = s.copy().move_to([-2.35, 0.85, 0])
        self.play(Transform(branch, VGroup(s_token)), run_time=0.45)
        self.remove(branch)
        self.add(s_token)

        # 8.0-12.5s: split after-Mamba feature.
        title = self.title("切成两支", CYAN)
        x = self.chip("x after Mamba", CYAN, 2.1).move_to([-2.0, -0.25, 0])
        x1 = self.chip("x1", GREEN, 1.0).move_to([1.15, 0.45, 0])
        x2 = self.chip("x2", PINK, 1.0).move_to([1.15, -0.95, 0])
        a1 = Arrow(x.get_right(), x1.get_left(), buff=0.08, color=GREEN, stroke_width=3)
        a2 = Arrow(x.get_right(), x2.get_left(), buff=0.08, color=PINK, stroke_width=3)
        sub = self.subtitle("Mamba 后的特征切成两支")
        split = VGroup(title, x, x1, x2, a1, a2, sub)
        self.play(FadeIn(title), FadeIn(x), FadeIn(sub), run_time=0.4)
        self.play(FadeIn(x1), FadeIn(x2), GrowArrow(a1), GrowArrow(a2), run_time=0.75)
        self.wait(1.65)
        self.clear(VGroup(title, x, a1, a2, sub))

        # 12.5-18s: S -> x1 -> gate x2 -> Y.
        title = self.title("空间增强前馈", YELLOW)
        s_token.move_to([-2.15, 0.9, 0])
        x1.move_to([-2.15, -0.1, 0])
        fuse = self.chip("Fuse", CYAN, 1.25).move_to([-0.55, 0.4, 0])
        gelu = self.chip("GELU", YELLOW, 1.25).move_to([0.82, 0.4, 0])
        x2.move_to([0.82, -0.85, 0])
        y = self.chip("Y", CYAN, 1.0).move_to([2.3, 0.4, 0])
        dot = MathTex(r"\odot", font_size=34, color=YELLOW).move_to([1.58, 0.4, 0])
        flow = VGroup(
            Arrow(s_token.get_right(), fuse.get_left(), buff=0.08, color=GREEN, stroke_width=3),
            Arrow(x1.get_right(), fuse.get_left(), buff=0.08, color=GREEN, stroke_width=3),
            self.edge_arrow(fuse, gelu, CYAN),
            Arrow(gelu.get_right(), dot.get_left(), buff=0.08, color=YELLOW, stroke_width=3),
            Arrow(x2.get_top(), dot.get_bottom(), buff=0.08, color=PINK, stroke_width=3),
            Arrow(dot.get_right(), y.get_left(), buff=0.08, color=CYAN, stroke_width=3),
        )
        sub = self.subtitle("S 融合 x1，再调制 x2")
        gate = VGroup(title, s_token, x1, fuse, gelu, x2, y, dot, flow, sub)
        self.play(FadeIn(title), FadeIn(sub), FadeIn(fuse), GrowArrow(flow[0]), GrowArrow(flow[1]), run_time=0.65)
        self.play(FadeIn(gelu), GrowArrow(flow[2]), FadeIn(dot), GrowArrow(flow[3]), GrowArrow(flow[4]), run_time=0.75)
        self.play(FadeIn(y), GrowArrow(flow[5]), Circumscribe(dot, color=YELLOW), run_time=0.75)
        self.wait(1.45)
        self.clear(gate)

        # 18-21s: quick disambiguation.
        title = self.title("不是这些", TEXT)
        no_attn = self.chip("不是注意力", RED, 1.8).move_to([-1.45, 0.35, 0])
        no_freq = self.chip("不是频域", RED, 1.65).move_to([1.45, 0.35, 0])
        yes = self.chip("空间增强 FFN", GREEN, 2.35).move_to([0, -0.65, 0])
        sub = self.subtitle("它就是空间增强前馈")
        clarify = VGroup(title, no_attn, no_freq, yes, sub)
        self.play(FadeIn(title), FadeIn(no_attn), FadeIn(no_freq), FadeIn(sub), run_time=0.5)
        self.play(FadeIn(yes), no_attn.animate.set_opacity(0.45), no_freq.animate.set_opacity(0.45), run_time=0.55)
        self.wait(1.15)
        self.clear(clarify)

        # 21-25s: code and CTA.
        title = self.title("三行接入", CYAN)
        lines = VGroup(
            Text("self.sefn = SEFN(dim, 2, True)", font="Consolas", font_size=22, color=CYAN),
            Text("y = mamba_block(x)", font="Consolas", font_size=22, color=TEXT),
            Text("out = self.sefn(y, x)", font="Consolas", font_size=22, color=YELLOW),
        ).arrange(DOWN, aligned_edge=LEFT, buff=0.2)
        self.fit(lines, 5.5)
        panel = SurroundingRectangle(lines, buff=0.25, corner_radius=0.12, color=CYAN, stroke_width=2)
        panel.set_fill(PANEL, opacity=0.93)
        code = VGroup(panel, lines).move_to([0, 0.55, 0])
        cta = VGroup(
            self.text("PDF笔记 + PyTorch代码 + 架构图", 26, TEXT),
            self.text("评论区打：SEFN", 34, YELLOW, BOLD),
        ).arrange(DOWN, buff=0.15).move_to([0, -1.75, 0])
        sub = self.subtitle("评论区打 SEFN")
        ending = VGroup(title, code, cta, sub)
        self.play(FadeIn(title), FadeIn(code), FadeIn(sub), run_time=0.45)
        self.play(Circumscribe(lines[2], color=YELLOW), FadeIn(cta), run_time=0.75)
        self.wait(6.7)
