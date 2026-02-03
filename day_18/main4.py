from turtle import Turtle, Screen
from colors import colors
import random

my_colors = colors
angles = [0,90,180,270]
my_turtle = Turtle()
my_screen = Screen()
my_turtle.hideturtle()


def draw(name, speed, size, distance, angles, colors):
    name.pensize(size)
    name.speed(speed)
    color = random.choice(colors)
    #angle = random.choice(angles)
    name.color(color)
    name.forward(distance)
    #name.setheading(angle)
    name.right(angles)



for _ in range(500):

  deg = random.randint(1,360)
  print(deg)
  draw(my_turtle, 10, random.randint(1,10), random.randint(1,50), deg, my_colors)

my_screen.exitonclick()