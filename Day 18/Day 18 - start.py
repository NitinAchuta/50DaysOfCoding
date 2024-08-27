#Day 18 start
import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    # r = random.randint(0,255)
    # g = random.randint(0, 255)
    # b = random.randint(0, 255)
    # random_color = (r, g, b)
    # return random_color
    return random.choice(color_list)

color_list = [(251, 240, 247), (236, 243, 250), (236, 226, 85), (211, 159, 109), (115, 176, 211), (202, 5, 69), 
 (231, 53, 126), (195, 77, 20), (215, 133, 176), (194, 163, 14), (33, 106, 169), (10, 20, 65), (30, 189, 116), (232, 224, 4), (18, 28, 172), 
 (234, 165, 197), (121, 187, 159), (203, 31, 130), (12, 186, 212), (10, 46, 25), (143, 216, 200), (43, 17, 11), (39, 132, 71), (107, 92, 210), 
 (182, 15, 8), (127, 219, 233), (233, 71, 40), (169, 178, 229)]

tim.pensize(1)
tim.speed(0)

for i in range (0,360, 5):
    tim.color(random_color())
    tim.setheading(i)
    tim.circle(100)



screen = t.Screen()
screen.exitonclick()
