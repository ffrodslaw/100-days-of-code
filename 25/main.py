# Day 25: Csv in Pandas
import pandas

# with open("weather_data.csv") as weather_data:
#     data = weather_data.readlines()
#
#     print(data)
#
# import csv
#
# temperatures = []
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)   # one row for each element of csv
#     for row in data:
#         print(row)
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
# print(temperatures)

# Pandas makes it easier
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# print(type(data))
# print(data["temp"])
#
# data_dict = data.to_dict()
# print(data_dict)
#
# temp_list = data["temp"].to_list()
# print(temp_list)
#
# # average temperature
# print(sum(temp_list)/len(temp_list))
#
# # easier:
# print(data["temp"].mean())
#
# # maximum temperature
# print(data["temp"]. max())
#
# # Get data in columns:
# print(data["condition"])
# print(data.condition)
#
# # Get data in rows:
# print(data[data.day == "Monday"])
# print(data[data.temp == data.temp.max()])  # which row had highest temperature?
#
# monday = data[data.day ==  "Monday"]
# print(monday.condition)
# # temp in fahrenheit
# print(monday.temp * 9/5 + 32)
#
# # Create dataframe from scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
#
# data = pandas.DataFrame(data_dict)
# print(data)
# data.to_csv("new_data.csv")

##################
#### Squirrel analysis

squirrel_data = pandas.read_csv("squirrel_data.csv")

black_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Black"])
gray_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Gray"])
cinnamon_squirrels = len(squirrel_data[squirrel_data["Primary Fur Color"] == "Cinnamon"])

squirrel_dict = {
    "Fur Color": ["black", "Gray", "Cinnamon"],
    "Count": [black_squirrels, gray_squirrels, cinnamon_squirrels]
}

squirrel_df = pandas.DataFrame(squirrel_dict)
squirrel_df.to_csv("squirrel_count.csv")