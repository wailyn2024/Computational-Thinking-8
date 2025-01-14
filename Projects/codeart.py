import turtle 

t= turtle.Turtle()

t.goto(100,0)
colors= ["pink,yellow"]
t.color ( colors[i % 2])
t.color("cyan")

for i in range(5):

    t.forward(100)
    t.left(72)

turtle.exitonclick()