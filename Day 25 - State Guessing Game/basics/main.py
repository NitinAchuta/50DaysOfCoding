# with open('weather_data.csv') as data_file:
#     data = data_file.readlines()


# import csv

# with open('weather_data.csv') as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.apend(int(row[1]))
#     print(temperatures)

import pandas as pd
data = pd.read_csv('weather_data.csv')
# print(type(data))

# data_dict = data.to_dict()
# # print(data_dict)

# temp_list = data['temp'].to_list()

# # sum = sum(temp_list)
# # avg = sum/len(temp_list)
# # print(avg)

# print(data['temp'].max())
# #GET DATA IN COLUMN
# print(data['condition'])
# print(data.condition)

#GET DATA IN ROW
# print(data[data.day == 'Monday'])
# print(data[data.temp == data.temp.max()])

monday = data[data.day == 'Monday']
print(monday)
monday_temp = monday.temp[0]
print(monday_temp)
monday_temp_F = monday_temp * 9/5 + 32
print(monday_temp_F)

#Create a dataframe from scratch
# data_dict = {
#     'students': ['Amy', 'James', 'Angela'],
#     'scores': [76, 56, 65]
# }
# data = pd.DataFrame(data_dict)
# data.to_csv('new_data.csv')