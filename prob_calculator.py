import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = list()
    for k,v in kwargs.items():
      for i in range(v):
        self.contents.append(k)

  def draw(self, num_draws):
    if num_draws >= len(self.contents):
      return self.contents
    else:
      balls = list()
      for draw in range(num_draws):
        draw_ind = random.randint(0, len(self.contents)-1)
        balls.append(self.contents.pop(draw_ind))
      return balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  success = 0
  for draw in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    drawn_ball = hat_copy.draw(num_balls_drawn)
    colors_got = 0
    for color in expected_balls.keys():
      if drawn_ball.count(color) >= expected_balls[color]:
        colors_got += 1
      if colors_got == len(expected_balls):
        success += 1
  probability = float(success/num_experiments)
  return(probability)
