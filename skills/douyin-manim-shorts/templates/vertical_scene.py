from manim import *
from pathlib import Path

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 9
config.frame_height = 16
config.background_color = "#10131A"

VOICEOVER_PATH = "audio/voiceover.wav"
FINAL_HOLD_SECONDS = 1.0

FONT = "Microsoft YaHei"
BG = "#10131A"
PANEL = "#171C24"
PANEL_SOFT = "#202633"
TEXT = "#F6F7FB"
TEXT_MUTED = "#A7B0C0"
ACCENT = "#FFD166"
ACCENT_2 = "#4CC9F0"
ALERT = "#EF476F"

TITLE_SIZE = 62
BODY_SIZE = 38
LABEL_SIZE = 28
TAG_SIZE = 24
FORMULA_SIZE = 34

TITLE_Y = 6.35
MAIN_CENTER_Y = 1.2
FORMULA_Y = -4.25
SUBTITLE_Y = -6.1

# Deep learning plug-in module safe zones. Use these when building compact
# 20-30 second module videos with formulas, gates, spectra, and code panels.
PLUGIN_TITLE_Y_RANGE = (3.0, 3.7)
PLUGIN_MAIN_Y_RANGE = (-1.8, 2.2)
PLUGIN_SUBTITLE_Y = -3.15
PLUGIN_CTA_MIN_Y = -3.25
PLUGIN_CORE_X_RANGE = (-3.0, 3.0)


class DouyinShortTemplate(Scene):
    def make_title(self, text):
        title = Text(text, font=FONT, font_size=TITLE_SIZE, weight=BOLD, color=TEXT)
        title.scale_to_fit_width(8.0)
        return title.move_to(UP * TITLE_Y)

    def make_subtitle(self, text):
        box = RoundedRectangle(
            width=7.8,
            height=0.72,
            corner_radius=0.12,
            stroke_width=0,
            fill_color=BLACK,
            fill_opacity=0.62,
        )
        label = Text(text, font=FONT, font_size=BODY_SIZE, color=TEXT)
        label.scale_to_fit_width(7.25)
        group = VGroup(box, label).move_to(UP * SUBTITLE_Y)
        return group

    def make_chip(self, text, color=TEXT, width=1.55):
        box = RoundedRectangle(
            width=width,
            height=0.62,
            corner_radius=0.14,
            stroke_width=2,
            stroke_color=color,
            fill_color=PANEL,
            fill_opacity=0.95,
        )
        label = Text(text, font=FONT, font_size=LABEL_SIZE, color=color, weight=BOLD)
        label.scale_to_fit_width(width - 0.22)
        return VGroup(box, label)

    def make_label_box(self, text, color=ACCENT_2, scale=0.52):
        """Auto-fit label for module names such as Low, High, Gate, AFDA."""
        label = Text(
            text,
            font=FONT,
            font_size=34,
            color=color,
            weight=BOLD,
            line_spacing=0.8,
        )
        label.scale(scale)
        box = SurroundingRectangle(
            label,
            buff=0.18,
            corner_radius=0.12,
            color=color,
            stroke_width=2.5,
        )
        box.set_fill(PANEL, opacity=0.9)
        return VGroup(box, label)

    def make_glow_arrow(self, start, end, color=ACCENT_2, buff=0.12):
        arrow = Arrow(start, end, buff=buff, color=color, stroke_width=5, max_tip_length_to_length_ratio=0.18)
        glow = arrow.copy().set_stroke(color=color, width=11, opacity=0.18)
        return VGroup(glow, arrow)

    def subtitle_swap(self, current, text):
        new_subtitle = self.make_subtitle(text)
        self.play(ReplacementTransform(current, new_subtitle), run_time=0.35)
        return new_subtitle

    def make_formula(self, tex, font_size=36):
        formula = MathTex(tex, font_size=font_size, color=TEXT)
        formula.set_stroke(BLACK, width=4, background=True)
        return formula

    def construct(self):
        if Path(VOICEOVER_PATH).exists():
            self.add_sound(VOICEOVER_PATH)

        title = self.make_title("30秒看懂一个概念")
        subtitle = self.make_subtitle("先抛出一个反直觉问题")

        dot_a = Dot(LEFT * 2.4 + UP * MAIN_CENTER_Y, color=ACCENT_2)
        dot_b = Dot(RIGHT * 2.4 + UP * MAIN_CENTER_Y, color=ACCENT_2)
        dot_c = Dot(DOWN * 1.25, color=ACCENT)
        triangle = Polygon(
            dot_a.get_center(),
            dot_b.get_center(),
            dot_c.get_center(),
            color=ACCENT,
            stroke_width=6,
        )
        question = Text("为什么这里会变?", font=FONT, font_size=BODY_SIZE, color=ACCENT, weight=BOLD).next_to(
            triangle, DOWN, buff=0.7
        )
        question.scale_to_fit_width(7.6)

        self.play(FadeIn(title, shift=DOWN * 0.2), FadeIn(subtitle), run_time=0.7)
        self.play(LaggedStart(FadeIn(dot_a), FadeIn(dot_b), FadeIn(dot_c), lag_ratio=0.2))
        self.play(Create(triangle), FadeIn(question, shift=UP * 0.2))
        self.wait(0.4)

        subtitle = self.subtitle_swap(subtitle, "用一个动画把它拆开")
        arrows = VGroup(
            Arrow(dot_a.get_center(), dot_c.get_center(), buff=0.15, color=ACCENT_2),
            Arrow(dot_b.get_center(), dot_c.get_center(), buff=0.15, color=ACCENT_2),
        )
        self.play(Create(arrows), dot_c.animate.scale(1.6), run_time=1.0)
        self.play(dot_c.animate.scale(1 / 1.6), run_time=0.35)

        subtitle = self.subtitle_swap(subtitle, "最后只留一句能记住的话")
        formula = self.make_formula(
            r"\mathrm{Concept}=\mathrm{Objects}+\mathrm{Relations}",
            font_size=FORMULA_SIZE,
        )
        formula.scale_to_fit_width(7.8)
        formula.move_to(UP * FORMULA_Y)
        self.play(Write(formula), run_time=0.65)

        takeaway = Text("复杂概念 = 关系的变化", font=FONT, font_size=BODY_SIZE, color=ACCENT, weight=BOLD)
        takeaway.scale_to_fit_width(7.8)
        takeaway.move_to(UP * 3.9)
        self.play(ReplacementTransform(question, takeaway), run_time=0.7)
        self.wait(FINAL_HOLD_SECONDS)
