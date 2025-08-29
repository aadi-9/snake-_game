from turtle import Turtle

X1 = [(0, 0), (-20, 0), (-40, 0)]
DIST = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.turtles = []
        self.createsnake()

    def createsnake(self):
        for x in X1:
            self.addseg(x)

    def addseg(self, x):
        leo = Turtle("square")
        leo.color("white")
        leo.penup()
        leo.goto(x)
        self.turtles.append(leo)

    def extendsnk(self):
        self.addseg(self.turtles[-1].position())

    def reset(self):
        for seg in self.turtles:
            seg.goto(1000,1000)
        self.turtles.clear()
        self.createsnake()


    def move(self):
        for x in range(len(self.turtles) - 1, 0, -1):
            newx = self.turtles[x - 1].xcor()
            newy = self.turtles[x - 1].ycor()
            self.turtles[x].goto(newx, newy)
        self.turtles[0].forward(DIST)

    def up(self):
        if self.turtles[0].heading() != DOWN:
            self.turtles[0].setheading(UP)

    def down(self):
        if self.turtles[0].heading() != UP:
            self.turtles[0].setheading(DOWN)

    def left(self):
        if self.turtles[0].heading() != RIGHT:
            self.turtles[0].setheading(LEFT)

    def right(self):
        if self.turtles[0].heading() != LEFT:
            self.turtles[0].setheading(RIGHT)
