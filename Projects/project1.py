###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("fall")
q1=codesters.Circle(0,0,200,'Purple')
q2=codesters.Square(-100,-50,125,'MediumBlue')
q2.turn_left(450)
q3=codesters.Square(100,-50,125, 'Lime')
q3.turn_right(450)
q4=codesters.Square(0,105,125,'Yellow')

s1=codesters.Sprite("soccerball.gif",0,105)
s1.set_size(1.75)
s2=codesters.Sprite("Globe.png",-100,-50)
s2.set_size(0.055)
s3=codesters.Sprite("image.png",100,-50)
s3.set_size(0.45)
s4=codesters.Sprite("Family4.png",0,0)
s4.set_size(0.3)
message1=codesters.Text("Just Wait",0,200,"Black")  
message2=codesters.Text("Kayson",0,-90,"Black")