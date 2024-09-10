###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background ("peace.jpg")

q1 = codesters.Square (100, 100, 200, 'blue')
q2 = codesters.Square (-100, 100, 200, 'pink')
q3 = codesters.Square ( -100, -100, 200, 'yellow')
q4 = codesters.Square ( 100, -100, 200, 'green')

s1 = codesters.Sprite ("egypt.jpg")
s2 = codesters.Sprite ("dancer.jpg")
s4 = codesters.Sprite ()

