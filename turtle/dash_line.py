import turtle as t

tim = t.Turtle()

for _ in range(1, 16) :
    tim.pensize(4)
    tim.pencolor("blue")
    tim.forward(10)
    tim.penup()
    tim.forward(10)
    tim.pendown()

window = t.Screen()
window.exitonclick()
