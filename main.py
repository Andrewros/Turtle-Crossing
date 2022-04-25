from turtle import Screen, Turtle
import time
from car import Car
import random
from levelboard import Scoreboard

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


def up():
    turtle.forward(10)
    screen.update()


screen = Screen()
WIDTH, HEIGHT = 600, 600
screen.setup(width=WIDTH, height=HEIGHT)
screen.tracer(0)
screen.listen()
screen.onkeypress(up, "Up")

turtle = Turtle(shape="turtle")
turtle.setheading(90)
turtle.pu()
turtle.backward(270)
game_is_on = True
cars = []
level = 1
board = Scoreboard()
board.writescore()
while game_is_on:
    time.sleep(0.1)
    generate_car = random.randint(0, 4)
    if generate_car == 3:
        car = Car(random.choice(COLORS))
        cars.append(car)
        car.speed = 8
    screen.update()

    for c in cars:
        c.level = level
        c.move()
        if c.distance(turtle) < 30:
            if car.xcor()-turtle.xcor() < 15:
                game_is_on = False
                board.game_over()
            if turtle.xcor() - car.xcor() < 15:
                game_is_on = False
                board.game_over()
    if turtle.ycor() > 260:
        for i in cars:
            i.hideturtle()
            i.forward(1000)

        level += 1
        board.level += 1
        board.clear()
        board.writescore()
        turtle.goto(x=0, y=-270)

screen.exitonclick()
