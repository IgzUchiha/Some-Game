from turtle import Turtle
# from web3 import Web3
import random

UP = "space"
DOWN = ""


class Item(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.shapesize(stretch_len=1, stretch_wid=1)
        self.color("blue")
        self.speed("fastest")

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)

    def up(self):
        if self.head.heading() != DOWN:
            self.segments[0].setheading(UP)
