###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")


s1 = codesters.Square(100, 100, 200, 'forestgreen')
s2 = codesters.Square(-100, 100, 200, 'mediumturquoise')
s3 = codesters.Square(-100, -100, 200, 'limegreen')
s4 = codesters.Square(100, -100, 200, 'deepskyblue')


sp1 = codesters.Sprite("tree", 100, 100)
sp1.set_size(0.8)
sp2 = codesters.Sprite("fishingrod", -100, 100)
sp2.set_size(0.2)
sp3 = codesters.Sprite("sailboat", 100, -100)
sp4 = codesters.Sprite("sportsballs", -100, -100)
sp4.set_size(0.8)


message1 = codesters.Text("Lachlan Forrest",0,220,"black")
message2 = codesters.Text("Eat your frog",0,-220)