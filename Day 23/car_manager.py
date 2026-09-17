from turtle import Turtle
import random

colors = ["red", "orange", "yellow", "green", "blue", "violet", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:

    def __init__(self):
        self.cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        # Using random module so that only fewer cars are generated
        random_choice = random.randint(1, 6)
        if random_choice == 1:
            new_car = Turtle("square")
            new_car.penup()
            new_car.setheading(-180)
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(colors))
            new_y = random.randint(-250, 250)
            new_car.goto(300, new_y)
            self.cars.append(new_car)

    def move_cars(self):
        for car in self.cars:
            car.forward(self.car_speed)

    def increase_speed(self):
        self.car_speed += MOVE_INCREMENT







