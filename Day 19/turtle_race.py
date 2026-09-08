import turtle
from turtle import Turtle, Screen
import random

screen = Screen()

screen.setup(width=500, height=400)


# turtle colors
colors = ["red", "green", "blue", "yellow", "orange", "purple"]

# store turtle objects
turtle_lst = []

def create_turtles():
    """
    Creates 6 turtles with 6 different colors at different positions on y-axis
    """
    # y start position
    y = -80
    for i in range(6):
            new_turtle = Turtle("turtle")
            turtle_lst.append(new_turtle)
            new_turtle.color(colors[i])
            new_turtle.penup()
            new_turtle.goto(x=-230, y = y)
            y += 30
    start_racing() # call function to start racing

def start_racing():
    """
    Turtles start racing at random steps and prints which turtle wins based on input.
    """
    winner_color = ""
    running = True
    while running:
        for t in turtle_lst:
            t.forward(random.randint(0,10))
            if t.xcor() > 230:
                winner_color = t.pencolor()
                running = False
    if inp == winner_color:
        print(f"You win! The {winner_color} turtle wins the game.")
    else:
        print(f"You lose! The {winner_color} turtle wins the game.")

    # screen.exitonclick()


if __name__ == "__main__":
    inp = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color:")

    if not inp == "":
        create_turtles()




