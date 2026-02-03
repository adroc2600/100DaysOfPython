from colors import rgb
from turtle import Turtle, Screen
import random

# import colorgram

# colors_obj = colorgram.extract('image.jpg', 1000)
# colors_list = []

# for x in colors_obj:
#     #print(f"X: {x}")
#     colors_list.append(x.rgb[0:3])
# print(colors_list)

x = -250
y = -250
count = 1
size = 20

my_colors = rgb
my_turtle = Turtle()
my_screen = Screen()
my_turtle.hideturtle()
my_turtle.speed(10)
my_screen.colormode(255)
my_turtle.teleport(-250,-250)
# IN A GRID
# for _ in range(100):
#     if count == 10:
#         x = -250
#         y += 40
#         count = 1
#         print(f"Y: {y}")

#     color = random.choice(my_colors)
#     my_turtle.dot(size, color)
#     my_turtle.teleport(x, y)
#     print(f"X: {x}")
#     x += 40
#     count += 1

#RANDOM
for _ in range(10000):
    rand_x = random.randint(-250, 70)
    rand_y = random.randint(-250, 190)
    rand_size = random.randint(1,40)
    color = random.choice(my_colors)
    my_turtle.dot(rand_size, color)
    my_turtle.teleport(rand_x, rand_y)

my_screen.exitonclick()