import pandas as pd

#Get a count of number of each fur color in 'Primary Fur Color' column
data = pd.read_csv('2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')

squirrels = data['Primary Fur Color']

colors = {
    'cinnamon': 0,
    'gray': 0,
    'black': 0
}
for color in squirrels:
    if color == 'Cinnamon':
        colors["cinnamon"] += 1
    elif color == 'Gray':
        colors["gray"] += 1
    else:
        colors["black"]  +=1

print(colors)

"""BOTH DO THE SAME THING"""
# gray_squirrels_count = len(data[data['Primary Fur Color'] == 'Gray'])
# cinnamon_squirrels_count = len(data[data['Primary Fur Color'] == 'Cinnamon'])
# black_squirrels_count = len(data[data['Primary Fur Color'] == 'Black'])

# print(cinnamon_squirrels_count, gray_squirrels_count, black_squirrels_count)

colors_df = pd.DataFrame(colors.items())
print(colors_df)