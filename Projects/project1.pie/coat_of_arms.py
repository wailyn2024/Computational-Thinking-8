###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("")

q1 = codesters.Square(100, 100, 200, 'LightPink')
q2 = codesters.Square(-100, 100, 200, 'MistyRose')
q3 = codesters.Square(-100, -100, 200, 'LightBlue')
q4 = codesters.Square(100, -100, 200, "MediumSeaGreen")

s1 = codesters.Sprite("BlackBelt_1", 100, 100)
s1.set_size(0.5)
s2 = codesters.Sprite("baking_1", -100, -100)
s2.set_size(0.2)
s3 = codesters.Sprite("Book_1", 100, -100) 
s3.set_size(0.3)
s4 = codesters.Sprite("bunny_3", -100, 100)
s4.set_size(0.2)

message1 = codesters.Text("Quinn Koester" ,0,220, "black")
message2 = codesters.Text("life's cool" ,0, -220, "black")