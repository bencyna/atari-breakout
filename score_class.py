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
        self.goto(-100, 250)
        self.write(f"Lives used: {self.l_score}", align="center", font=('Courier', 10, "normal"))

    def l_point(self):
        self.l_score += 1
        self.show_score()

    def r_point(self):
        self.r_score += 1
        self.show_score()

    def show_winner(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"You won! you used : {self.l_score} lives", align="center", font=('Courier', 30, "normal"))

    def show_loser(self):
        self.clear()
        self.goto(0, 0)
        self.write(f"You lost! you died : {self.l_score} times", align="center", font=('Courier', 30, "normal"))
