from turtle import Turtle
MOVE_DISTANCE = 20
LEFT = 180
RIGHT = 0
POSITION = (350, 0)

class Paddle(Turtle):
    def __init__(self, position):
        super(Paddle, self).__init__()
        # self.paddle = Turtle(shape="square")
        self.speed("fastest")
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.penup()
        self.goto(position)
        self.color("white")