from manim import * 

class Intro(Scene):
    def construct(self):
        self.wait(0.5)
        codeforces = ImageMobject('img/code-forces.png')
        codeforces.scale(0.75)
        leetcode = ImageMobject('img/Leetcode_logo_rvs')
        leetcode.scale(0.75)
        self.play(FadeIn(codeforces), codeforces.animate.shift(3 * LEFT))
        self.wait(1.25)
        self.play(FadeIn(leetcode), leetcode.animate.shift(3 * RIGHT))

        self.wait(2)
        union = Tex('Union', font_size=96, color=RED).shift(1.35 * LEFT + UP)
        find = Tex('Find', font_size=96, color=BLUE).shift(1.35 * RIGHT + UP)
        self.play(codeforces.animate.shift(2 * DOWN), leetcode.animate.shift(2 * DOWN))
        self.play(Create(union), Create(find))


        self.wait(15)