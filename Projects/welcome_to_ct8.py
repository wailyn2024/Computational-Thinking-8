###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("park")
mySprite = codesters.Sprite("fox")
mySprite.say("I like pancakes!")
mySprite.set_size(1.5)


mySprite2 = codesters.Sprite("baseball",-250,250)