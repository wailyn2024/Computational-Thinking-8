########################
import codesters
from codesters import StageClass
stage = StageClass()
########################


stage.set_background("forest")

q1 = codesters.Square(100,100,200, "green")
q2 = codesters.Square(-100,100,200,"grey")
q3 = codesters.Square(-100,-100,200, "beige")
q4 = codesters.Square(100,-100,200,"black")
q5 = codesters.TriangleRight(100,100,200,200,"orange")


s1 = codesters.Sprite("toucan",100,100)
s1.set_size(.2)
s2 = codesters.Sprite("cat2", -100,-100)
s3 = codesters.Sprite("guitar", 100, -100)
s3.set_size(0.18)
s4 = codesters.Sprite("book", -100, 100)
s4.set_size(.35)

message1 = codesters.Text("Liam Kudo-King",0, 220,"white")
message2 = codesters.Text("blah blah blah",0,-220,"white")