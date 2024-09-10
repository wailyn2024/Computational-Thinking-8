###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("underwater")

q1 = codesters.Square(100, 100, 200, 'navy')
q2 = codesters.Square(-100, 100, 200, 'RoyalBlue')
q3 = codesters.Square(-100, -100, 200, 'LightSkyBlue')
q4 = codesters.Square(100, -100, 200, 'DeepSkyBlue')


s1 = codesters.Sprite("jumpingspooder", 100, 100)
s2 = codesters.Sprite("thomas", -100, -100)
s2.set_size(0.5)
s3 = codesters.Sprite("drpepper" 100, -100)
s3.set_size(0.5)
s4 = codesters.Sprite("cardinal", -100, 100)
s4.set_size(0.1)

message1 = codesters.Text("I love dr. pepper!", 0, 220, "navy")