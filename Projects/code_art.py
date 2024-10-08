import turtle
#Code_starts
t = turtle.Turtle()

t.goto(100, 0)
t.color("blue")
#Color_is_blue 
for i in range(500):
    t.forward(100+i)
    t.left(72)
#Code_over_now
turtle.exitonclick()
