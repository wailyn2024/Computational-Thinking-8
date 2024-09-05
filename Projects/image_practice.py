###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("space")
Sprite1 = codesters.Sprite("gJJFamQca86CibEeDmegk-1200-80.png")
Sprite1.say("Yummy apple!!")
Sprite2 = codesters.Sprite("apple", 0, -70) 
Sprite2.set_size(0.1)