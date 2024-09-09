import codesters
from codesters import StageClass
stage = StageClass()


stage.set_background("winter")


q1 = codesters.Square(100, 100, 200, 'red')
q2 = codesters.Square(-100, 100, 200, 'Gold')
q3 = codesters.Square(-100, -100, 200, 'blue')
q4 = codesters.Square(100, -100, 200, 'orange')



s1 = codesters.Sprite("baseball", 100, 100)
s1.set_size(0.5)

s2 = codesters.Sprite("flowers", -100, -100)
s2.set_size(0.5)
s3 = codesters.Sprite("sodacan", 100, -100)
s3.set_size(0.5)
s4 = codesters.Sprite("bigapple", -100, 100)
s4.set_size(0.5)