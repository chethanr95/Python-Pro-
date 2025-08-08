from turtle import Turtle, Screen
import random

window = Screen()
window.setup(width=800, height=400)
user_bet = window.textinput(title="Make your Bet!", prompt="Enter your Bet turtle color:")

turtles_list = [] 
colors = [ "indigo", "blue", "green", "yellow", "orange", "red" ]

#def setup race() :
y = -100
for index in range(0,6) :
    
    def arrange_start_line() :
        global y
        #print(y)
        turtles_list[index].goto(-350, y)
        y += 30
        #backward()

    #print(index)
    #turtles_list[index] = Turtle()
    #new_turtle = Turtle()
    turtles_list.append(Turtle(shape="turtle"))
    turtles_list[index].color(colors[index])
    turtles_list[index].penup()
    turtles_list[index].speed("fastest")
    arrange_start_line()
    #end finish xcor
    
race_finished = False

while not race_finished :

    for turtle in turtles_list :
           
        if turtle.xcor() >= 370 :
            winning_color = turtle.pencolor()
            if winning_color == user_bet :
                print("You Won")
        
            else :
                print("You Lost")

            print(f"Winner Color = {winning_color}")
            race_finished = True

        turtle.forward(random.randint(0,10))

window.exitonclick()