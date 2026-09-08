from turtle import Turtle, Screen

turtle = Turtle()
screen = Screen()

# moves forward with key W
def move_forward():
    turtle.forward(10)

# moves backward with key S
def move_backwards():
    turtle.backward(10)

# moves counterclockwise with key A
def turn_left():
    turtle.left(10)

# moves clockwise with key D
def turn_right():
    turtle.right(10)

# clears screen
def clear():
    turtle.clear()
    turtle.penup()
    turtle.home() # returns turtle to position x : 0, y: 0
    turtle.pendown()



screen.listen()  # listen to the events

# onkey events
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="c", fun=clear)

screen.exitonclick()
