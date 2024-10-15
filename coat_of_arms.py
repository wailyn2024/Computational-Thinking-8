###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("spring")


Thistle = codesters.Square(100, 100, 200, 'Thistle') 
Light_yellow = codesters.Square(100, 100, 200, 'LightYellow') 
White = codesters.Square(100, 100, 200, 'White') 
Indigo = codesters.Square(100, 100, 200, 'Indigo') 


Thistle1 = codesters.Sprite("cat", 100 , 100)
White2 = codesters.Sprite("cardinal", -100 , -100)
White2.set_size(0.5)
Light_yellow3 = codesters.Sprite("basketball", 100 , -100)
Light_yellow3.set_size(0.5)
Indigo4 = codesters.Sprite("soccerball", -100 , 100)
Indigo4.set_size(0.1)


message1 = codesters.Text('Braylen Brooks', 0,220, "Indigo")
message2 = codesters.Text('Sigma', 0,-220, "LightYellow")