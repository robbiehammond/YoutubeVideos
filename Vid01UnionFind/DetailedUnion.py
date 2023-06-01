from manim import * 

class DetailedUnion(Scene):
    def construct(self):
        vertices = [0, 1, 2, 3, 4, 5, 6]
        edges = [(0, 1), (0, 2), (2, 3), (6, 5), (5, 4)]
        lt = {0: [-2, 1, 0], 1: [-3, 0, 0], 2: [-1, 0, 0], 3: [-1, -1, 0], 4: [1, 1, 0], 5: [2, 0, 0], 6: [2, -1, 0]}
        g = Graph(vertices, edges, labels=True, layout=lt, layout_scale=3,)
        self.play(Create(g))
        self.play(g[0].animate.set_stroke(RED, width=3), g[4].animate.set_stroke(RED, width=3))

        self.play(g.animate.shift(3 * LEFT))

        union = Tex('Union(3, 5)', font_size = 96).shift(2 * UP + 3 * RIGHT)
        self.play(Create(union))
        find5 = Tex('Find(5) = 4', font_size = 72).shift(0.5 * UP + 3 * RIGHT)
        find3 = Tex('Find(3) = 0', font_size = 72).shift(0.5 * DOWN + 3 * RIGHT)
        self.play(Create(find5))
        self.play(Create(find3))
        self.wait(1)

        parent = Tex('parent[4] = 0', font_size = 72).shift(1.5 * DOWN + 3 * RIGHT)
        self.play(Create(parent))
        self.play(g[4].animate.shift(1 * DOWN + 0.5 * LEFT), g[5].animate.shift(1 * DOWN + 0.5 * LEFT), g[6].animate.shift(1 * DOWN + 0.5 * LEFT))
        self.play(g.animate.add_edges(*[(4, 0)]), g[4].animate.set_stroke(WHITE, width=0))

        self.wait(4)

        self.play(FadeOut(g), FadeOut(parent), FadeOut(union), FadeOut(find5), FadeOut(find3))

        code = '''
Union(a, b) -> () {
    repA = Find(a);
    repB = Find(b);
    parent[repB] = repA
}
'''

        rendered_code = Code(code=code, tab_width=4, background="window", font_size=36, language="C++",
                                    font="Monospace")
        self.play(FadeIn(rendered_code))

        self.wait(5)



