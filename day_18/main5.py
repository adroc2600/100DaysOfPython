from turtle import Turtle, Screen
from colors import colors
import random

my_colors = colors
my_turtle = Turtle()
my_screen = Screen()
my_turtle.hideturtle()

my_turtle.speed(0)
gap_size = 7
for _ in range(int(360 / gap_size)):
  color = random.choice(colors)
  my_turtle.color(color)
  my_turtle.circle(100)
  my_turtle.right(gap_size)

my_screen.exitonclick()