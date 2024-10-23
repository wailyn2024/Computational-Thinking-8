import turtle
import random

#Set Backdrop
screen = turtle.Screen()
screen.bgcolor("black")

#Set Speed
t = turtle.Turtle()
t.speed(0)

#What To Draw
def draw_spiral():
    for i in range(100):
        t.color(random.random(), random.random(), random.random())
        t.circle(i * 2)
        t.right(91)

draw_spiral()

t.hideturtle()
turtle.exitonclick()
