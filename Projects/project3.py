import turtle, random, math
t= turtle.Turtle()

t.speed(50)
turtle.bgcolor("pink")

colors = ["light yellow" , "dark salmon"]
for i in range (2000):
    t.color(random.choice(colors))
    t.forward (100 + i%50)
    t.left(random.choice([90,95,92]))



