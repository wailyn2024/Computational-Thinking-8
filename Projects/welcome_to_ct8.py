###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("winter")
mySprite = codesters.Sprite("dog")
mySprite.say("You didn't find me")

print("\n\nWhen you have found the CARDINAL, click here, then use CTRL C to end the program\n\n")
print("This is the new last instruction")
mySprite2 = codesters.Sprite("baseball",-250,250)