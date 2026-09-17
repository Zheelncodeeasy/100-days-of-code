from turtle import Turtle

FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 0
        self.hideturtle()
        self.penup()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)

    def create_text(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def update_level(self):
        self.level += 1
        self.create_text()

