###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("winter")

q1=codesters.Square(100,100,200, 'lavender')
q2=codesters.Square(-100,100,200, 'blue')
q3=codesters.Square(-200,-200,-200, 'RosyBrown')
q4=codesters.Square(100,-100,200, 'MistyRose')

s1=codesters.Sprite("lake", 0.02)
s2=codesters.Sprite("music", 0.02)
s3=codesters.Sprite("cool_dog",0.02)
s3.set_size (0.23)                   

s4=codesters.Sprite("seattle", 0.02)

message1=codesters.Text("Blakely Kriegler",0,220,"Black")
message2=codesters.Text("Hi my name is Blakely",0,220,"Black")                   
