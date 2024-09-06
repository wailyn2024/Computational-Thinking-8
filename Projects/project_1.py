###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("rainstorm")
sprite1 = codesters.sprite("drums",100,100)
sprite2 = codesters.sprite("sailboat",100,-100)
sprite3 = codesters.sprite("rickenbacker-1-6",-100,100)
sprite4 = codesters.sprite("seattle",-100,-100)
square1 = codesters.Square("red",100,-100)
square2 = codesters.Square("purple",100,100) 
square3 = codesters.Square("white",-100,100)
square4 = codesters.Square("black",-100,-100)
