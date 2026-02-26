# import csv

# #weather = []
# temps = []

# with open("weather_data.csv", mode='r') as file:
#     weather = csv.DictReader(file)
#     for row in weather:
#         temps.append(int(row['temp']))

# print(temps)
# #print(weather[:])

import pandas

#data = pandas.read_csv("weather_data.csv")
# print(data)

# temp_list = data["temp"].to_list()

#hard way
# total = 0
# for _ in temp_list:
#     total += int(_)

#using sum
# print(sum(temp_list)/len(temp_list))

#using pandas
#print(data["temp"].mean())

# print(data[data.temp == data.temp.max()])

# monday = data[data.day == "Monday"]

# print((monday.temp[0] * 1.8) + 32)

# print(type(monday.temp))
# print(type(monday.temp[0]))

squirrel = pandas.read_csv("Squirrel.csv")

#Long way
# gray_squirrels = squirrel[squirrel["Primary Fur Color"] == "Gray"]
# cinnamon_squirrels = squirrel[squirrel["Primary Fur Color"] == "Cinnamon"]
# black_squirrels = squirrel[squirrel["Primary Fur Color"] == "Black"]


# squirrel_dict = {
#     "Colors": ["Gray", "Cinnamon", "Black"],
#     "Count": [len(gray_squirrels), len(cinnamon_squirrels), len(black_squirrels)]
# }

# print(pandas.DataFrame(squirrel_dict))

#Short way
sqc = squirrel["Primary Fur Color"].value_counts().reset_index()
sqc.columns = ["Color", "Count"]
print(sqc)

