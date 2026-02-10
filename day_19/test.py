from turtle import Turtle, Screen
import random

color_list = {"red","green","blue","yellow","purple","black"}
turtles_list = []
screen_height = 500
screen_width = 500

my_screen = Screen()
my_screen.setup(width=screen_width, height=screen_height)
guess = my_screen.textinput("Guess", "Guess the winner:")

for t in range(0, 6):
    tim = Turtle(shape="turtle")
    print(f"Turtle: {t} = {tim}")


my_screen.exitonclick()