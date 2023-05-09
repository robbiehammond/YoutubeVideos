from manim import *

class Graph3(Scene):
    def construct(self):
        vertices = [0, 1, 2, 3, 4, 5]
        edges = []
        lt = {0: [-1, 1, 0], 1: [-3, -1, 0], 2: [-5, 1, 0], 3: [1, -1, 0], 4: [3, 1, 0], 5: [5, -1, 0]}
        g = Graph(vertices, edges, labels=True, layout="kamada_kawai", layout_scale=3,)
        self.add(g)
        self.play(g.animate.change_layout(lt),run_time=4)  
        #self.play(g.animate.add_edges(*[(1,2)]),run_time=4)

        self.wait(1)


        union1 = Tex('union(1, 2)', font_size = 72).shift(2.5 * DOWN)
        self.play(FadeIn(union1))
        self.play(g.animate.add_edges(*[(1,2)]),run_time=1)
        self.play(g[2].animate.set_stroke(RED, width=3))
        self.wait(2)
        self.play(FadeOut(union1))

        # self.play(g[1].animate.set_stroke(WHITE, width=0)) To turn stuff back


        union2 = Tex('union(3, 4)', font_size = 72).shift(2.5 * DOWN)
        self.play(FadeIn(union2))
        self.play(g.animate.add_edges(*[(3,4)]),run_time=1)
        self.play(g[3].animate.set_stroke(RED, width=3))
        self.wait(1)
        self.play(FadeOut(union2))

        default_width = g[4].get_width()
        find4 = Tex('find(4)', font_size = 72).shift(2.5 * DOWN)
        self.play(FadeIn(find4))
        self.play(g[4].animate.set_width(1.2))
        self.wait(1)
        self.play(g[4].animate.set_width(default_width))
        self.play(g[3].animate.set_width(1.2))
        self.wait(1)
        self.play(g[3].animate.set_width(default_width))


        self.play(FadeOut(find4))



        union3 = Tex('union(4, 2)', font_size = 72).shift(2.5 * DOWN)
        self.play(FadeIn(union3))

        self.play(g[4].animate.set_width(1.2))
        self.wait(0.5)
        self.play(g[4].animate.set_width(default_width))
        self.play(g[3].animate.set_width(1.2))
        self.wait(0.5)
        self.play(g[3].animate.set_width(default_width))

        self.play(g[4].animate.move_to(2 * LEFT + 1 * DOWN),
                  g[3].animate.move_to(2 * LEFT),
                    run_time=1
        )
        self.play(g[3].animate.set_stroke(WHITE, width=0), run_time=0.3)
        self.play(g.animate.add_edges(*[(3, 2)]))
        self.wait(1)
        self.play(FadeOut(union3))

        union0 = Tex('union(0, 5)', font_size = 72).shift(2.5 * DOWN)
        self.play(FadeIn(union0))
        self.play(g.animate.add_edges(*[(0,5)]),run_time=1)
        self.play(g[0].animate.set_stroke(RED, width=3))
        self.wait(1)
        self.play(FadeOut(union2))



