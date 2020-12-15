from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.speed_y = 10
        self.speed_x = 10

    def update(self):
        self.move()

    def move(self):
        self.goto(self.xcor() + self.speed_x, self.ycor() + self.speed_y)

    def check_collision(self, screen_height, paddle_1, paddle_2):
        if self.ycor() > 280 or self.ycor() < -280:
            self.speed_y *= -1

        if self.distance(paddle_1) < 50 and self.xcor() > paddle_1.xcor() - 20 or \
                self.distance(paddle_2) < 50 and self.xcor() < paddle_2.xcor() + 20:
            self.speed_x *= -1

    def reset_position(self):
        self.home()
        self.speed_x = self.speed_x * -1
