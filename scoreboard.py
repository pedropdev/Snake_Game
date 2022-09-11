import turtle
from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.num_eaten = 0
        self.penup()
        self.goto(0, 280)
        self.color("white")
        self.hideturtle()

    def keep_score(self):
        self.write(f"Score: {self.num_eaten}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over", align=ALIGNMENT, font=FONT)
