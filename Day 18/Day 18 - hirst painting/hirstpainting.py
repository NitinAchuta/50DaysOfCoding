#Hirst painting
# import colorgram as cg
# colors = cg.extract('hirstpainting.jpg', 30)
# rgb_colors = []

# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)

# print(rgb_colors)

'''
REQUIREMENTS:
- 10 x 10 rows of spots
- Each dot should be around 20 in size
    - spaced apart by 50 paces
'''

import turtle as t
import random
t.colormode(255)

def random_color():
    return random.choice(color_list)

def draw_row():
    for i in range(10):
        tim.dot(20, random_color())
        tim.forward(50)

def draw_pic():
    for i in range(10):
        tim.setpos(0,  i * 50)
        draw_row()

color_list = [(251, 240, 247), (236, 243, 250), (236, 226, 85), (211, 159, 109), (115, 176, 211), (202, 5, 69), 
 (231, 53, 126), (195, 77, 20), (215, 133, 176), (194, 163, 14), (33, 106, 169), (10, 20, 65), (30, 189, 116), (232, 224, 4), (18, 28, 172), 
 (234, 165, 197), (121, 187, 159), (203, 31, 130), (12, 186, 212), (10, 46, 25), (143, 216, 200), (43, 17, 11), (39, 132, 71), (107, 92, 210), 
 (182, 15, 8), (127, 219, 233), (233, 71, 40), (169, 178, 229)]


tim = t.Turtle()
tim.pu()
tim.speed('fastest')
tim.hideturtle()
draw_pic()

screen = t.Screen()
screen.exitonclick()