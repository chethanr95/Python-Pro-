import turtle
import pandas

map_gif_file = "/Users/ChethanR/OneDrive - kyndryl/Pictures/python/Code/india-states/india-map.gif"
map_csv_file = "/Users/ChethanR/OneDrive - kyndryl/Pictures/python/Code/india-states/all-states.csv"

#create turtle object
my_turtle = turtle.Turtle()
my_turtle.penup()


#create screen object
screen = turtle.Screen()
screen.title("India-states")
screen.addshape(map_gif_file)
my_turtle.shape(map_gif_file)

#Preapare list of all states from the csv from pandas
states_df = pandas.read_csv(map_csv_file)
all_states_list = states_df.State.to_list()
#print(all_states_list)
guessed_states_list=[]

#main logic control
while len(guessed_states_list) <= len(all_states_list) :
    #prompt window 
    state_entered = screen.textinput(title=f"{len(guessed_states_list)}/{len(all_states_list)} guessed", prompt="Enter the State Name:")
    state_entered = state_entered.title() 

    if state_entered == "Exit" :
        break #out of the while loop
    
    else: 
        if state_entered in all_states_list :
            
            guessed_states_list.append(state_entered)
            

            state_line_ds = states_df[states_df.State == state_entered]
            #print(state_line_ds)
            
            #x = state_line_ds.Latitude.
            #state = state_line_ds.State.item()
            x = state_line_ds.Latitude.item()
            y = state_line_ds.Longitude.item()
            #print(x,y)
            position=(x,y)
            

            my_turtle.goto(position)
            my_turtle.write(state_entered)

            #print(guessed_states_list)

           



screen.exitonclick()

