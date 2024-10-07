#start
import turtle 

t = turtle.Turtle()

turtle.bgcolor("pink")
t.speed(100)

colors = ["yellow","white","orange"]
angles = [50]
sides = [45, 78, 90]

for i in range(1000): 
    t.color( colors[i%3])
    t.forward(100 + 1 + i)
    t.left(45 + 1)

turtle.exitonclick()