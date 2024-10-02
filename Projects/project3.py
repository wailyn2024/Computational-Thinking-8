import turtle, random, math

t = turtle.Turtle()

t.goto(100, 0)

color = ["black", "cyan", "green"]
for i in range(5000):
    t.color(color[i%3])
    t.forward(150)
    t.left(100)

#This shape is a circle
#This shape is getting traced around by different colors and shapes and the shapes look like triangles
#The colors that this shape is getting traced by is black, green, and cyan 
           
turtle.exitonclick()