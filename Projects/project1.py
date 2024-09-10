###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("fontaine")

q1 = codesters.Square(100, 100, 200, 'MidnightBlue')
q2 = codesters.Circle(-100, 100, 200, 'Indigo')
q3 = codesters.Circle(-100, -100, 200, 'Lavender')
q4 = codesters.Square(100, -100, 200, 'RoyalBlue')

s1 = codesters.Sprite("furina", 100, 100)
s1.set_size(0.3)
s2 = codesters.Sprite("softball", -100, -100)
s2.set_size(0.1)
s3 = codesters.Sprite("cool_dog", 100, -100)
s3.set_size(0.2)
s4 = codesters.Sprite("baking", -100, 100)
s4.set_size(0.2)

message1 = codesters.Text("Morgan Besse",0,220)
message2 = codesters.Text("Every journey has its final day.",0,-220)