##################################
### SETUP ###
import codesters
from codesters import StageClass
stage=StageClass ()
#################################


stage.set_background("fall")


sprite1=codesters.Sprite("cardinal",100,0)
sprite1.say("Go SAAS!")


sprite2=codesters.Sprite("dog", -100,0)
sprite2.set_size(0.3)
sprite2.say("Go Dawgs!")