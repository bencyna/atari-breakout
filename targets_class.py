from turtle import Turtle


class Target(Turtle):
    def __init__(self, position, color):
        super(Target, self).__init__()
        self.penup(),
        self.shape('square')
        self.shapesize(1, 2)
        self.speed(10)
        self.goto(position),
        self.color(color)

    def ball_collision(self):
        self.reset()