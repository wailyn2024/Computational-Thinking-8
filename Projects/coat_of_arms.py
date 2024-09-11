###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("fall3")

q1 = codesters.Square(100,100,200,'Black') 
q2 = codesters.Square(-100,100,200,'LightGray') 
q3 = codesters.Square(-100,-100,200,'Silver') 
q4 = codesters.Square(100,-100,200,'Gray') 

S1 = codesters.Sprite("paw2",100,100)
S2 = codesters.Sprite("basketball3",-100,-100)
