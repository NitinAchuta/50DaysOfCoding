from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        """Initialize the ball"""
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.pu()
        self.x_move = 10
        self.y_move = 10
        self.move_speed = 0.1

    def move(self):
        """Make the ball move towards the top right"""
        global y_direction
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)


    def bounce_y(self):
        """Make the ball bounce off the top wall"""
        self.y_move *= -1

    def bounce_x(self):
        """Make the ball bounce off the paddle"""
        self.x_move *= -1
        self.move_speed *= 0.8

    def reset_position(self):
        """Reset the ball position (should only run when ball misses the r_paddle)"""
        self.goto(0, 0)
        self.bounce_x()
        self.move_speed = .1
