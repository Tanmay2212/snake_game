from turtle import Turtle

X_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]  # List of starting coordinates
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in X_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        snake = Turtle(shape="square")
        snake.penup()
        snake.color("crimson")
        snake.goto(position)  # Use coordinates directly
        self.segments.append(snake)

    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move(self):
         for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
         self.head.forward(MOVE_DISTANCE)
            
    def Up(self):
        if self.head.heading() !=DOWN:
            self.head.setheading(UP)


    def Down(self):
        if self.head.heading() !=UP:
            self.head.setheading(DOWN)
        
        

    def Left(self):
         if self.head.heading() !=RIGHT:
            self.head.setheading(LEFT)


    def Right(self):
         if self.head.heading() !=LEFT:
            self.head.setheading(RIGHT)

