from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super(Score, self).__init__()
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.color("white")
        self.speed(5)
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=('Courier', 50, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=('Courier', 50, "normal"))

    def l_point(self):
        self.l_score += 1
        self.show_score()

    def r_point(self):
        self.r_score += 1
        self.show_score()