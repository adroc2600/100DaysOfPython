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


