###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################


stage.set_background("rain")
sprite1 = codesters.Sprite("drum",100,100)
sprite1.set_size(0.5)
sprite2 = codesters.Sprite("sailboat",100,-100)
sprite2.set_size(0.5)
sprite3 = codesters.Sprite("bass",-100,100)
sprite3.set_size(0.5)
sprite4 = codesters.Sprite("soccer",-100,-100)
sprite4.set_size(0.5)
square1 = codesters.Square(100,-100,200, "red")
square2 = codesters.Square(100,100,200, "purple")
square3 = codesters.Square(-100,100,200,"white")
square4 = codesters.Square(-100,-100,200,"black")

message1 = codesters.Text("Jamari",0,220,"black")
message2 = codesters.Text("hello",0,-220,"red")