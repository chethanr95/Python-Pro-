from turtle import Turtle, Screen

tim = Turtle()

def move_forward() :
    tim.color("green")
    tim.forward(10)

def move_backward() :
    tim.color("red")
    tim.backward(10)

def move_left() :
    tim.color("yellow")
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)

def move_right() :
    tim.color("blue")
    new_heading = tim.heading() -10
    tim.setheading(new_heading)

def clear() :
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()



window = Screen()
window.listen()
window.onkey(key = "w", fun = move_forward )
window.onkey(key="s", fun=move_backward)
window.onkey(key="a", fun=move_left)
window.onkey(key="d", fun=move_right)
window.onkey(key="c", fun=clear)








window.exitonclick()

