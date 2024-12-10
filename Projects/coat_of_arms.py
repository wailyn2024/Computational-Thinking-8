###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background ("summer")

q1= codesters.Square (100,100,200,'white')
q2= codesters.Square (-100,100,200,'pink')
q3= codesters.Square (-100,-100,200, 'violet')
q4= codesters.Square (100,-100,200, 'blue')

s1= codesters.Sprite ("skimask",100,-100)
s1.set_size(0.1)
s2= codesters.Sprite ("Christmas",100,100)
s2.set_size(0.5)
s3= codesters.Sprite ("sushi",-100,-100)
s3.set_size(0.3)
s4= codesters.Sprite ("volleyball",-100,100)
s4.set_size(0.1)
message1= codesters.Text("Wailyn Chen",0,220,"black")
message2= codesters.Text("These are some of my favorite things",0,-220,"black")


