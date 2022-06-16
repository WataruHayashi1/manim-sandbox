from manim import *

class Merge(Scene):
  def construct(self):
    circle = Circle()
    line = Line()
    line.next_to(circle, RIGHT, buff=0.0)
    self.play(GrowFromCenter(circle))
    self.play(GrowFromCenter(line))
    