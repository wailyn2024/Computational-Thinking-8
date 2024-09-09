########################
import codesters
from codesters import StageClass
stage = StageClass()
########################


stage.set_background("underwater")

q1 = codesters.Square(100,100,200, "green")
q2 = codesters.Square(-100,100,200,"green")
q3 = codesters.Square(-100,-100,200, "brown")
q4 = codesters.Square(100,-100,200,"black")


s1 = codesters.Sprite("bat",100,100)
s2 = codesters.Sprite("cardinal", -100,-100)
s3 = codesters.Sprite("guitar", 100, -100)
s3.set_size(0.25)
s4 = codesters.Sprite("fish", -100, 100)

message1 = codesters.Text("random message",0, 220,"green")
message2 = codesters.Text("blah blah blah",0,-220,"black")