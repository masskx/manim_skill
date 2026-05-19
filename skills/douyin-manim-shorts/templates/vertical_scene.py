from manim import *
import numpy as np
from pathlib import Path

config.pixel_width = 1080
config.pixel_height = 1920
config.frame_width = 7.2
config.frame_height = 12.8
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

TITLE_Y = 3.25
MAIN_CENTER_Y = 0.5
FORMULA_Y = 1.6
SUBTITLE_Y = -3.0

# Layout-first 9:16 zones for plug-in module shorts.
# Every page should choose a scene type, layout template, and visual layer plan before animation.
SAFE_X_MIN, SAFE_X_MAX = -3.1, 3.1
SAFE_Y_MIN, SAFE_Y_MAX = -3.35, 3.65
ZONES = {
    "title_zone": {"center": [0, 3.25, 0], "max_width": config.frame_width * 0.86, "max_height": 0.8},
    "visual_zone": {"center": [0, 0.50, 0], "max_width": config.frame_width * 0.86, "max_height": 3.9},
    "formula_zone": {"center": [0, 1.60, 0], "max_width": config.frame_width * 0.82, "max_height": 1.2},
    "diagram_zone": {"center": [0, 0.10, 0], "max_width": config.frame_width * 0.86, "max_height": 2.3},
    "annotation_zone": {"center": [0, -1.40, 0], "max_width": config.frame_width * 0.82, "max_height": 0.55},
    "code_zone": {"center": [0, 0.45, 0], "max_width": config.frame_width * 0.86, "max_height": 2.5},
    "subtitle_zone": {"center": [0, -3.00, 0], "max_width": config.frame_width * 0.88, "max_height": 0.55},
    "cta_zone": {"center": [0, -2.10, 0], "max_width": config.frame_width * 0.86, "max_height": 0.9},
}
LAYERS = {
    "background": 0,
    "grid": 1,
    "arrows": 2,
    "diagram": 3,
    "formula": 4,
    "labels": 5,
    "subtitles": 6,
    "cta": 7,
}
COLLISION_PAIRS = {
    ("formula", "diagram"),
    ("formula", "arrows"),
    ("formula", "title"),
    ("arrows", "labels"),
    ("arrows", "code_panel"),
    ("cta", "subtitle"),
    ("diagram", "subtitle"),
    ("code_panel", "cta"),
}


