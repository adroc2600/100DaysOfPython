from turtle import Turtle, Screen
from colors import rgb
import random
import threading
import queue

DOT_COUNT = 10_000
THREADS = 4

dot_queue = queue.Queue()

def generate_dots(n):
    for _ in range(n):
        dot_queue.put((
            random.randint(-250, 70),
            random.randint(-250, 190),
            random.randint(1, 40),
            random.choice(rgb)
        ))

screen = Screen()
screen.colormode(255)

t = Turtle()
t.hideturtle()
t.speed(0)
t.penup()

threads = []
per_thread = DOT_COUNT // THREADS

for _ in range(THREADS):
    th = threading.Thread(target=generate_dots, args=(per_thread,))
    th.start()
    threads.append(th)

screen.tracer(0)

drawn = 0
while drawn < DOT_COUNT:
    try:
        x, y, size, color = dot_queue.get(timeout=0.01)
        t.goto(x, y)
        t.dot(size, color)
        drawn += 1
    except queue.Empty:
        pass

screen.update()
screen.exitonclick()
