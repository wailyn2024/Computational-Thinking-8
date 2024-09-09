###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")


s1 = codesters.Square(100, 100, 200, 'darkgreen')
s2 = codesters.Square(-100, 100, 200, 'mediumturquoise')
s3 = codesters.Square(-100, -100, 200, 'limegreen')
s4 = codesters.Square(100, -100, 200, 'mediumblue')


sp1 = codesters.Sprite("pinetree", 100, 100)
sp2 = codesters.Sprite("fishingrod", -100, 100)