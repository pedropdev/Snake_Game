from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snek(Turtle):

    def __init__(self):
        super().__init__()
        self.snek_bod = []
        self.create_snake()
        self.head = self.snek_bod[0]

    def create_snake(self):
        for snek_part in STARTING_POSITIONS:
            self.add_segment(snek_part)

    def add_segment(self, position):
        new_snek = Turtle(shape="square")
        new_snek.penup()
        new_snek.color("white")
        new_snek.goto(position)
        self.snek_bod.append(new_snek)

    def extend(self):
        self.add_segment(self.snek_bod[-1].position())

    def move(self):
        for parts in range(len(self.snek_bod) - 1, 0, -1):
            new_x = self.snek_bod[parts - 1].xcor()
            new_y = self.snek_bod[parts - 1].ycor()
            self.snek_bod[parts].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def leftwards(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def rightwards(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
