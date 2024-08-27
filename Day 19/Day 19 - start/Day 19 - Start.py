# day 19 start
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def clear_drawing():
    tim.reset()

def counter_clock():
    tim.left(10)

def clock():
    tim.right(10)

screen.listen()
screen.onkey(key='w', fun=move_forwards)
screen.onkey(key ='s', fun=move_backwards)
screen.onkey(key='a', fun=counter_clock)
screen.onkey(key='d', fun=clock)
screen.onkey(key='c', fun=clear_drawing)


screen.exitonclick()