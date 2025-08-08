from turtle import Turtle, Screen

my_turtle = Turtle()
my_turtle.shape("turtle")
my_turtle.color("coral")
my_turtle.forward(100)
#print(my_turtle)

my_screen = Screen()
#print(my_screen)
print(f"{my_screen.canvheight}, {my_screen.canvwidth}")


my_screen.exitonclick()