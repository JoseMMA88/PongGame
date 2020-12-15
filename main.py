from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time


# Screen Setup
screen = Screen()
screen.setup(width=800, height=600)
screen.title("PONG GAME")
screen.bgcolor("black")
screen.tracer(0)


# Paddle Setup
paddle_1 = Paddle((350, 0))
paddle_2 = Paddle((-350, 0))


# Score Setup
score_1 = Score((40, 260))
score_2 = Score((-40, 260))


# Ball Setup
ball = Ball()


# Controls listeners
screen.listen()
screen.onkeypress(fun=paddle_1.move_up, key="Up")
screen.onkeypress(fun=paddle_1.move_down, key="Down")
screen.onkeypress(fun=paddle_2.move_up, key="w")
screen.onkeypress(fun=paddle_2.move_down, key="s")


# game Loop
is_gaming = True
while is_gaming:
    time.sleep(ball.move_speed)
    screen.update()
    ball.update()
    ball.check_collision(screen.window_height(), paddle_1, paddle_2)

    # Check Goals
    if ball.xcor() > paddle_1.xcor() + 10:
        ball.reset_position()
        score_1.up_score()

    elif ball.xcor() < paddle_2.xcor() - 10:
        ball.reset_position()
        score_2.up_score()

screen.exitonclick()