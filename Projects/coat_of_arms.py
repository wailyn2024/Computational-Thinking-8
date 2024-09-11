###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("winter")

square1 = codesters.Square(100,100,200,'Blue')
square2 = codesters.Square(-100,100,200, 'Red')
square3 = codesters.Square(-100,-100,200,'black')
square4 = codesters.Square(100,-100,200,'white')

ski = codesters.Sprite("skis",-100,100)
ski.set_size(0.7)
soccerball = codesters.Sprite("soccerball",100,100)
bat = codesters.Sprite("image",100,-100)
bat.set_size(0.5)
dog = codesters.Sprite("dog",-100,-100)
dog.set_size(0.1)


message1 = codesters.Text("Aadit Purohit",0,220,"red")
message2 = codesters.Text("Soccer, Cricket, Dog, Ski", 0,-220, "red")