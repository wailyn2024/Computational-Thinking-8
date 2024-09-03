###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("summer")
mySprite = codesters.Sprite("fish")
mySprite.say("Good job!")
mySprite2 = codesters.Sprite("basketball",-250,250)