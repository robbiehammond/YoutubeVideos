from manim import * 

class BigGraph(Scene):
    def construct(self):
        element_ring = Circle(radius=3.5)
        self.play(Create(element_ring))
        points = [(-1.5, -1.5), (1.5, 1.5), (-1.5, 1.5), (1.5, -1.5)]
        dots = [LabeledDot(label=str(i), point=points[i][0] * RIGHT + points[i][1] * UP) for i in range(len(points))]

        anims = []
        for i in range(len(points)):
            anims.append(Create(dots[i]))
        self.play(*anims)

        e1 = Ellipse(width = 4.0, height = 1.0, color=WHITE).move_to([0, -1.5, 0])
        e2 = Ellipse(width = 4.0, height = 1.0, color=WHITE).move_to([0, 1.5, 0])
        self.play(Create(e1), Create(e2))


        sameSet = Tex('Are nodes 0 and 2 in the same set?', font_size = 32).shift(3.25 * DOWN, 4.25 * RIGHT)
        yes = Tex('No', font_size= 32, color=RED).shift(3.75 * DOWN, 4.5 * RIGHT)
        self.play(Create(sameSet))
        self.wait(1)
        self.play(Create(yes))
        self.wait(2)
        self.play(FadeOut(sameSet), FadeOut(yes))
        self.wait(1)
        numSubsets = Tex('How many subsets are there?', font_size = 32).shift(3.25 * DOWN, 4.25 * RIGHT)
        two = Tex('Two', font_size= 32, color=RED).shift(3.75 * DOWN, 4.5 * RIGHT)
        self.play(Create(numSubsets))
        self.wait(1)
        self.play(Create(two))
        self.wait(2)
        self.play(FadeOut(numSubsets), FadeOut(two))
        self.wait(5)



        poly_list = [
            [2.25, 2.25, 0],
            [2.25, -2.25, 0],
            [-2.25, -2.25, 0],
            [-2.25, -1, 0],
            [.75, -1, 0],
            [.75, 2.25, 0],

        ]
        self.play(FadeOut(e1), FadeOut(e2), Create(Polygon(*poly_list, color=WHITE)))
        c1 = Circle(radius=0.5, color=WHITE).move_to([-1.5, 1.5, 0])
        self.play(Create(c1))

        sameSet = Tex('Are nodes 0 and 2 in the same set?', font_size = 32).shift(3.25 * DOWN, 4.25 * RIGHT)
        yes = Tex('Still No', font_size= 32, color=RED).shift(3.75 * DOWN, 4 * RIGHT)
        self.play(Create(sameSet))
        self.wait(1)
        self.play(Create(yes))

        self.wait(1)

        numSubsets = Tex('How many subsets are there?', font_size = 32).shift(3.25 * DOWN, 4.25 * RIGHT)
        two = Tex('Still Two', font_size= 32, color=RED).shift(3.75 * DOWN, 4 * RIGHT)
        self.play(Create(numSubsets))
        self.wait(1)
        self.play(Create(two))
        self.wait(2)
        self.play(FadeOut(numSubsets), FadeOut(two))
        self.wait(5)

        self.wait(2)
