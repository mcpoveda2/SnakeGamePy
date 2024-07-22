from turtle import Screen, Turtle
from  Snake import Snake
import time

#Screen Setuo
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game by Michael Poveda")
screen.tracer(0)

snake = Snake()

#Inicio del juego
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(1)

    snake.move()

screen.exitonclick()