from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Score(Turtle):
    def __init__(self):
        self.score = 0
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_text()

    def update_text(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over",align=ALIGNMENT, font=FONT)

    def update_score(self):
        self.score += 1
        self.clear()  # clears previous text - can use undo as well
        self.update_text()








