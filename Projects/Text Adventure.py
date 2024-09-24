# intro
print("After years of work, you finally come up with the potion that can turn anyone into a cat or a bunny with just one click of a botten ")
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
    if "carrots" in c2:
        print ("Yum! that was so good!")
    elif "lettuce" in c2:
        ("Yumm you love lettuce!")
    else:
        print("yuck! you find out you dont like cilantro ")



else:
    print(" nice! you turn into a baby kitten. Now you are a little tired")

    c1 = input ("Do you want to fall asleep in a [meadow] or a [tree] or a [Bush]")
    if "tree" in c1:
        print ("Ouch! you fell out and hurt you paw!")
        print ("Now you are stuck and dont know what to do.")
        print ("There is something running in the distance, do you try and [hobble over] to it or [stay put]?")
        if "stay put" in c1:
            print("unfortunately you die because you were not able to make yourself go through the pain and try and find food.")
        else: 
            print ("The thing you saw was a human and gave you food to help you heal more quickly!")
            print ("you were able to heal quickly and and keep thriving!")
        
    else:
        print ("Hah,You woke up feeling well rested!")
        # choice 3
        c1 = input ("There is something running in the distance, do you try and [hobble over] to it or [stay put]?")
        if "stay put" in c1:
            print("unfortunately you die because you were not able to find food fast enough.")
        else: 
            print ("The thing you saw was a human and gave you food to help you heal more quickly!")
            print ("you were able to heal quickly and and keep thriving!")
        print ( "did you enjoy this experience of being an animal [yes] or [no]"?)
               
        if "yes" in c3
        print ("Now you get to mass produce the potion!")
        else:
            print ("womp womp")
        
       