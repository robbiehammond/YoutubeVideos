from manim import * 

class DetailedFind(Scene):
    def construct(self):
        vertices = [0, 1, 2]
        edges = []
        lt = {0: [-2, 1, 0], 1: [0, 0, 0], 2: [2, -2, 0]}
        g = Graph(vertices, edges, labels=True, layout=lt, layout_scale=3,)
        self.wait(3)
        self.play(Create(g))
        self.wait(8)
        self.play(g.animate.add_edges(*[(1, 0)]), run_time = 0.5)
        self.wait(1.5)
        self.play(g.animate.remove_edges(*[(1, 0)]), run_time = 0.5)

        
        self.play(g.animate.add_vertices(*[3, 4, 5], positions={3: [0.5, -2, 0], 4: [-0.5, -2, 0], 5: [-0.5, -3, 0]} ,labels=True))
        self.play(g.animate.add_edges(*[(3, 1), (4, 1), (5, 4)]))
        self.wait(1.5)
        self.play(g.animate.remove_edges(*[(3, 1), (4, 1), (5, 4)]))
        self.play(g.animate.remove_vertices(*[3, 4, 5]))
        self.wait(18)

        self.play(*(g[i].animate.set_stroke(RED, width=3) for i in range(3)))

        self.wait(3)


        self.play(g.animate.add_edges(*[(1, 0)]), g[1].animate.set_stroke(WHITE, width=0), run_time=0.75)
        self.play(g.animate.add_edges(*[(2, 1)]), g[2].animate.set_stroke(WHITE, width=0), run_time=0.75)

        self.wait(8)

        self.play(g.animate.shift(4 * LEFT))

        default_width = g[0].get_width()

        find = Tex('find(2) = ?', font_size = 96).shift(2 * UP + 3 * RIGHT)
        self.play(Create(find))

        
        find2 = Tex('parent[2] = 1', font_size = 72).shift(0.5 * UP + 3 * RIGHT)
        self.play(g[2].animate.set_width(1.2))
        self.play(Create(find2))
        self.wait(1)

        find1 = Tex('parent[1] = 0', font_size = 72).shift(0.5 * DOWN, 3 * RIGHT)
        self.play(g[2].animate.set_width(default_width), g[1].animate.set_width(1.2))
        self.play(Create(find1))
        self.wait(1)

        find0 = Tex('parent[0] = 0', font_size = 72).shift(1.5 * DOWN, 3 * RIGHT)
        self.play(g[1].animate.set_width(default_width), g[0].animate.set_width(1.2))
        self.play(Create(find0))
        self.wait(1)

        findComplete = Tex('find(2) = 0', font_size = 96).shift(2 * UP + 3 * RIGHT)
        self.play(g[0].animate.set_width(default_width))
        self.play(ReplacementTransform(find, findComplete))

        self.wait(3)

        self.play(FadeOut(g), FadeOut(findComplete), FadeOut(find), FadeOut(find2), FadeOut(find1), FadeOut(find0))

        code = '''
Find(a) -> Element {
    if (parent[a] != a)
        return Find(parent[a]);
    return a;
}
'''

        rendered_code = Code(code=code, tab_width=4, background="window", font_size=36, language="C++",
                                    font="Monospace")
        self.play(FadeIn(rendered_code))

        self.wait(7)
        self.play(FadeOut(rendered_code))
