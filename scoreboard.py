from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 18, "normal")


class ScoreBoard(Turtle):

    def __init__(self):

        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.high_score = int(file.read())
        self.color("white")
        self.penup()
        self.goto(0, 280)
        self.hideturtle()
        self.update()

    def update(self):
        self.clear()
        self.write(f" score: {self.score}     High score: {self.high_score}", False, ALIGN, FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update()

    def scoreinc(self):
        self.score += 1
        self.update()
