from turtle import Screen
from snake import Snake
import time

alive = True

my_screen = Screen()
my_screen.setup(width=600,height=600)
my_screen.bgcolor("black")
my_screen.listen()
my_screen.tracer(0)

my_snake = Snake(3,.75)

my_screen.listen()
my_screen.onkey(my_snake.up, "Up")
my_screen.onkey(my_snake.down, "Down")
my_screen.onkey(my_snake.left, "Left")
my_screen.onkey(my_snake.right, "Right")


while alive:
    my_snake.move()
    my_screen.update()
    time.sleep(.1)






my_screen.exitonclick()