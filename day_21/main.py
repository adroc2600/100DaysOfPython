from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

alive = True

my_screen = Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("black")
my_screen.listen()
my_screen.tracer(0)
my_scoreboard = Scoreboard()

my_snake = Snake(3)
my_food = Food()


my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")


while alive:
    my_snake.move()
    my_screen.update()
    time.sleep(.2)

    if my_snake.head.distance(my_food) <= 15:
        my_food.move()
        my_snake.grow()
        my_scoreboard.update_score()

    if my_snake.head.xcor() > 270 or my_snake.head.xcor() < -270 or my_snake.head.ycor() > 270 or my_snake.head.ycor() < -270:
        my_scoreboard.game_over()
        alive = False

    for s in my_snake.snake_list[1:]:
        if my_snake.head.distance(s) < 10:
            my_scoreboard.game_over()
            alive = False






my_screen.exitonclick()