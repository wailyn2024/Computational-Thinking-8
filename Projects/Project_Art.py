import turtle, random
t = turtle.Turtle()
t.penup()
t.goto(0,0)
t.pendown()
colors = ["orchid","teal","indian red","wheat"]
for i in range(10000):
    t.color(random.choice(colors))
    t.speed(100)
    t.forward(100+1)
    t.left(150+i)
turtle.exitonclick
    

