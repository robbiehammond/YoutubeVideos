from manim import *

'''
    This file produces the visuals for explaining the unoptimized UF operation.

'''


class UnoptimizedUF(Scene):


    def UFDemo(self):
            vertices = [0, 1, 2, 3, 4, 5]
            edges = []
            lt = {0: [-0.5, 1, 0], 1: [-1.5, -1, 0], 2: [-2.5, 1, 0], 3: [0.5, -1, 0], 4: [1.5, 1, 0], 5: [2.5, -1, 0]}
            g = Graph(vertices, edges, labels=True, layout="kamada_kawai", layout_scale=3,)
            self.add(g)
            self.play(g.animate.change_layout(lt),run_time=4)  

            for i in range(0, len(vertices)):
                self.play(g[i].animate.set_stroke(RED, width=3))

            self.wait(1)

            code = '''class UnionFind {

    Init(set) -> UnionFind {
        for element in set {
            parent[element] = element;
        }
    }

    Union(a, b) -> () {
        repA = Find(a);
        repB = Find(b);
        parent[repB] = repA
    }

    Find(a) -> Element {
        if (parent[a] != a)
            return Find(parent[a]);
        return a;
    }
}

'''

            self.play(*[g[i].animate.shift(4 * RIGHT) for i in range(0, len(vertices))])

            rendered_code = Code(code=code, tab_width=4, background="window", font_size=18, language="C++",
                                        font="Monospace")
            rendered_code.move_to(3 * LEFT)
            self.play(FadeIn(rendered_code))

            union1 = Tex('union(2, 1)', font_size = 72).shift(3 * DOWN, 3 * RIGHT)
            self.play(FadeIn(union1))
            self.play(g.animate.add_edges(*[(1,2)]),run_time=1)
            self.play(g[1].animate.set_stroke(WHITE, width=0), run_time=0.3)
            self.wait(2)
            self.play(FadeOut(union1))



            union2 = Tex('union(3, 4)', font_size = 72).shift(3 * DOWN, 3 * RIGHT)
            self.play(FadeIn(union2))
            self.play(g.animate.add_edges(*[(3,4)]),run_time=1)
            self.play(g[4].animate.set_stroke(WHITE, width=0), run_time=0.3)
            self.wait(1)
            self.play(FadeOut(union2))

            default_width = g[4].get_width()
            find4 = Tex('find(4)', font_size = 72).shift(3 * DOWN, 3 * RIGHT)
            self.play(FadeIn(find4))
            self.play(g[4].animate.set_width(1.2))
            self.wait(1)
            self.play(g[4].animate.set_width(default_width))
            self.play(g[3].animate.set_width(1.2))
            ans = Tex('= 3', font_size=72).shift(3 * DOWN, 4 * RIGHT)
            self.play(find4.animate.shift(LEFT))
            self.play(FadeIn(ans))
            self.wait(1)
            self.play(g[3].animate.set_width(default_width))


            self.play(FadeOut(find4), FadeOut(ans))


            union3 = Tex('union(2, 4)', font_size = 72).shift(3 * DOWN, 3 * RIGHT)
            self.play(FadeIn(union3))

            self.play(g[4].animate.set_width(1.2))
            self.wait(0.5)
            self.play(g[4].animate.set_width(default_width))
            self.play(g[3].animate.set_width(1.2))
            self.wait(0.5)
            self.play(g[3].animate.set_width(default_width))

            self.play(g[4].animate.shift(0.5 * LEFT + 2 * DOWN),
                      g[3].animate.shift(0.5 * LEFT, 1 * DOWN),
                        run_time=1
            )
            self.play(g[3].animate.set_stroke(WHITE, width=0), run_time=0.3)
            self.play(g.animate.add_edges(*[(3, 2)]))
            self.wait(1)
            self.play(FadeOut(union3))

            union0 = Tex('union(0, 5)', font_size = 72).shift(3 * DOWN, 3 * RIGHT)
            self.play(FadeIn(union0))
            self.play(g.animate.add_edges(*[(0,5)]),run_time=1)
            self.play(g[5].animate.set_stroke(WHITE, width=0), run_time=0.3)
            self.wait(1)
            self.play(FadeOut(union0))


            find4Again = Tex('find(4)', font_size = 72).shift(3 * DOWN, 3 * RIGHT)
            self.play(FadeIn(find4Again))
            self.play(g[4].animate.set_width(1.2))
            self.wait(.25)
            self.play(g[4].animate.set_width(default_width))
            self.play(g[3].animate.set_width(1.2))
            self.wait(.25)
            self.play(g[3].animate.set_width(default_width))
            self.play(g[2].animate.set_width(1.2))
            self.wait(.5)
            ans2 = Tex('= 2', font_size=72).shift(3 * DOWN, 4 * RIGHT)
            self.play(find4Again.animate.shift(LEFT))
            self.play(FadeIn(ans2))
            self.play(g[2].animate.set_width(default_width))
            self.wait(1)


    def construct(self):
        self.UFDemo()

