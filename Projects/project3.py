import turtle, random, math
t = turtle.Turtle()
#speed (300)
t.goto(100, 50)
t.color("pink")
#colors
colors = ["black","purple","pink","yellow","red"]
for i in range(10000):
#shape
    t.color (random.choice(colors))
    t.forward(100+i%50)
    t.right (45)
    t.left (10)
turtle.exitonclick() 
#i have so much colors in my shape 