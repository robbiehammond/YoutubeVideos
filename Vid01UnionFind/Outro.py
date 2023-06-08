from manim import *

class Outro(Scene):
    def construct(self):
        self.wait(3)
        myBaseTemplate = TexTemplate(
            documentclass="\documentclass[preview]{standalone}"
        )
        myBaseTemplate.add_to_preamble(r"\usepackage{ragged2e}")

        text = Tex(
            "\\justifying{See the Description for Additional Notes and Resources}",
            tex_template=myBaseTemplate,
            font_size=72
        ).scale(0.6)
        text2 = Tex(r"$\downarrow$", font_size=108).shift(1 * DOWN)
        self.play(FadeIn(text))
        self.play(FadeIn(text2))
        self.wait(25)