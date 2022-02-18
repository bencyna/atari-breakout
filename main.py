from turtle import Screen
from ball_class import Ball
from score_class import Score
from targets_class import Target
from paddle_class import Paddle
import time

positions_left = {
    "p1": (-360, -50), "p2": (-300, -50), "p3": (-240, -50), "p4": (-180, -50), "pN-5": (-120, -50),
    "p5": (-60, -50), "p6": (0, -50), "p7": (60, -50), "p8": (120, -50),
    "p9": (180, -50), "p10": (240, -50), "p11": (300, -50), "p11-x": (360, -50), "p12": (-360, 0), "p13": (-300, 0),
    "p14": (-240, 0), "p15": (-180, 0), "p16": (-120, 0), "p17": (-60, 0), "p18": (0, 0),
    "p19": (60, 0), "p20": (120, 0), "p21": (180, 0), "p22": (240, 0), "p23": (300, 0),
    "p23-x": (360, -50), "p24": (-360, 50), "p25": (-300, 50), "p26": (-240, 50), "p27": (-180, 50), "p28": (
        -120, 50),
    "p29": (-60, 50), "p30": (0, 50), "p31": (60, 50), "p32": (120, 50), "p33": (180, 50),
    "p34": (240, 50), "p35": (300, 50), "p35-x": (360, 50), "p36": (-360, 100), "p37": (-300, 100), "p38": (
        -240, 100),
    "p39": (-180, 100), "p40": (-120, 100), "p41": (-60, 100), "p42": (0, 100), "p43": (60, 100),
    "p44": (120, 100), "p45": (180, 100), "p46": (240, 100), "p47": (
        300, 100), "p47-x": (360, 100),
    "p48": (-360, 150), "p49": (-300, 150), "p50": (-240, 150), "p51": (-180, 150), "p52": (-120, 150),
    "p53": (
        -60, 150), "p54": (0, 150), "p55": (60, 150), "p56": (
        120, 150),
    "p57": (180, 150), "p58": (240, 150), "p59": (300, 150), "p59-x": (360, 150), "p60": (-360, 200),
    "p61": (-300, 200),
    "p62": (-240, 200), "p63": (-180, 200), "p64": (-120, 200), "p65": (
        -60, 200),
    "p66": (0, 200), "p67": (60, 200), "p68": (120, 200), "p69": (180, 200), "p70": (240, 200), "p71": (300, 200),
    "p71-x": (360, 200),
}

# ToDo: Setup Screen
screen = {}


def setup():
    global screen
    screen = Screen()
    screen.bgcolor("black")
    screen.setup(width=800, height=600)
    screen.title("Breakout")


setup()

screen.tracer()
score = Score()
ball = Ball()
paddle = Paddle((0, -250))

screen.listen()
screen.onkeypress(paddle.left, "Left")
screen.onkeypress(paddle.right, "Right")


def won():
    global screen, score
    screen.clear()
    setup()
    score.show_winner()


def lost():
    global screen, score
    screen.clear()
    setup()
    score.show_loser()


# ToDo: Ball class
# Move ball
# Check if ball hits wall
# change direction on collisions
# increase speed on hit target

# ToDo: Paddle class
# Allow user to move paddle
# Check for ball collisions

# ToDo: Score class
# Add a score board
# When ball collides with item increase score and display

# ToDo: Targets class
# Move to position
# When ball hits target destroy yourself
# Add to score
# instead of for loop, maybe have a dictionary with name and position instead
speed = .009

stored_target_classes = []
for i, position in enumerate(positions_left):
    stored_target_classes.append(Target((positions_left[position]), 'White'))

on = True
while on:
    time.sleep(speed)
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.vertical_wall_collision()
        if ball.ycor() < 50:
            score.l_score += 1
            score.show_score()
            ball.reset_ball()

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.horizontal_wall_collision()

    if ball.xcor() > 380:
        ball.horizontal_wall_collision()

    if ball.xcor() < -380:
        ball.horizontal_wall_collision()

    if -230 > ball.ycor() > -260 and -60 < paddle.xcor() - ball.xcor() < 60:
        ball.vertical_wall_collision()

    for i, position in enumerate(positions_left):
        if -30 < ball.xcor() - positions_left[position][0] < 30 and -30 < ball.ycor() - positions_left[position][
            1] < 20:
            ball.vertical_wall_collision()
            positions_left.pop(position)
            stored_target_classes[i].ball_collision()
            stored_target_classes.remove(stored_target_classes[i])
            speed -= .0001

            break

    if len(positions_left) == 0:
        won()
        break;
    if score.l_score > 2:
        lost()
        break

screen.exitonclick()
