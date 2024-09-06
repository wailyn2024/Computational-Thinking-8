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


print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")
print(" this is the last instruction")
mySprite2 = codesters.Sprite("baseball",-250,250)