import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

def move_amount(low=1, high=10) -> int:
    return random.randint(low, high)


WIDTH = 600
HEIGHT = 600

low_speed = 1
high_speed = 20

y_cords = []
num_cars = 10
counter = 0
start_x = int(WIDTH/2)
y_range = int(HEIGHT/2) -40
cars = []


my_screen = Screen()
my_screen.setup(WIDTH, HEIGHT)
my_screen.tracer(0)
my_screen.listen()

my_score = Scoreboard()
my_turtle = Player()

my_screen.onkey(my_turtle.move_up, "Up")
my_screen.onkey(my_turtle.move_down, "Down")
my_screen.onkey(my_turtle.move_left, "Left")
my_screen.onkey(my_turtle.move_right, "Right")

num = 10

while num <= y_range:
    y_cords.append(num)
    y_cords.append(-num)
    num += 22
random.shuffle(y_cords)


game_is_on = True
while game_is_on:
    if counter < num_cars:
        #start_y = random.randrange(-y_range, y_range)
        car = CarManager(start_x=start_x, start_y=random.choice(y_cords))
        cars.append(car)
        counter += 1
        car.move(move_amount(low_speed, high_speed))
        my_screen.update()
        
    for car in cars:
        car.move(move_amount(low_speed, high_speed))
        my_screen.update()

        #Detect collision
        if my_turtle.distance(car) <= 15:
            my_score.game_over()
            game_is_on = False

        #Detect crossing finish line
        if my_turtle.ycor() >= y_range:
            my_score.update_score()
            low_speed += 10
            high_speed += 10
            num_cars += 10
            my_turtle.go_home()


        if car.xcor() < -start_x:
            cars.remove(car)
            car.clear()
            car.hideturtle()
            del car    
            counter -= 1


    time.sleep(0.1)
    my_screen.update()

my_screen.exitonclick()
