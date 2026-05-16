from manim import *
from pathlib import Path

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#10131A"

VOICEOVER_PATH = "audio/voiceover.wav"
FINAL_HOLD_SECONDS = 1.0

TITLE_Y = 6.35
MAIN_CENTER_Y = 1.2
FORMULA_Y = -4.25
SUBTITLE_Y = -6.1


class DouyinShortTemplate(Scene):
    def make_title(self, text):
        title = Text(text, font_size=64, weight=BOLD, color=WHITE)
        title.scale_to_fit_width(8.0)
        return title.move_to(UP * TITLE_Y)

    def make_subtitle(self, text):
        box = RoundedRectangle(
            width=7.8,
            height=0.72,
            corner_radius=0.12,
            stroke_width=0,
            fill_color=BLACK,
            fill_opacity=0.55,
        )
        label = Text(text, font_size=38, color=WHITE)
        group = VGroup(box, label).move_to(UP * SUBTITLE_Y)
        return group

    def subtitle_swap(self, current, text):
        new_subtitle = self.make_subtitle(text)
        self.play(ReplacementTransform(current, new_subtitle), run_time=0.35)
        return new_subtitle

    def make_formula(self, tex, font_size=36):
        formula = MathTex(tex, font_size=font_size, color=WHITE)
        formula.set_stroke(BLACK, width=4, background=True)
        return formula

    def construct(self):
        if Path(VOICEOVER_PATH).exists():
            self.add_sound(VOICEOVER_PATH)

        title = self.make_title("30秒看懂一个概念")
        subtitle = self.make_subtitle("先抛出一个反直觉问题")

        dot_a = Dot(LEFT * 2.4 + UP * 1.2, color=BLUE_C)
        dot_b = Dot(RIGHT * 2.4 + UP * 1.2, color=BLUE_C)
        dot_c = Dot(DOWN * 1.6, color=YELLOW)
        triangle = Polygon(
            dot_a.get_center(),
            dot_b.get_center(),
            dot_c.get_center(),
            color=YELLOW,
            stroke_width=6,
        )
        question = Text("为什么这里会发生变化?", font_size=42, color=YELLOW).next_to(
            triangle, DOWN, buff=0.7
        )

        self.play(FadeIn(title, shift=DOWN * 0.2), FadeIn(subtitle), run_time=0.7)
        self.play(LaggedStart(FadeIn(dot_a), FadeIn(dot_b), FadeIn(dot_c), lag_ratio=0.2))
        self.play(Create(triangle), FadeIn(question, shift=UP * 0.2))
        self.wait(0.4)

        subtitle = self.subtitle_swap(subtitle, "用一个动画把它拆开")
        arrows = VGroup(
            Arrow(dot_a.get_center(), dot_c.get_center(), buff=0.15, color=BLUE_B),
            Arrow(dot_b.get_center(), dot_c.get_center(), buff=0.15, color=BLUE_B),
        )
        self.play(Create(arrows), dot_c.animate.scale(1.6), run_time=1.0)
        self.play(dot_c.animate.scale(1 / 1.6), run_time=0.35)

        subtitle = self.subtitle_swap(subtitle, "最后只留一句能记住的话")
        formula = self.make_formula(
            r"\mathrm{Concept}=\mathrm{Objects}+\mathrm{Relations}",
            font_size=34,
        )
        formula.scale_to_fit_width(7.8)
        formula.move_to(UP * FORMULA_Y)
        self.play(Write(formula), run_time=0.65)

        takeaway = Text("复杂概念 = 关系的变化", font_size=48, color=YELLOW)
        takeaway.move_to(UP * 3.9)
        self.play(ReplacementTransform(question, takeaway), run_time=0.7)
        self.wait(FINAL_HOLD_SECONDS)
