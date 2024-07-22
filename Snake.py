from turtle import Screen, Turtle

START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
class Snake():

    def __init__(self):
         # Posiciones
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in START_POSITION:
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.segments.append(segment)

    def move(self):
        for seg in range(len(self.segments) - 1, 0, -1):
            posx = self.segments[seg - 1].xcor()
            posy = self.segments[seg - 1].ycor()
            self.segments[seg].goto(posx, posy)
        self.segments[0].forward(20)