from turtle import Screen
import time
from Snake import Snake
from food import Food
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = ScoreBoard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

gameon = True
while gameon:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.turtles[0].distance(food) < 15:
        food.refresh()
        snake.extendsnk()
        scoreboard.scoreinc()

    if (snake.turtles[0].xcor() > 290 or snake.turtles[0].xcor() < -290 or snake.turtles[0].ycor() > 290 or
            snake.turtles[0].ycor() < -290):
        scoreboard.reset()
        snake.reset()

    for turt in snake.turtles[1:]:
        if snake.turtles[0].distance(turt) < 10:
            scoreboard.reset()
            snake.reset()

screen.exitonclick()
