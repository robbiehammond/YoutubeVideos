from manim import * 

class Assumptions(Scene):
    def construct(self):
        self.wait(2)
        prs = Tex('Prerequisites', font_size=72).shift(3 * UP)
        self.play(Create(prs))
        s = r'''
        \begin{itemize}
            \item Graphs and Related Algorithms 
            \begin{itemize}
                \item Construction 
                \item Searching (particularly DFS)
            \end{itemize}
        \end{itemize}
        '''
        prereqs = Tex(s).shift(UP)
        self.play(Create(prereqs))
        self.wait(5)


        niceToKnow = Tex('Helpful to Know', font_size=72).shift(DOWN)
        self.play(Create(niceToKnow))
        s1 = r'''
        \begin{itemize}
            \item Basic Set Notation 
            \begin{itemize}
                \item $\in$, $\forall$, $\cup$, $\exists$, etc
            \end{itemize}
        \end{itemize}
        '''
        toKnows = Tex(s1).shift(2.5 * DOWN)
        self.play(Create(toKnows))


        self.wait(8)