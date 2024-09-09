###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("fall")
q1 = codesters.Square(100,100,200,"snow")
q2 = codesters.Square(-100,100,200,"PaleGreen")
q3 = codesters.Square(-100,-100,200,"snow")
q4 = codesters.Square(100,-100,200,"LightSkyBlue")

s1 = codesters.Sprite("bookcustom",100,100)
s1.set_size(0.3)
s2 = codesters.Sprite("dogcustom",-100,-100)
s2.set_size(0.3)
s3 = codesters.Sprite("runningcustom",100,-100)
s3.set_size(0.3)
s4 = codesters.Sprite("mugcustom",-100,100)
s4.set_size(0.3)

message1 = codesters.Text("Zoe Michel Smith",0,220,"black")
message2 = codesters.Text("Have fun! Make friends!",0,-220, "black")