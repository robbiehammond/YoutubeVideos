from manim import * 

class DetailedFind(Scene):
    def construct(self):
        Find = Tex(r'Find $\rightarrow$ Get Representative Of Subset', font_size = 48)
        self.play(Create(Find))
        self.wait(0.5)
        self.play(Find.animate.shift(3.5 * UP))
        

        element_ring = Circle(radius=3)
        self.play(Create(element_ring))
        points = [(-1.5, -1.5), (1.5, 1.5), (-1.5, 1.5), (1.5, -1.5)]
        dots = [LabeledDot(label=str(i), point=points[i][0] * RIGHT + points[i][1] * UP) for i in range(len(points))]

        anims = []
        for i in range(len(points)):
            anims.append(Create(dots[i]))
        self.play(*anims)

        c2 = Circle(radius=0.5, color=WHITE).move_to([1.5, 1.5, 0])
        c3 = Circle(radius=0.5, color=WHITE).move_to([-1.5, 1.5, 0])
        e1 = Ellipse(width = 4.0, height = 1.0, color=WHITE).move_to([0, -1.5, 0])
        self.play(Create(c2), Create(c3), Create(e1))
        self.wait(2)
        self.play(dots[2].animate.set_stroke(RED, width=3), dots[1].animate.set_stroke(RED, width=3), dots[3].animate.set_stroke(RED, width=3))


        self.wait(2)

        Find0 = Tex(r'$Find(0) = 3$', font_size = 48).shift(2.5 * DOWN + 4.5 * RIGHT)
        self.play(Create(Find0))
        self.wait(2)
        Find3 = Tex(r'$Find(3) = 3$', font_size = 48).shift(3.25 * DOWN + 4.5 * RIGHT)
        self.play(Create(Find3))

        self.wait(1)
        