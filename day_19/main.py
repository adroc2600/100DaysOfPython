from turtle import Turtle, Screen
import random

color_list = {"red","green","blue","yellow","purple","black"}
turtles_list = []
screen_height = 500
screen_width = 500

my_screen = Screen()
my_screen.setup(width=screen_width, height=screen_height)
guess = my_screen.textinput("Guess", "Guess the winner:")


y = -140
for color in color_list:
    t = Turtle(shape="turtle", visible=False)
    t.penup()
    t.fillcolor(color)
    t.shapesize(2, 2)
    turtles_list.append(t)
    t.teleport(-220,y)
    y += 60
    t.showturtle()

# for t in turtles_list:
#     t.showturtle()

race_on = True
while race_on:
    for t in turtles_list:
        if t.xcor() <= 200:
            t.forward(random.randint(0,20))
        else:
            winner = t.fillcolor()
            race_on = False
            break

if guess == winner:
    print(f"You guessed correct, the winner was {winner}")
else:
    print(f"You guessed wrong, the winner was {winner}")

my_screen.exitonclick()