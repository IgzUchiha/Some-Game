import time
from turtle import Screen
from item import Item


item = Item()
screen = Screen()
screen.setup(width=700, height=700)
screen.bgcolor("black")
screen.title("Some Game")
screen.tracer(0)

game_is_on = True
while game_is_on:
    screen.update()

    screen.exitonclick()