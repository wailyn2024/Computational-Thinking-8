###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("park")

q1 = codesters.Square(100, 100, 200, 'blue')
q2 = codesters.Square(-100, 100, 200, 'yellow')
q3 = codesters.Square(-100, -100, 200, 'red')
q4 = codesters.Square(100, -100, 200, 'green')

s1 = codesters.Sprite("DND", 100, 100)
s1.set_size(0.4)
s2 = codesters.Sprite("Drift", -100, -100)
s2.set_size(0.3)
s3 = codesters.Sprite("family", 100, -100)
s3.set_size(0.6)
s4 = codesters.Sprite("cardinal", -100, 100)
s2.set_size(0.1)

message1 = codesters.Text("Im neel", 0, 220, "red")
message1 = codesters.Text("Hello!", 0, -220, "blue")