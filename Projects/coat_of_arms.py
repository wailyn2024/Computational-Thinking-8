###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

stage.set_background("basketballcourt25")


sq1 = codesters.Square(100, 100, 200, 'red')
sq2 = codesters.Square(-100, 100, 200, 'pink')
sq3 = codesters.Square(-100, -100, 200, 'gold')
sq4 = codesters.Square(100, -100, 200, 'blue')


basketball = codesters.Sprite("basketball", 100, 100, 200)
spotify = codesters.Sprite("spotify",-100, 100, 200)
taiwan = codesters.Sprite("taiwan", -100, -100, 200)
saas = codesters.Sprite("cardinal", 100, -100, 200)