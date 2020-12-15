from turtle import Turtle


FONT = ("Verdana", 26, "normal")


class Score(Turtle):

    def __init__(self, position):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(position)
        self.write(arg=f"{self.score}", font=FONT)

    def up_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"{self.score}", font=FONT)
