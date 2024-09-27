###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################



stage.set_background("fall")

q1 = codesters.Square(100, 100, 200, 'pink')
q2 = codesters.Square(-100, 100, 200, 'blue')
q3 = codesters.Square(-100,-100, 200, 'green')
q4 = codesters.Square(100,-100,200,'red' )

s1 = codesters.Sprite("cardinal", 100, 100)
s2 = codesters.Sprite ("basketball", -100, -100)
s2.set_size (0.5)
s3 = codesters.Sprite("corgi", 100, -100)
s3.set_size (0.5)
s4 = codesters.Sprite("flower2", -100, 100)
s4.set_size (0.5)

message1 = codesters.Text("tabitha madden",0,220,"red")
message2 = codesters.Text("have a good day",0, -220,"black")