
from turtle import Turtle
statring_position = [(0, 0), (-20, 0), (-40, 0)]
move_destance = 20
up = 90
down = 270
left = 180
right = 0


segments = []

class Snake:
    def __init__(self):
        # self.segments = None
        self.segment = []
        self.create_snake()
        self.speed = 1
        self.head = self.segment[0]
    def create_snake(self):
        for position in statring_position:
            self.add_segment(position)
    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segment.append(new_segment)

    def extend(self):
        self.add_segment(self.segment[-1].position())
    def move(self):
        self.speed = 1
        for seg_num in range(len(self.segment)-1, 0, -1):
            new_x = self.segment[seg_num - 1].xcor()
            new_y = self.segment[seg_num - 1].ycor()
            self.segment[seg_num].goto(new_x, new_y)
        self.segment[0].forward(move_destance)
    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        self.head.setheading(down)
    def left(self):
       self.head.setheading(left)
    def right(self):
        self.head.setheading(right)
