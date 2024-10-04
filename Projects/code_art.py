import turtle, random

# this is where it starts
t = turtle.Turtle()
t.penup()
t.speed(100)
t.goto(-100, -100)
t.color("cyan")
turtle.bgcolor("black")
t.pendown()

# now for some colors
t.begin_fill()
colors = ["white", "red"]
for i in range(200):
    t.forward(100 + i%5)
    t.color(colors[i%2])
    t.left(random.choice([72]) )
t.end_fill()
t.goto (-110 , -98)
for i in range(100):
    t.forward(100 + i)
    t.left(72)
    t.color = ["red"]
    
# the end
turtle.exitonclick()