from manim import *
import random

class UnoptimizedUF(Scene):

    def construct(self):
        self.wait(3)
        element_ring = Circle(radius=3.5)
        self.play(Create(element_ring))
        points = [(-1.5, -1.5), (1.5, 1.5), (-1.5, 1.5), (1.5, -1.5)]
        dots = [LabeledDot(label=str(i), point=points[i][0] * RIGHT + points[i][1] * UP) for i in range(len(points))]

        anims = []
        for i in range(len(points)):
            anims.append(Create(dots[i]))
        self.play(*anims)

        self.wait(2)

        # ------------------------------------------ # 
        c1 = Circle(radius=0.5, color=WHITE).move_to([-1.5, -1.5, 0])

        c2 = Circle(radius=0.5, color=WHITE).move_to([1.5, 1.5, 0])

        c3 = Circle(radius=0.5, color=WHITE).move_to([-1.5, 1.5, 0])

        c4 = Circle(radius=0.5, color=WHITE).move_to([1.5, -1.5, 0])

        self.play(Create(c1), Create(c2), Create(c3), Create(c4))

        e1 = Ellipse(width = 4.0, height = 1.0, color=WHITE).move_to([0, -1.5, 0])

        self.wait(4)

        merge = Tex('Merge nodes 0 and 3', font_size = 32).shift(3.25 * DOWN, 4.75 * RIGHT)

        self.play(Create(merge))

        #self.play(FadeOut(c1), FadeOut(c4))
        self.play(FadeOut(c4))
        self.play(ReplacementTransform(c1, e1))
        self.play(FadeOut(merge))

        self.wait(4)

        sameSet = Tex('Are nodes 0 and 3 in the same set?', font_size = 32).shift(3.25 * DOWN, 4.25 * RIGHT)
        yes = Tex('Yes', font_size= 32, color=RED).shift(3.75 * DOWN, 4.5 * RIGHT)
        self.play(Create(sameSet))
        self.play(Create(yes))



        self.wait(1)

