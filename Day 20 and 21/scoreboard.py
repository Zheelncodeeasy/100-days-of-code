from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "normal")

class Score(Turtle):
    def __init__(self):
        self.score = 0
        self.high_score = 0
        # Reading high score from data.txt
        with open("data.txt") as file:
            self.high_score = int(file.read())
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.update_text()

    def update_text(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", "w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_text()

    def update_score(self):
        self.score += 1
        self.clear()  # clears previous text - can use undo as well
        self.update_text()








