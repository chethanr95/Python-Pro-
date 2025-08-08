from turtle import Turtle
import random


COLORS = ["violet", "indigo", "blue", "green", "orange", "yellow", "red"]
SPEED = 10
Y_BORDER = 270


class Cars :
    
    def __init__(self) :
        
        self.car = Turtle()
        self.car.speed(SPEED)
        self.car.color(random.choice(COLORS))
        self.car.shape("square")
        self.car.shapesize(stretch_wid = 0.7, stretch_len = 1.3)
        self.car.penup()

        self.car_position = self.get_start_position()
        #my_car.goto(position)
        self.set_position(self.car_position)


    def set_position(self, position) :
        self.car.goto(position)


    def get_start_position(self) :
        
        #x is always fixed from right edge of the screen
        x = random.randint(10, 270)
        y = random.randint(-Y_BORDER, Y_BORDER)
        return (x,y)
    

    def keep_moving(self) :
    
            move_steps = random.randint(5,10)
            new_x = self.car.xcor() - move_steps
            new_y = self.car.ycor()
            position = (new_x, new_y)
            self.set_position(position)
            
            #car movead ahead the turtle, reset 
            if self.car.xcor() < -220 :
                 self.set_position(self.get_start_position())