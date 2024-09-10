##############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
##############################################

stage.set_background ("white.jpeg")

q1 = codesters.Square (100, 100, 200, 'red')
q2 = codesters.Square (-100, 100, 200, 'blue')
q3 = codesters.Square ( -100, -100, 200, 'pink')
q4 = codesters.Square ( 100, -100, 200, 'green')

s1 = codesters.Sprite ("egypt.jpg", 100, 100)
s1.set_size(0.3)
s2 = codesters.Sprite ("dancer.jpg", -100, -100)
s2.set_size(0.2)
s3 = codesters.Sprite ("muslim.png", 100, -100)
s3.set_size(0.1)
s4 = codesters.Sprite ("peace.jpg", -100, 100)
s4.set_size(0.17)

message1 = codesters.Text ("hi!",0,220,"black")
message2 = codesters.Text (":)",0,-220,"black")