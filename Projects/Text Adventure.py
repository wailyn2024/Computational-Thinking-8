# intro
print("After years of work, you finally, come up with the potion that can turn anyone into a cat or a bunny with just one click of a botten ")
print("But before you can produce it, you have to test it on yourself")
print("")
print("you take a sip of it, and start seeing stars.")
print("Then you see words being spelled in front of you eyes.")

# choice 1
c1 = input ("Do you want to become [bunny] or a [cat]")
if "bunny" in c1:
    print ("You are now a small baby bunny")

    # choice 2
    print ("you are starting to get a little bit hungry.")
    c2 = input ("Do you want to eat [carrots] or [lettuce] or [cilantro]?")
    if "carrots" in c2 or "lettuce" in c2:
        print ("Yum! that was so good!")
    else:
        print("yuck! you find out you dont like cilantro ")



else:
    print(" nice! you turn into a baby kitten. Now you are a little tired")