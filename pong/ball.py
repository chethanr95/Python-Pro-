from turtle import Turtle
import random
import time

COLORS = ["violet", "indigo", "blue", "green", "orange", "yellow", "red"]

class Ball(Turtle) :
    def __init__(self) :
        super().__init__()
        self.shape("circle")
        self.penup()
        self.x_steps = 10
        self.y_steps = 10
        self.color(random.choice(COLORS))
        self.goto(0,0)
        
      

    def keep_moving(self) :
        new_x = self.xcor() + self.x_steps
        new_y = self.ycor() + self.y_steps
        self.goto(new_x, new_y)


    def bounce_y(self) :
        """ball hit the Top or Bottom Wall when keep_moving """
        #xcor should keep moving with increment, no change
        #ycor shoud should decement. i.e. +10 step move shall be -10 step
        self.y_steps *= -1

    def bounce_x(self) :
        """Left or Right Paddle Hit the ball """  
        #xcor should be decremented
        #ycor will decrement upon wall hit with biunce_y  
        self.x_steps *= -1

    def reset(self) :
        time.sleep(0.1)
        """upon scoring a point, paddle missed the ball""" 
        self.color(random.choice(COLORS))
        self.goto(0,0)  
        self.bounce_x()