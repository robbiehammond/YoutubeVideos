from manim import * 

'''
    TODO: Record Vocals Intro, create animations in FCP for "First paragraph of "What is it chapter"
          - With whatever time, get started on this part.
'''

class Name(Scene):
    def construct(self):
        union = Tex('Union', font_size=64, color=RED).shift(LEFT + UP)
        find = Tex('Find', font_size=64, color=BLUE).shift(RIGHT + UP)

        self.add(union)
        self.add(find)

        self.play(Create(union), Create(find), run_time=1.5)

        self.wait(6)

        union_func_arrow = Arrow(start = LEFT + .75 * UP, end = 3 * LEFT + 1.5 * DOWN, stroke_width = 3)
        union_func = Tex(r"$Union(A, B) \rightarrow Do\ (setA \cup setB)$", font_size=36).shift(4 * LEFT + 2 * DOWN)
        union_func2 = Tex(r"$Union(A, A) \rightarrow Do\ Nothing$", font_size=36).shift(4 * LEFT + 2.75 * DOWN)

        self.play(Create(union_func), Create(union_func_arrow))
        self.wait(4)
        self.play(Create(union_func2))

        self.wait(3)

        find_func = Tex(r"$Find(A) \rightarrow Return\ representative\ of\ setA$", font_size=36).shift(3 * RIGHT + 2.35 * DOWN)
        find_func_arrow = Arrow(start = RIGHT + .75 * UP, end = 3 * RIGHT + 2 * DOWN, stroke_width = 3)
        self.play(Create(find_func), Create(find_func_arrow))

        self.wait(10)
