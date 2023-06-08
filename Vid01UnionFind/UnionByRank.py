from manim import *

class UnionByRank(Scene):
    def construct(self):
        self.wait(1)
        vertices = [0, 1, 2, 3]
        edges = [(1, 0), (2, 0)]
        lt = {0: [0, 1, 0], 1: [-1, 0, 0], 2: [-2, -1, 0], 3: [2, 1, 0]}
        g = Graph(vertices, edges, labels=True, layout=lt)
        self.play(Create(g))
        self.play(g[0].animate.set_stroke(RED, width=3), g[3].animate.set_stroke(RED, width=3))
        self.play(g.animate.shift(UP))
        self.wait(1)

        union = Tex('Union(0, 3)', font_size = 72).shift(3 * DOWN)
        self.play(Create(union))


        #making parent[0] = 3
        self.play(*(g[i].animate.shift(DOWN) for i in range(3)))
        self.play(g.animate.add_edges(*[(0, 3)]))
        self.play(g[0].animate.set_stroke(WHITE, width=0))

        unionRep1 = Tex(r'Union(0, 3) $\rightarrow$ Max Depth is 3', font_size = 72).shift(3 * DOWN)
        unionRep2 = Tex(r'Union(0, 3) $\rightarrow$ Max Depth is 2', font_size = 72).shift(3 * DOWN)
        self.play(ReplacementTransform(union, unionRep1))
        union = Tex('Union(0, 3)', font_size = 72).shift(3 * DOWN)
        self.wait(1)

        #undo above
        self.play(FadeOut(unionRep1))
        self.play(g.animate.remove_edges(*[(0, 3)]))
        self.play(*(g[i].animate.shift(UP) for i in range(3)))
        self.play(g[0].animate.set_stroke(RED, width=3))

        #making parent[3] = 0 (the one that makes more sense)
        self.play(Create(union))
        self.play(g[3].animate.shift(DOWN + LEFT))
        self.play(g.animate.add_edges(*[(3, 0)]))
        self.play(g[3].animate.set_stroke(WHITE, width=0))
        self.play(ReplacementTransform(union, unionRep2))
        self.wait(1)
        self.play(FadeOut(g), FadeOut(union), FadeOut(unionRep2))


        self.wait(3)
