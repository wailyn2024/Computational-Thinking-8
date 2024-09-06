###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("mountain")
quart1 = codesters.Square(100, 100, 200,'DarkOrchid')
quart2 = codesters.Square(-100, 100, 200,'Goldenrod')
quart3 = codesters.Triangle(100, -100, 200,'LightCoral')
quart4 = codesters.Triangle(-100, -100, 200,'SeaGreen')
quart4.turn_right(45)
message1 = codesters.Text("Divit J Gupta",0,220,"Black")
message1.set_size(4.5)
message2 = codesters.Text("I like my coffee Black :))",0,220,"Gold")