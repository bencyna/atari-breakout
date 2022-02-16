from turtle import Turtle
import time


class Ball(Turtle):
    def __init__(self):
        super(Ball, self).__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.move_speed = 0.05
        self.x_movement = 10
        self.y_movement = 10
        self.move_ball()

        def move_ball(self):
            new_x = self.xcor() + self.x_movement
            new_y = self.ycor() + self.y_movement
            self.goto(new_x, new_y)