from turtle import Turtle, Screen


tim = Turtle()
tim.shape("arrow")
tim.color("green")

tim.forward(100)
tim.right(135)
tim.forward(140)
tim.right(135)
tim.forward(100)
tim.right(135)
tim.forward(140)
tim.left(135)
tim.forward(95)

display = Screen()
display.exitonclick()