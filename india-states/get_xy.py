import turtle

map_gif_file = "/Users/ChethanR/OneDrive - kyndryl/Pictures/python/Code/india-states/india-map.gif"

my_turtle = turtle.Turtle()
my_turtle.penup()


#create screen object
screen = turtle.Screen()
screen.title("India-states")
screen.addshape(map_gif_file)
my_turtle.shape(map_gif_file)


def get_x_y(x,y) :
    print(x,y)
turtle.onscreenclick(get_x_y)
turtle.mainloop()

screen.exitonclick()
