from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.hideturtle()
        self.shape("square")
        self.shapesize(5, 1)
        self.color("white")
        self.penup()
        self.setposition(position)
        self.showturtle()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)