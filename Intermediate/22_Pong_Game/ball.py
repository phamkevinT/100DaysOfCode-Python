from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 3
        self.y_move = 3
        self.move_speed = 0.1

    def move(self):
        """Move the ball"""
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce_y(self):
        """Collision with top or bottom walls bounces the ball in opposite direction"""
        self.y_move *= -1

    def bounce_x(self):
        """Collision with the either paddle bounces ball in opposite direction and increases ball speed"""
        self.x_move *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        """Reset the ball position to middle of screen"""
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
