import turtle,random, math
t = turtle.Turtle()

t.speed(150)
turtle.bgcolor("red")


for i in range(100):
    t.color("blue")
    t.forward(50 + i)
    t.left(25)

turtle.exitonclick()