from turtle import Screen
from rookie_turtle import RookieTurtle
from scorecard import Levelcard
#from cars import Cars
from new_cars import Cars
import time



#screen setup 
screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor("white")
screen.title("Crossing")

#turn off screen animation
screen.tracer(0)

#create the turtle
rookie = RookieTurtle()

#create scorecard
score = Levelcard()

#create the cars for level 1
num_cars = 3
cars = []
for i in range(0,num_cars) :
    new_car = Cars()
    cars.append(new_car)
    
#event listener, with onkey()
screen.listen()

is_game_on = True
#main game 
while is_game_on :
    
    time.sleep(0.1)
    
    #to be used along with tracer
    screen.update()

    #turtle move up on key press
    screen.onkey(key="Up", fun = rookie.move_up)

    #each car to be moving
    for i in range(0,num_cars) :
        cars[i].keep_moving()
        
        #Detect car hit the turtle, game over
        if cars[i].car.distance(rookie) <= 15 :
            score.game_over()
            is_game_on = False
    

    #turtle successfully crossed the road
    #level up , add new car onto the road,  turtle restart
    if rookie.ycor() >= 270 : 
        score.level_up()
        rookie.reposition()
        num_cars += 1
        new_car = Cars()
        cars.append(new_car) 


#the last line
screen.exitonclick()