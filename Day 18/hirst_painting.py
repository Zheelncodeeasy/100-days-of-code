import colorgram
from turtle import Turtle, colormode, Screen
import random

# colors = colorgram.extract('D:/100 Days of Code - Python/Day 18/hirst_dot_painting.jpg', 30)
#
# rgb_list = []   # list of (r,g,b) tuple
#
# for color in colors:
#     rgb = color.rgb # fetch all r, g, b values from colors list
#     rgb_values = rgb.r, rgb.g, rgb.b # pack separate red, blue and green colors in a tuple
#     rgb_list.append(rgb_values) # append RGB tuple to a list
# print(rgb_list)
#

colormode(255)
colors_list = [(208, 160, 82), (54, 89, 131), (146, 91, 40), (140, 26, 48), (222, 206, 108), (132, 177, 203),
               (158, 45, 83), (47, 55, 103), (167, 160, 38), (128, 189, 143), (84, 20, 44), (36, 42, 70),
               (187, 93, 105), (187, 139, 170), (84, 123, 181), (59, 39, 31), (78, 153, 165), (88, 157, 91),
               (195, 79, 72), (45, 74, 78), (161, 202, 220), (80, 73, 44), (57, 131, 121), (218, 176, 188),
               (220, 183, 166), (166, 207, 165)]


# creating turtle object
hirst_painting =  Turtle()
hirst_painting.hideturtle()
hirst_painting.speed("fastest")

x_pos = 0.00
y_pos = 0.00

# creating random colors function
def random_colors():
   color = random.choice(colors_list)
   return color


def draw_dots():
    for _ in range(10):
        hirst_painting.penup()
        hirst_painting.forward(20)
        hirst_painting.dot(10, random_colors())
        hirst_painting.forward(20)


for _ in range(10):
    draw_dots()
    hirst_painting.setx(x_pos)
    y_pos += 30
    hirst_painting.sety(y_pos)


<<<<<<< HEAD

=======
>>>>>>> ceeed8c5d2ba4574e8b3d27c35b7ccfbb9d7f0be
my_screen = Screen()
my_screen.exitonclick()
