import turtle, random, math
t= turtle.Turtle()
#speed
t.speed(100)
turtle.bgcolor("pink")
#colors
colors = ["Navy", "RoyalBlue"]
for i in range(20000):
    t.color(random.choice(colors))
    t.forward(150+i%15)
#shape
    t.left (120)

    
turtle.exitonclick()
