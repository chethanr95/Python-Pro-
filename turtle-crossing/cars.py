from turtle import Turtle
import random
import time


COLORS = ["violet", "indigo", "blue", "green", "orange", "yellow", "red"]
Y_BORDER = 270
#list of cars on the screen
cars = []
##MOVE_STEPS = 5
SPEED = 10


class Cars : 
  
    def __init__(self) :
        self.move_steps = 0
        self.num_cars = random.randint(8,13)
        self.create_multiple_cars()
        

    def append_car(self, mycar) :
        cars.append(mycar)        

    def set_position(self, my_car, position) :
        my_car.goto(position)

    def create_car(self) :
        my_car = Turtle()
        my_car.speed(SPEED)
        my_car.color(random.choice(COLORS))
        my_car.shape("square")
        my_car.shapesize(stretch_wid = 0.7, stretch_len = 1.3)
        my_car.penup()
        position = self.get_start_position()
        #my_car.goto(position)
        self.set_position(my_car, position)

        return my_car


    def create_multiple_cars(self) :
        
        for i in range (0, self.num_cars) :
            car = self.create_car() 
            self.append_car(car)


    def get_start_position(self) :
        
        #x is always fixed from right edge of the screen
        x = random.randint(10, 270)
        y = random.randint(-Y_BORDER, Y_BORDER)
        return (x,y)
    

    def keep_moving(self) :
        for car in cars :
            #move on x axis only, y axis is fixed
            #new_x = car.xcor() - MOVE_STEPS
            #time.sleep(0.2)
            self.move_steps = random.randint(5,10)
            new_x = car.xcor() - self.move_steps
            #car.goto(new_x, car.ycor())
            position = (new_x, car.ycor()) 
            self.set_position(car, position)

            if car.xcor() < -260 :
                #(new_x,new_y) = self.get_start_position()
                #car.goto(new_x, new_y)
                self.set_position(car, self.get_start_position())
            #self.create_multiple_cars()

