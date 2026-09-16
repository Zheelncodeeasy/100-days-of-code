from turtle import Turtle, Screen

class Paddle(Turtle):

    def __init__(self, position):
        # Creating paddle
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("white")
        self.goto(position)
        self.turtlesize(stretch_wid=5, stretch_len=1)

    def go_up(self):
        new_y_cord = self.ycor() + 20
        self.goto(self.xcor(), new_y_cord)

    def go_down(self):
        new_y_cord = self.ycor() - 20
        self.goto(self.xcor(), new_y_cord)
