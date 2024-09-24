# choice 1 
c1 = input("Do you go up the [park] or into the [movies]")
if "park" in c1:
    print("You go to the park")

    # choice 2 
    print("The park has a [swing] to the left and a [slide] to the right.")
    c2 = input("Do you go [left] or [right]?")
    if "left" in c2 or "swing" in c2:
        print("You walk left towards the swing.")
    # choice 3 
        print("The swings are full but there is an [ice cream shop] and a [cafe]")
        c3 = input("Do you go [left] or [right]?")
        if "left" in c3 or "ice cream shop" in c3:
            print("You walk left towards the ice cream shop.")
        else:
            print("You walk right towards the cafe.")

    else:
        print("You walk right towards the slide.")
    # choice 4
    print("You slide down the slide and it burns you because it's sunny out.")


else:
    print("You decide to go into the movies, you can watch [Moana 2], [Tangled 2], or [Frozen III]")
    c4 = input("What movie do you decide to see?")
    if "Moana" in c4:
        print("You go buy a ticket")
    elif "Tangled" in c4:
        print("You go buy a ticket")
    else:
        print("You go buy a ticket")
    # choice 5
    print("After you buy the ticket you go to buy snacks and your stuck between two, [popcorn] or [gummy bears]")
    c5 = input("Do you choose [popcorn] or [gummy bears].")
    if "gummy bears" in c5:
        print("You choose gummy bears.")
    else:
        print("You choose the popcorn.")
    # choice 6
    print("Now your in the theater and can either sit in the [back] or the [front] of the theater.")
    c6 = input("Do you go in the [back] or the [front]?")
    if "back" in c6:
        print("You sit in the back.")
    else:
        print("You choose to sit in the front.")
    


