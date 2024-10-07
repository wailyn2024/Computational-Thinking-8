#start
import turtle

t = turtle.Turtle()

t.goto(100,0)
t.color("cyan")

#change colors
colors = ["pink", "cyan", "gray"]



for i in range(900):
    turtle.forward(100+i)
    turtle.left(91)


    
#End
turtle.exitonclick()