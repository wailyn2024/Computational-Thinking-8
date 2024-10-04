###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
stage.set_background("fall")

q1=codesters.Square(100, 100, 200, 'pink')
s1= codesters.Sprite ("cardinal" ,100,100)
s2=codesters.Sprite("cat",-100,-100)
s2.set_size(0.5)
message1= codesters.Text("hi",0,220,"light blue")
message2= codesters.Text("hello" ,0,-220,"blue")
s3= codesters.Sprite ("tom" ,150,-150) 
s3.set_size(0.03)