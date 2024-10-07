import turtle, random, math

t = turtle.Turtle()


t.speed(100)

colors = ["pink","light coral","yellow"]
for i in range( 100000 ):
    turtle.bgcolor( "pink" )
    t.color ( "light coral" ) 
    t.color( "yellow" )
    t.forward( 400 )
    t.left( 72000 )

for i in range( 100000 ) :
    t.forward( 200 ) 
    t.left( 72+1 )
    t.left( 60 )
    t.right( 7200 )
    t.left (720000000)


t.penup()
t.pendown()
t.speed( 100 )


for i in range(100000) :
    t.left(23)
    t.forward (900)
    t.speed (100)
    









turtle.exitonclick() 