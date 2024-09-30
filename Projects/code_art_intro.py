# ###############################################
# ### SETUP ###
import turtle
# ###############################################



#RED PENTAGON
t = turtle.Turtle()
t.penup()
t.goto(-100, -100)
t.color("red")
t.pendown()

t.right(10)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)
t.left(72)
t.forward(100)

#GREEN SQUARE
t = turtle.Turtle()
t.penup()
t.goto(100,100)
t.color("green")
t.pendown()

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

#GREEN RECTANGLE
t = turtle.Turtle()
t.penup()
t.goto(100,-100)
t.color("green")
t.pendown()

t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)

#GREEN STAR
t = turtle.Turtle()
t.penup()
t.goto(0,-100)
t.color("green")
t.pendown()

t.forward(100)
t.left(130)
t.forward(100)
t.right(90)
t.forward(100)
t.left(140)
t.forward(100)
t.right(45)
t.forward(100)
t.left(90)
t.forward(100)
t.right(45)
t.forward(100)
t.right(-140)
t.forward(100)
t.left(-90)
t.forward(100)
t.right(-130)
t.forward(220)

#CIRCLE AAAAAA
window = turtle.Screen()
t = turtle.Turtle()
t.penup()
t.goto(0,-100)
t.color("green")
t.pendown()

turtle.begin_fill()
turtle.circle(80)
turtle.end_fill()


t = turtle.Turtle()
t.penup()
t.goto(0,-100)
t.color("green")
t.pendown()
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)


# ###############################################
# ### ENDING ###
turtle.exitonclick()
# ###############################################
