import turtle as t
import random

new_t = t.Turtle()
t.colormode(255)

def random_color() :
    r = random.randint(1,255)
    g = random.randint(1,255)
    b = random.randint(1,255)
    color_tuple = (r,g,b)
    return color_tuple

direction = [0, 90, 180,270]
new_t.pensize(6)
new_t.speed("fastest")

for _ in range (300) :
    new_t.color(random_color())
    new_t.forward(25)
    new_t.setheading(random.choice(direction))

my_screen = t.Screen()
my_screen.exitonclick()