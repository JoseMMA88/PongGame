from turtle import Turtle


BODY_NUM = 5
SPEED = 20


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(position)
        self.shapesize(stretch_wid=5, stretch_len=1)

    def move_up(self):
        if self.ycor() < 225:
            self.goto(self.xcor(), self.ycor() + SPEED)

    def move_down(self):
        if self.ycor() > -202:
            self.goto(self.xcor(), self.ycor() - SPEED)
