import codesters
from codesters import StageClass
stage = StageClass()

t = codesters.Sprite()
t.pen_up()
t.go_to(-100,-100)
t.pen_color("blue")
t.pen_down()

for i in range(6):
    t.forward(100)
    t.left(60)
    