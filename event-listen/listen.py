#from turtle import Turtle, Screen
import turtle

#tim = Turtle()
tim = turtle.Turtle()

def forward() :
    tim.forward(20)

#window = Screen()
window = turtle.Screen()


window.listen()
window.onkey(key="space", fun=forward)
window.exitonclick()
