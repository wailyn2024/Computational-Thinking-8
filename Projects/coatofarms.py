###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("pony.jpg")

q1 = codesters.Square(100, 100, 200, 'pink')
q2 = codesters.Square(-100, 100, 200, 'white')
q3 = codesters.Square(-100, -100, 200, 'coral')
q4 = codesters.Square(100, -100, 200, 'yellow')

s1 = codesters.Sprite("les.webp" , 100, 100 )
s1.set_size(0.2)

s2 = codesters.Sprite("dance.jpeg" , -100, -100) 
s2.set_size(0.5)

s3 = codesters.Sprite("food.jpeg" , 100, -100) 
s3.set_size(0.5)

s4 = codesters.Sprite("ben.jpeg" , -100, 100) 
s4.set_size(0.5)

message1 = codesters.Text("Micki Nordstrom" ,0,220,"black")
message2 = codesters.Text("aAahhHh body BANG" ,0,-220, "black")

