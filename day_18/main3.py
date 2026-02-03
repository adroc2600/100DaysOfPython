from turtle import Turtle, Screen
import random

colors = ["blue", "red", "green", "yellow", "purple","black", "orange"]
my_turtle = Turtle()
my_screen = Screen()
sides = 3

while sides <= 10:

  deg = 360/sides
  color = random.choice(colors)
  my_turtle.color(color)
  for _ in range(sides):
    my_turtle.forward(100)
    my_turtle.left(deg)
  sides += 1


my_screen.exitonclick()