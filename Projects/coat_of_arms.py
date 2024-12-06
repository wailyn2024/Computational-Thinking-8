###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background ("summer")

q1= codesters.Square (100,100,200,'white')
q2= codesters.Square (-100,100,200,'pink')
q3= codesters.Square (-100,-100,200, 'violet')
q4= codesters.Square (100,-100,200, 'blue')

s1= codesters.Sprite ("flower2",100,-100)
s2= codesters.Sprite ("",-100,-100)
