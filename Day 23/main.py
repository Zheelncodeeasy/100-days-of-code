import time
from turtle import Screen
from car_manager import CarManager
from player import Player
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0) # turns off animations

# creating CarManager instance
car_manager = CarManager()

# Creating Player instance
player = Player()

# Creating scoreboard instance
scoreboard = Scoreboard()
scoreboard.create_text()

screen.listen()
screen.onkey(player.go_up, "Up")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update() # refreshed the screen after 0.1 seconds

    car_manager.create_car()
    car_manager.move_cars()

    # Detects turtle collision with a car
    for car in car_manager.cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_on = False

    # Detects whether player reached finish line and
    # updates the level and starting position of player
    # Increases car speed based on different levels
    if player.reach_finish_line():
       scoreboard.update_level()
       player.begin_again()
       car_manager.increase_speed()

screen.exitonclick()

