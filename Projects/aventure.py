   # choice 1
   # you get to a taylor swift concert
c1 = input ("Do you go up into the stadium or into the merchandise stand? ")
if "stadium" in c1:
    print("You walk into the stadium")

    # choice 2
    print ("The opener is playing in the stadium do you turn left and watch her or turn right.") 
    c2= input ("Do you go [left] or [right]")
    if "left" in c2 or "opener" in c2:
        print("You walk left towards your seats.")
    else:
        print("You walk right and get food.")
    # The openers are sabrina carpenter and gracie abrams
    # choice 3 
    if "left" in c2:
        print ("you watch the opener and cheer while waiting.")
    else:
        print ("you eat your food and dont watch the first opener.")
    # either way you watch opener number two
    # choice 4 
    print ("Just as taylor is about to start you hear a noise")
    c4 = input ("Do you go [left] and investigate or [stay] where you are?")
    if "left" in c4:
        print("You walk towards the noise and hear a howl")
    else:
        print("you go anyways and hear a howl")
    
    # choice 5
    print ("you go to the noise and see a puppy")
    c5 = input ("do you run away, grab the puppy, or leave?")
    if "run away" in c5:
        print("You run back to your seats")
    elif "grab" in c5:
        print("you run back to your seats and hold him there")
    else:
        print ("you cant give up good taylor swift tickets so you go back")
    
    # choice 6
    print ("when you get back to your seats she starts")
    c6 = input ("after the show do you get dinner or go to your hotel?")
    if "dinner":
        print("You eat good food the end.")
    else:
        print("you go to sleep and enjoyed the show the end.")

    