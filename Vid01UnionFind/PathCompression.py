from manim import *

class PathCompression(Scene):
    def construct(self):    
        vertices = [0, 1, 2, 3, 4]
        edges = [(2, 0), (1, 0), (3, 2), (4, 3)]
        lt = {0: [0, 2, 0], 1: [1, 1, 0], 2: [-2, 1, 0], 3: [-1, -1, 0], 4: [0, -3, 0]}
        self.wait(7.5)
        g = Graph(vertices, edges, labels=True, layout=lt)
        self.play(Create(g))
        self.wait(4)
        self.play(g.animate.shift(2 * LEFT))
        self.play(g[0].animate.set_stroke(RED, width=3))

        default_width = g[4].get_width()


        find4 = Tex('find(4)', font_size = 72).shift(3 * UP + 3 * RIGHT)
        self.play(Create(find4), g[4].animate.set_width(1.2))
        self.wait(1)

        find3 = Tex('find(3)', font_size = 72).shift(UP + 3 * RIGHT)
        a1 = Arrow(find4, find3, stroke_width=10).shift(0.5 * LEFT)
        self.play(Create(find3), Create(a1), g[4].animate.set_width(default_width), g[3].animate.set_width(1.2))
        self.wait(1)

        find2 = Tex('find(2)', font_size = 72).shift(DOWN + 3 * RIGHT)
        a2 = Arrow(find3, find2, stroke_width=10).shift(0.5 * LEFT)
        self.play(Create(find2), Create(a2), g[3].animate.set_width(default_width), g[2].animate.set_width(1.2))
        self.wait(1)

        find0 = Tex('find(0) = 0', font_size = 72).shift(3 * DOWN + 3 * RIGHT)
        a3 = Arrow(find2, find0, stroke_width=10).shift(0.5 * LEFT)
        self.play(Create(find0), Create(a3), g[2].animate.set_width(default_width), g[0].animate.set_width(1.2))
        self.wait(5)

        find2Rep = Tex('find(2) = 0', font_size = 72).shift(DOWN + 3 * RIGHT)
        self.play(g[0].animate.set_width(default_width), g[2].animate.set_width(1.2), ReplacementTransform(find2, find2Rep))

        find3Rep = Tex('find(3) = 0', font_size = 72).shift(UP + 3 * RIGHT)
        self.play(g[2].animate.set_width(default_width), g[3].animate.set_width(1.2))
        self.play(g.animate.remove_edges(*[(3,2)]))
        self.play(g.animate.add_edges(*[(3,0)]))
        self.play(ReplacementTransform(find3, find3Rep))


        find4Rep = Tex('find(4) = 0', font_size = 72).shift(3 * UP + 3 * RIGHT)
        self.play(g[3].animate.set_width(default_width), g[4].animate.set_width(1.2))
        self.play(g.animate.remove_edges(*[(4,3)]))
        self.play(g.animate.add_edges(*[(4,0)]))
        self.play(ReplacementTransform(find4, find4Rep))
        self.play(g[4].animate.set_width(default_width))
        self.wait(1)
        self.play(
            *[FadeOut(mob)for mob in self.mobjects]
        )
        self.wait(2)




