#colors = colorgram.extract(image.jpg, number_of_colors)

import turtle as t, random

colors = [(90, 190, 210), (55, 195, 44), (20, 90, 190), (33, 50, 90), (150, 130, 200), (180, 146, 179), (56, 20, 80), (130, 120, 240), (185, 233, 166), ( 180, 20, 230)]
t.colormode(255)

tim = t.Turtle()
tim.speed("fastest")
tim.shape("turtle")
tim.color("green")
tim.penup()


#move turtle to initial dot start position from its default center position
tim.setheading(225)
tim.forward(250)
tim.setheading(0)


number_of_dots = 101

for dot_num in range(1, number_of_dots) :
    #dom(diameter_size, color)
    tim.dot(8, random.choice(colors))
    tim.forward(50)

    if  dot_num % 10 == 0 :
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)
        



window = t.Screen()
window.exitonclick()