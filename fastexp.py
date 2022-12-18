from manim import *

class FastExponentiation(Scene):
    def construct(self):
        pot = 64
        s = 'I'
        tex = MathTex(s.replace('I', 'x^{' + str(pot) + '}')).scale(2.5)
        self.play(Create(tex))
        self.wait(3.0)
        count = 1
        while pot > 1:
            if pot%2 == 0:
                s = s.replace('I', f'(I)^2')
            else:
                s = s.replace('I', f'(I)^2 x')
            pot //= 2
            ptex = MathTex(s.replace('I', 'x^{' + (str(pot) if pot > 1 else '') + '}')).scale(2.5)
            self.play(Transform(tex, ptex))
            if count == 1:
                self.wait(2)
            elif count == 2:
                self.wait(1)
            count += 1
        self.wait(3)
