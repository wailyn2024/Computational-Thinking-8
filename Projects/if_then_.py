###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################

while True:
    word=input("What do your think grandma likes?")

    if "d" in word and "i" in word and "v" in word and "t" in word:
        print(f"Grandma doesn't like {word}!")
    else:
        print(f"Grandma like {word}")

    print("")