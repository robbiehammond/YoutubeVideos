from manim import * 

class DetailedFind(Scene):
    def construct(self):
        vertices = [0, 1, 2]
        edges = []
        lt = {0: [-2, 1, 0], 1: [0, 0, 0], 2: [2, -2, 0]}
        g = Graph(vertices, edges, labels=True, layout=lt, layout_scale=3,)
        self.play(Create(g))
        self.wait(2)
        self.play(g.animate.add_edges(*[(1, 0)]), run_time = 0.5)
        self.wait(1)
        self.play(g.animate.remove_edges(*[(1, 0)]), run_time = 0.5)
        self.wait(2)

        
        self.play(g.animate.add_vertices(*[3, 4, 5], positions={3: [0.5, -2, 0], 4: [-0.5, -2, 0], 5: [-0.5, -3, 0]} ,labels=True))
        self.play(g.animate.add_edges(*[(3, 1), (4, 1), (5, 4)]))
        self.wait(1)
        self.play(g.animate.remove_edges(*[(3, 1), (4, 1), (5, 4)]))
        self.play(g.animate.remove_vertices(*[3, 4, 5]))
        self.wait(1)

        self.play(*(g[i].animate.set_stroke(RED, width=3) for i in range(3)))

        self.wait(1)



        self.wait(1)
