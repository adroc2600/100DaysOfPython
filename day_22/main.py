from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

WIDTH = 800
HEIGHT = 600

TOP_BOUNDRY = HEIGHT/2 - 20
BOTTOM_BOUNDRY = -TOP_BOUNDRY
RIGHT_BOUNDRY = WIDTH/2 - 50
LEFT_BOUNDRY = -RIGHT_BOUNDRY

my_screen = Screen()
my_screen.setup(width=WIDTH,height=HEIGHT)
my_screen.bgcolor("black")
my_screen.listen()
my_screen.tracer(0)
my_screen.title("Pong")

my_score = Score()

right_paddle = Paddle(x=350, y=0)
left_paddle = Paddle(x=-350, y=0)
my_ball = Ball()

my_screen.onkey(right_paddle.move_up, "i")
my_screen.onkey(right_paddle.move_down, "k")

my_screen.onkey(left_paddle.move_up, "w")
my_screen.onkey(left_paddle.move_down, "s")

while True:
    _, paddle_height, _ = right_paddle.turtlesize()
    paddle_height *= 20

    #Detect if ball hit right paddle
    if my_ball.ycor() >= right_paddle.ycor() - paddle_height/2 and my_ball.ycor() <= right_paddle.ycor() + paddle_height/2:
        if int(my_ball.xcor()) >= RIGHT_BOUNDRY:
            my_ball.hit_paddle()
            
    #Detect if ball hit left paddle
    if my_ball.ycor() >= left_paddle.ycor() - paddle_height/2 and my_ball.ycor() <= left_paddle.ycor() + paddle_height/2:
        if int(my_ball.xcor()) <= LEFT_BOUNDRY:
            my_ball.hit_paddle()
    
    #Detect if left scored
    if int(my_ball.xcor()) > RIGHT_BOUNDRY:
        my_score.update_left_score()
        my_ball.reset()

    #Detect if right scored
    if int(my_ball.xcor()) < LEFT_BOUNDRY:
        my_score.update_right_score()
        my_ball.reset()

    #Detect if ball hits top or bottom
    if my_ball.ycor() > TOP_BOUNDRY or my_ball.ycor() < BOTTOM_BOUNDRY:
        my_ball.bounce()

    my_ball.move()
    my_screen.update()
    time.sleep(.009)


my_screen.exitonclick()