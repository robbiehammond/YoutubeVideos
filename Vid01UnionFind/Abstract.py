from manim import *
import random
'''
    TODO for tomorrow: Put deterministic points down, draw circles to show sets growing 

'''




class UnoptimizedUF(Scene):

    def construct(self):
        element_ring = Circle(radius=3.0)
        self.play(Create(element_ring))
        points = [(1.25, 1.25), (-1.25, 1.25), (1.25, -1.25), (-1.25, -1.25), (1.25, 0.75), (-1.25, 0.75), (1.25, -0.75), (-1.25, -0.75), (0.75, 1.25), (-0.75, 1.25), (0.75, -1.25), (-0.75, -1.25), (0.75, 0.75), (-0.75, 0.75), (0.75, -0.75), (-0.75, -0.75)]
        dots = [Dot(point=points[i][0] * RIGHT + points[i][1] * UP) for i in range(16)]

        anims = []
        for i in range(len(points)):
            anims.append(Create(dots[i]))
        self.play(*anims)

