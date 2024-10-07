###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

t = codesters.Sprite()


t.set_speed(100)
t.pen_down()

colors = ["pink","light coral","yellow"]
for i in range( 100 ):
    t.set_color ( "light coral" ) 
    t.set_color( "yellow" )
    t.forward( 40 )
    t.set_heading( i*72 )

for i in range( 100 ) :
    t.forward( 20 ) 
    
    t.set_heading( i*60 )



for i in range(100) :
    
    t.set_heading( i*23 )
    t.forward (90)
 
    







