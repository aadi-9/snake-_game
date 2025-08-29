from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color("red")
        self.speed(0)
        self.refresh()

    def refresh(self):
        randx = random.randint(-270, 270)
        randy = random.randint(-270, 270)
        self.goto(randx, randy)
