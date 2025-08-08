import turtle as t
import random

tim = t.Turtle()
tim.speed("fastest")

t.colormode(255)

def random_color() :
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    color_tuple = (r, g, b)
    return color_tuple


def draw_spirograph(offset) :
    for _ in range(int(360 / offset)) :
        tim.color(random_color())    
        tim.circle(25)
        tim.circle(50)
        tim.circle(75)
        tim.circle(100)
        tim.circle(125)
        tim.circle(150)
        tim.setheading(tim.heading() + offset)



draw_spirograph(5) 

window = t.Screen()
window.exitonclick()