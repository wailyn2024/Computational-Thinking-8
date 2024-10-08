import turtle
import random

screen = turtle.Screen()
screen.bgcolor("black")

t = turtle.Turtle()
t.speed(0)

def draw_spiral():
    for i in range(100):
        t.color(random.random(), random.random(), random.random())
        t.circle(i * 2)
        t.right(91)

draw_spiral()

t.hideturtle()
turtle.exitonclick()
