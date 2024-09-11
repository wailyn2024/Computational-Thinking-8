##############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
##############################################


stage.set_background("gymnasium-2")
B1 = codesters.Sprite("Basketball", 150, -150)
B1.set_size(.17)
SN1 = codesters.Sprite("Space Needle", -150, -150)
SN1.set_size(.18)
IC1 = codesters.Sprite("IceCastle", 150, 150)
IC1.set_size(.30)
BB1 = codesters.Sprite("BlueBoy", -150, 150)
BB1.set_size(.20)
B1.say("Hi I'm Mikhail!")