class DouyinShortTemplate(Scene):
    def safe_scale_to_width(self, mobject, max_width):
        if mobject.width > max_width:
            mobject.scale_to_fit_width(max_width)
        return mobject

    def safe_scale_to_height(self, mobject, max_height):
        if mobject.height > max_height:
            mobject.scale_to_fit_height(max_height)
        return mobject

    def fit_to_box(self, mobject, max_width, max_height):
        self.safe_scale_to_width(mobject, max_width)
        self.safe_scale_to_height(mobject, max_height)
        return mobject

    def place_in_zone(self, mobject, zone_name):
        zone = ZONES[zone_name]
        self.fit_to_box(mobject, zone["max_width"], zone["max_height"])
        mobject.move_to(zone["center"])
        return mobject

    def set_layer(self, mobject, layer_name):
        mobject.set_z_index(LAYERS[layer_name])
        return mobject

    def arrange_without_overlap(self, group, direction=DOWN, buff=0.25):
        group.arrange(direction, buff=max(buff, 0.25))
        return group

    def _bbox(self, mobject):
        return (mobject.get_left()[0], mobject.get_right()[0], mobject.get_bottom()[1], mobject.get_top()[1])

    def _boxes_overlap(self, a, b, pad=0.04):
        ax1, ax2, ay1, ay2 = self._bbox(a)
        bx1, bx2, by1, by2 = self._bbox(b)
        return ax1 < bx2 - pad and ax2 > bx1 + pad and ay1 < by2 - pad and ay2 > by1 + pad

    def check_overlaps(self, mobjects, label="scene"):
        warnings = []
        visible = [m for m in mobjects if m is not None]
        for i, a in enumerate(visible):
            if a.width > config.frame_width * 0.90:
                warnings.append(f"{label}: object {i} exceeds 90% frame width")
            if a.get_left()[0] < SAFE_X_MIN or a.get_right()[0] > SAFE_X_MAX:
                warnings.append(f"{label}: object {i} outside safe x range")
            if a.get_bottom()[1] < SAFE_Y_MIN or a.get_top()[1] > SAFE_Y_MAX:
                warnings.append(f"{label}: object {i} outside safe y range")
            for j, b in enumerate(visible[i + 1 :], start=i + 1):
                if self._boxes_overlap(a, b):
                    warnings.append(f"{label}: object {i} overlaps object {j}")
        for warning in warnings:
            print("[layout-warning]", warning)
        return warnings

    def check_collision(self, named_mobjects, label="scene"):
        warnings = []
        visible = [(name, mob) for name, mob in named_mobjects if mob is not None]
        for i, (name_a, mob_a) in enumerate(visible):
            for name_b, mob_b in visible[i + 1:]:
                if (name_a, name_b) in COLLISION_PAIRS or (name_b, name_a) in COLLISION_PAIRS:
                    if self._boxes_overlap(mob_a, mob_b):
                        warnings.append(f"{label}: {name_a} collides with {name_b}")
        for warning in warnings:
            print("[collision-warning]", warning)
        return warnings

    def edge_point(self, mobject, side, buff=0.08):
        if side == "right":
            return mobject.get_right() + RIGHT * buff
        if side == "left":
            return mobject.get_left() + LEFT * buff
        if side == "top":
            return mobject.get_top() + UP * buff
        if side == "bottom":
            return mobject.get_bottom() + DOWN * buff
        return mobject.get_center()

    def make_safe_title(self, text):
        title = Text(text, font=FONT, font_size=TITLE_SIZE, weight=BOLD, color=TEXT)
        self.set_layer(title, "labels")
        return self.place_in_zone(title, "title_zone")

    def make_title(self, text):
        return self.make_safe_title(text)

    def make_subtitle(self, text):
        label = Text(text, font=FONT, font_size=BODY_SIZE, color=TEXT)
        self.safe_scale_to_width(label, ZONES["subtitle_zone"]["max_width"])
        box = SurroundingRectangle(label, buff=0.18, corner_radius=0.12, color=BLACK, stroke_width=0)
        box.set_fill(BLACK, opacity=0.62)
        group = VGroup(box, label)
        self.set_layer(group, "subtitles")
        return self.place_in_zone(group, "subtitle_zone")

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
        group = VGroup(box, label)
        self.set_layer(group, "diagram")
        label.set_z_index(LAYERS["labels"])
        return group

    def make_label_box(self, text, color=ACCENT_2, font_size=30):
        """Auto-fit label. Never use a fixed Rectangle wrapper for text."""
        label = Text(
            text,
            font=FONT,
            font_size=font_size,
            color=color,
            weight=BOLD,
            line_spacing=0.8,
        )
        self.safe_scale_to_width(label, config.frame_width * 0.32)
        box = SurroundingRectangle(
            label,
            buff=0.18,
            corner_radius=0.12,
            color=color,
            stroke_width=2.5,
        )
        box.set_fill(PANEL, opacity=0.9)
        group = VGroup(box, label)
        self.set_layer(group, "labels")
        return group

    def make_glow_arrow(self, start_obj, end_obj, color=ACCENT_2, start_side="right", end_side="left", buff=0.08):
        start = self.edge_point(start_obj, start_side, buff=buff)
        end = self.edge_point(end_obj, end_side, buff=buff)
        arrow = Arrow(start, end, buff=0, color=color, stroke_width=2.6, max_tip_length_to_length_ratio=0.18)
        glow = arrow.copy().set_stroke(color=color, width=7, opacity=0.14)
        group = VGroup(glow, arrow)
        self.set_layer(group, "arrows")
        return group

    def make_elbow_arrow(self, start_obj, end_obj, direction="right", color=ACCENT_2, stroke_width=2.4):
        """Route around middle content. Prefer this when a direct edge arrow would cross text/formula."""
        if direction in ("right", "left_to_right"):
            p1 = self.edge_point(start_obj, "right")
            p4 = self.edge_point(end_obj, "left")
            mid_x = (p1[0] + p4[0]) / 2
            p2 = np.array([mid_x, p1[1], 0])
            p3 = np.array([mid_x, p4[1], 0])
        elif direction in ("down", "top_to_bottom"):
            p1 = self.edge_point(start_obj, "bottom")
            p4 = self.edge_point(end_obj, "top")
            mid_y = (p1[1] + p4[1]) / 2
            p2 = np.array([p1[0], mid_y, 0])
            p3 = np.array([p4[0], mid_y, 0])
        else:
            p1 = self.edge_point(start_obj, "right")
            p4 = self.edge_point(end_obj, "left")
            mid_x = (p1[0] + p4[0]) / 2
            p2 = np.array([mid_x, p1[1], 0])
            p3 = np.array([mid_x, p4[1], 0])
        line = VMobject(color=color, stroke_width=stroke_width)
        line.set_points_as_corners([p1, p2, p3, p4])
        tip = ArrowTriangleFilledTip(color=color).scale(0.16)
        tip.move_to(p4)
        tip.rotate(line.get_angle())
        group = VGroup(line, tip)
        self.set_layer(group, "arrows")
        return group

    def subtitle_swap(self, current, text):
        new_subtitle = self.make_subtitle(text)
        self.play(ReplacementTransform(current, new_subtitle), run_time=0.35)
        return new_subtitle

    def make_formula(self, tex, font_size=36):
        formula = MathTex(tex, font_size=font_size, color=TEXT)
        formula.set_stroke(BLACK, width=4, background=True)
        self.set_layer(formula, "formula")
        return self.fit_to_box(formula, config.frame_width * 0.78, ZONES["formula_zone"]["max_height"])

    def construct(self):
        if Path(VOICEOVER_PATH).exists():
            self.add_sound(VOICEOVER_PATH)

        # Layout plan: hook_scene -> title_visual_subtitle_layout.
        # Place static objects first, run overlap checks, then animate.

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
        self.safe_scale_to_width(question, ZONES["visual_zone"]["max_width"])
        visual_group = VGroup(dot_a, dot_b, dot_c, triangle, question)
        self.fit_to_box(visual_group, ZONES["visual_zone"]["max_width"], ZONES["visual_zone"]["max_height"])
        self.check_overlaps([title, visual_group, subtitle], label="hook_scene")
        self.check_collision([("title", title), ("diagram", visual_group), ("subtitle", subtitle)], label="hook_scene")

        self.play(FadeIn(title, shift=DOWN * 0.2), FadeIn(subtitle), run_time=0.7)
        self.play(LaggedStart(FadeIn(dot_a), FadeIn(dot_b), FadeIn(dot_c), lag_ratio=0.2))
        self.play(Create(triangle), FadeIn(question, shift=UP * 0.2))
        self.wait(0.4)

        subtitle = self.subtitle_swap(subtitle, "用一个动画把它拆开")
        arrows = VGroup(
            self.make_glow_arrow(dot_a, dot_c, start_side="bottom", end_side="left", color=ACCENT_2),
            self.make_glow_arrow(dot_b, dot_c, start_side="bottom", end_side="right", color=ACCENT_2),
        )
        self.check_collision([("diagram", visual_group), ("arrows", arrows), ("subtitle", subtitle)], label="arrow_scene")
        self.play(Create(arrows), dot_c.animate.scale(1.6), run_time=1.0)
        self.play(dot_c.animate.scale(1 / 1.6), run_time=0.35)

        subtitle = self.subtitle_swap(subtitle, "最后只留一句能记住的话")
        formula = self.make_formula(
            r"\mathrm{Concept}=\mathrm{Objects}+\mathrm{Relations}",
            font_size=FORMULA_SIZE,
        )
        self.place_in_zone(formula, "formula_zone")
        self.check_overlaps([title, triangle, formula, subtitle], label="formula_scene")
        self.check_collision([("title", title), ("formula", formula), ("diagram", triangle), ("subtitle", subtitle)], label="formula_scene")
        self.play(Write(formula), run_time=0.65)

        takeaway = Text("复杂概念 = 关系的变化", font=FONT, font_size=BODY_SIZE, color=ACCENT, weight=BOLD)
        self.place_in_zone(takeaway, "title_zone")
        self.play(ReplacementTransform(question, takeaway), run_time=0.7)
        self.wait(FINAL_HOLD_SECONDS)
