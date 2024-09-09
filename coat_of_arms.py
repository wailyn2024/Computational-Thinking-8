###############################################
### SETUP ###
import codesters
from codesters import StageClass
import codesters.shapes
stage = StageClass()
###############################################


stage.set_background(spring)



Thistle = codesters.Square(100, 100, 200, 'Thistle') 
Light_yellow = codesters.Square(100, 100, 200, 'LightYellow') 
White = codesters.Square(100, 100, 200, 'White') 
Indigo = codesters.Square(100, 100, 200, 'Indigo') 


Thistle1 = codesters.sprite("cat", 100 , 100)

White2 = codesters.sprite("Images/1306f3a700771ca5e99ed55dd5df6a51.jpg", -100 , -100)
White2.set_size(0.5)

Light_yellow3 = codesters.sprite("basketball", 100 , -100)
Light_yellow3.set_size(0.5)

Indigo4 = codesters.sprite("soccerball", -100 , 100)
Indigo4.set_size(0.1)


message1 = codesters.text('this is my name', 0,220, "Indigo")
message2 = codesters.text('this is my message', 0,-220, "LightYellow")