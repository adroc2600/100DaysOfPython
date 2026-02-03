from turtle import Turtle, Screen
import random
import time

from prettytable import PrettyTable

# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("blue")

# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)
# timmy.left(90)
# timmy.forward(100)

# my_screen = Screen()
# my_screen.exitonclick()

align = ["l", "c", "r"]
fields = ["City name", "Area", "Population", "Annual Rainfall"]

table = PrettyTable()

table.add_column(fields[0],
["Adelaide","Brisbane","Darwin","Hobart","Sydney","Melbourne","Perth"])
table.add_column(fields[1], [1295, 5905, 112, 1357, 2058, 1566, 5386])
table.add_column(fields[2], [1158259, 1857594, 120900, 205556, 4336374, 3806092,
1554769])
table.add_column(fields[3],[600.5, 1146.4, 1714.7, 619.5, 1214.8, 646.9,
869.4])

while True:
  print(table)
  choice = random.choice(align)
  table.align = choice
  sort_by = random.choice(fields)
  print(table.get_string(sortby=sort_by))
  
  time.sleep(1)