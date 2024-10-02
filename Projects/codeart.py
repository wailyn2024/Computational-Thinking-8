import turtle, random

#Creating
t = turtle.Turtle()

#Moving
t.forward(random.choice([5,10,15,20]))
t.left(random.choice([15+1]))
t.speed(100)

# Colors
for i in range(100000):
    t.color(random.choice(["red","orange","yellow","green","cyan","blue","purple","pink"]))
    turtle.bgcolor("white")

    #Rotating shape
    t.forward(1+i/3)
    t.left(45+2)


turtle.exitonclick()