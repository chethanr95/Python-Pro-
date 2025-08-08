from turtle import Turtle
import random

#new snake segemnt positions
POSITIONS = [(0,0), (-20,0), (-40,0)]
COLORS = ["white", "gray", "pink", "red", "orange", "blue", "purple", "green", "purple", "coral", "silver"]
MOVE_STEPS = 20
SPEED = "slowest"
WALL_BORDER =299

#snake segments
segments = []

class Snake : 
    
    def __init__(self) :
        
        for position in POSITIONS :
            self.create_snake(position)
            #self.create_segment(position)
            self.head = segments[0]
            self.head.shape("triangle")
            
    #create inital snake with default 3 segments, initial default position known
    def create_snake(self, position) :
    #def create_segment(self, position) :
    
        segment = Turtle(shape="square")
        segment.shapesize(stretch_len = 0.8, stretch_wid = 0.8)
        segment.penup()
        segment.color(random.choice(COLORS))
        #segment.color("white")
        segment.goto(position)
        segment.speed(SPEED)

        #add each segment into segments list
        self.append_segments(segment)

    def append_segments(self, segment) :

        segments.append(segment)


    #create individual segments upon food eaten , position unknown, behind the last segment's position
    def create_new_segment(self, food_color) :
        new_segment = Turtle(shape="square")
        new_segment.shapesize(stretch_len = 0.8, stretch_wid = 0.8)
        new_segment.penup()
        new_segment.color(random.choice(COLORS))
        #new_segment.color(food_color)
        new_segment_x = segments[-1].xcor()
        new_segment_y = segments[-1].ycor()
        new_segment.goto( new_segment_x, new_segment_y)
        new_segment.speed(SPEED)
        self.append_segments(new_segment)


    #grow snake segment upon food eaten
    def grow(self, food_color) :
        self.create_new_segment(food_color)

    #onkey movement functions
    def move_up(self) :
        head_direction = self.head.heading()
        if head_direction != 90 and head_direction != 270 :
            self.head.setheading(90)


    def move_down(self) :
        head_direction = self.head.heading()
        if head_direction != 90 and head_direction != 270 :
            self.head.setheading(270)

    def move_left(self) :
        head_direction = self.head.heading()
        if head_direction != 0 and head_direction != 180 :
            self.head.setheading(180)

    def move_right(self) :
        head_direction = self.head.heading()
        if head_direction != 0 and head_direction != 180 :
            self.head.setheading(0)

    #default game movement without onkey
    def move(self) :
        """snake head to be moving,
       and snake segments to follow the head
       initial snake index: 0 = head, 1 = head-1 = middle, 2 =head-2 = last""" 
        import time
        #working correctly
        #time.sleep(1)
        #for index in range(1, len(segments)-1) :
        for index in range(len(segments)-1, 0, -1) :
            #print(f"--itr index {index}-----")
            cur_x = segments[index].xcor()
            cur_y = segments[index].ycor()
            #print(f"cur_x = {cur_x} , cur_y = {cur_y}")
            prev_x = segments[index-1].xcor()
            prev_y = segments[index-1].ycor()
            #print(f"prev_x = {prev_x} , prev_y = {prev_y}")
            
            segments[index].goto(prev_x,prev_y)

        self.head.forward(MOVE_STEPS)

    #snake wall hit
    def wall_hit(self) :
        head_x_cor = self.head.xcor()
        head_y_cor = self.head.ycor()

        if head_x_cor > WALL_BORDER or head_x_cor < -WALL_BORDER : 
            return True
        elif head_y_cor > WALL_BORDER or head_y_cor < -WALL_BORDER :
            return True
        else :
            return False
        
    #snake body hit, not the head itslef
    def body_hit(self) :
        #for segment in segments[1:] :
        for segment in segments[3:] :    
            if self.head.distance(segment) <= 0.0 :
                return True



