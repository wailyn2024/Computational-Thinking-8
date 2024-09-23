# Intro
print("You are an kid and are exploring a old house at night.")
print("You walk in and see a something move in the darkness.")
print("You scream and it seems to echo infinitely.")
print("You continue forward.")
print("-----------------------")
print("2 doors appear in front of you.")
# choice 1
c1 = input("Do you go [downward] or [upward]? ")
if"downward" in c1:
    print("you venture deeper into the darkness...")
    # choice 2
    print("At the bottom of the path there are 2 doors.")
    c2 = input("Do you go [left] or [right]?")
    if "left" in c2:
        print("You open the left door.")
        print("A man locks the door on you and you get trapped.")
        print("You lose.")
    else:
        print("You go through the right door.")
        print("A man locks the door on you and you get trapped.")
        print("You lose.")





else:
    print("you carefully follow the stairs up.")
    # choice 3
    print("when you finally get to the top of the stairs theres a dusty bedroom and a dirty bathroom.")
    c3 = input("Do you go left or right?")
    if "left" in c3 or "bedroom" in c3:
        print("You enter the bedroom.")
        # choice 4
        print("the bedroom looks like it hasn't been touched in years.")
        c4 = input("Do you open the [closet], look under the [bed], or lift the [rug].")
        if "closet" in c4:
            print("You peer into the closet and a man grabs you...")
            print("You lose.")
        elif "bed" in c4:
            print("You look under the bed and a man grabs pulls you under with him.")
            print("You lose")
        else:
            print("You lift the rug and when you stand up the shadow of a man is behind you.") 
            print("You lose.")



    else:
        print("You enter the bathroom.")
        # choice 5
        c5 = input("Do you look in the [cabinet above the toilet] or [under the sink]?")
        if "cabinet" in c5 or "cabinet above the toilet" in c5:
            print("you open the cabinet and scream...")
            print("You lose.")
        else:
            print("You look under the sink and cry with tears of joy.")
            # choice 6 
            print("You find a ton of money in a old bag!")
            c6 = input("Do you take the money for [yourself] or give it to [charity]? ")
            if "yourself" in c6 or "myself" in c6:
                print("You win and have a become a billionaire!")
            else:
                print("You make a ton of sick kids happy, but you aren't.")
                print("You lose.")