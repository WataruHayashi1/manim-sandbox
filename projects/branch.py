from manim import *

class Branch(Scene):
  def construct(self):
    init_commit = Circle(color=WHITE)
    self.play(GrowFromCenter(init_commit))