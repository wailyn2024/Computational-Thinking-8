###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background ("spring")

q1=codesters.Square(100,100,200,'Pink')
q2=codesters.Square(100,100,200,'MistyRose')
q3=codesters.Square(-100,-100,200,'Pink')
q4=codesters.Square(100,-100,200,'MistyRose')

s1=codesters.Sprite("Pink roses",100,100)
s1.set_size(0.1)
s2=codesters.Sprite("Thomas",-100,-100)
s2.set_size(0.1)
s3=codesters.Sprite("mountain", 100,-100)
s3.set_size(0.1)
s4=codesters.Sprite("disney",-100,100)
s4.set_size(0.1)


message1=codesters.Text("Hi! how are you?",0,220, "white")
message2=codesters.Text("Hi! I'm good.",0,-220, "white")