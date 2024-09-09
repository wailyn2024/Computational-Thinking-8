###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")

q1 = codesters.Square(100,100,200, 'black')
q2 = codesters.Square(-100,100,200,'white')
q3 = codesters.Square(-100,-100,200,'red')
q4 = codesters.Square(100,-100,200,'blue')

s1 = codesters.Sprite("bball",100,100)
s1.set_size(0.1)

s2 = codesters.Sprite("cardinal",-100,-100)
s2.set_size(0.5)

s3 = codesters.Sprite("fam",100,-100)
s3.set_size(0.1)

s4 = codesters.Sprite("gaming",-100,100)
s4.set_size(0.1)