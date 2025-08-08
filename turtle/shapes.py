import turtle as t
import random

new_t = t.Turtle()

#def draw_shape(num_sides, clr) :
def draw_shape(num_sides) :
    angle = 360 / num_sides
    #new_t.pencolor(clr)
    while num_sides != 0 :
        #print(f"number of sides = {num_sides}")
    
        new_t.forward(100)
        new_t.right(angle)
        num_sides -= 1

for sides in range(1,10) : 
    color = ["black", "blue", "red", "green", "violet", "orange", "yellow", "Indigo", "grey", "pink"]
    #draw_shape(sides,color[sides])
    new_t.color(color[sides])
    draw_shape(sides)

window = t.Screen()
window.exitonclick()    