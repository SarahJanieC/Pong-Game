from turtle import Turtle


class PaddleLeft(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(5,1)
        self.goto(-350,0)

    def up(self):
        new_y = self.ycor() + 28
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 28
        self.goto(self.xcor(), new_y)
