###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("testtesttest")
mySprite = codesters.Sprite("duckyyyy",-100,0)
mySprite.say("hello!")
mySprite.set_size(0.3)

mySprite2 = codesters.Sprite("frogggg", 100,0)
mySprite2.say("hello!")
mySprite2.set_size(0.3)