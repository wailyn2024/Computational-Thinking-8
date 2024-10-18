#start of code
import turtle, random
t = turtle.Turtle()

t.speed(100)
turtle.bgcolor("black")
colors= ["purple","crimson","red","blue"]
for i  in range(5000) :
    t.color(random.choice(colors))
    t.forward(8)
    t.left(random.choice([0,60,120,180,240,300]))

turtle.exitonclick()
# end of code

