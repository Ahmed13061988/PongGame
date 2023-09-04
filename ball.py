from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.goto(0, 0)
        self.penup()
        self.move()

    def move(self):
        new_x = self.xcor() + 5
        new_y = self.ycor() + 5
        self.goto(new_x, new_y)
