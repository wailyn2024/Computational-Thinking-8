###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################




while True:
    word =input("What do you think Grandma likes?")
    if "a" or "b" in word:
        print(f"Grandma loves {word}!")
    else:
        print(f"Grandma doesn't like {word}...")
