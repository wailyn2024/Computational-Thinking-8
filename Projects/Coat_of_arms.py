###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("City")

quart1 = codesters.Square(100, 100, 200,'DarkOrchid')
quart2 = codesters.Square(-100, 100, 200,'Goldenrod')
quart3 = codesters.Triangle(100, -59, 200,'LightCoral')
quart4 = codesters.Triangle(-100, -59, 200,'SeaGreen')
quart5 = codesters.Triangle(0, -119, 200,'Navy')

quart4.turn_right(60)
quart3.turn_right(-60)

message1 = codesters.Text("Divit J Gupta",0,220,"Black")
message1.set_size(4.5)
message2 = codesters.Text("90% of the time I want to sleep",0,-220,"Gold")

S1 = codesters.Sprite("rabbit", 100, 100,)
S1.set_size(.3)
S2 = codesters.Sprite("Valorant", -100, 100)
S2.set_size(0.3)
S3 = codesters.Sprite("sleep", 100,-75)
S3.set_size(.5)
S4 = codesters.Sprite("book", -100, -75,)
S4.set_size(0.15)