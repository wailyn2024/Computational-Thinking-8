import turtle

t = turtle.Turtle()

t.goto (100,0)
t.color ("cyan")
#Moving Forward & Left
for i in range (170):
    t.forward (150)
    t.left (115+1)


#Color
t.color("green")

#Rotating shapes
for i in range (171):
    t.forward (151)
    t.left(216 + 1)



turtle.exitonclick ()