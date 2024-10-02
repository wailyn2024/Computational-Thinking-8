#start
import turtle,random, math

t=turtle.Turtle()

#color settings
t.goto(100,0)
t.color("pink")
colors=["blue","orange","cyan"] 

#shape
for i in range (300):
    t.forward (150 + 5*i)
    t.left(120)
    t.color(colors[i%3])
    
#end
turtle.exitonclick()