##############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
##############################################


stage.set_background("winter")

q1 = codesters.Square(100, 100, 200, 'black')
q2 = codesters.Square(-100, 100, 200, 'gold')
q3 = codesters.Square(-100, -100, 200, 'red')
q4 = codesters.Square(100, -100, 200, 'pink')

s1 = codesters.Sprite("wilson basketball", 100, 100)
s1.set_size(0.2)

s2 = codesters.Sprite("xbox controller", -100, -100)
s2.set_size(0.2)

s3 = codesters.Sprite("watermelon", 100, -100)
s3.set_size(0.4)

s4 = codesters.Sprite("skiing", -100, 100)
s4.set_size(0.3)

message1 = codesters.Text("kai",0,220,"yellow" )
message2 = codesters.Text("i love number 34",0,-220, "teal")