###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("mountain")

sprite1 = codesters.Sprite("Rat",100,0)
sprite1.set_size(0.3)
sprite1.say("H1 Im l0st!")

sprite2 = codesters.Sprite("cardinal",-100,0)
sprite2.say("Im also l0sT")