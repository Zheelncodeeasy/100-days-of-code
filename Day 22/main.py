from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width = 800, height = 600)
screen.title("Pong")
screen.bgcolor("black")
screen.tracer(0)  # turns off turtle animations

# Creating Paddles and moving them with keys
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

# Creating a Ball
ball = Ball()

# Creating a Scoreboard
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_on = True

while game_on:
    screen.update()   # refreshes the screen
    time.sleep(ball.move_speed)  # increasing the speed
    ball.move()
    # Detect  collision with wall
    if ball.collision():
        # Bounce the ball
        ball.bounce_y()

    # Detect collision with right paddle or left paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 330 or
       ball.distance(l_paddle) < 50 and ball.xcor() < -330):
        ball.bounce_x()

    # Detect R paddle miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # Detect L paddle miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()