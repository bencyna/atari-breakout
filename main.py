from turtle import Screen
from ball_class import Ball
from score_class import Score
from targets_class import Target
from paddle_class import Paddle
import time
positions_left = [

]

# ToDo: Setup Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer()
score = Score()
ball = Ball()
paddle = Paddle((0, -250))

screen.listen()
screen.onkeypress(paddle.left, "Left")
screen.onkeypress(paddle.right, "Right")

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
for num_y in range(-50, 250, 50):
    for num_x in range(-360, 360, 60):
        target = Target((num_x, num_y), 'White')
        positions_left.append((num_x, num_y))

print(positions_left)
on = True
while on:
    screen.update()
    ball.move_ball()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.vertical_wall_collision()

    if ball.xcor() > 390 or ball.xcor() < -390:
        ball.horizontal_wall_collision()

    if ball.xcor() > 380:
        ball.horizontal_wall_collision()

    if ball.xcor() < -380:
        ball.horizontal_wall_collision()

    if -240 > ball.ycor() > -260 and paddle.xcor() - ball.xcor() < 40:
        ball.vertical_wall_collision()

screen.exitonclick()
