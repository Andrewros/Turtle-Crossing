from turtle import Turtle
import random


class Car(Turtle):
    def __init__(self, car_color):
        super().__init__()
        self.color(car_color)
        self.setheading(180)
        self.pu()
        self.goto(x=310, y=random.randint(-260, 260))
        self.shape("square")
        self.shapesize(stretch_len=3, stretch_wid=1.5)
        self.level = 1

    def move(self):
        self.forward(7*(.66*self.level))
