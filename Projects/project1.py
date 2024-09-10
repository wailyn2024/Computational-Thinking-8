###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("fall")


q1 = codesters.Square(100, 100, 200, 'salmon')
q2 = codesters.Square(-100, 100, 200, 'tomato')
q3 = codesters.Square(-100, -100, 200, 'crimson')
q4 = codesters.Square(100, -100, 200, 'white')


s1 = codesters.Sprite("softball", 100, 100)
s1.set_size(0.1)
s2 = codesters.Sprite("golden", -100, -100)
s2.set_size(0.1)
s3 = codesters.Sprite("music", 100, -100)
s3.set_size(0.2)
s4 = codesters.Sprite("seattle", -100, 100)
s4.set_size(0.6)

message1 = codesters.Text("Harper Grace Owens", 0,220,"white")
message2 = codesters.Text("live,laugh,love",0,-220,"white")