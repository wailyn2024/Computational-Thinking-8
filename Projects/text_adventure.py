# Intro

print("You swim into the spooky abandoned shipwreck ")
print("Thousands of fish scurry out as you enter.")
print("")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")


# Choice 1

c1 = input("Do you choose to up to the [deck] or into the [rooms]")
if "deck" in c1:
    print("You carefully swim up to the deck.")
    # Choice 2
    print("The upstairs deck leads to a bathroom on the right and a control room on the left.")
    c2 = input("Do you go [left] or [right]?")
    if "left" in c2 or "control" in c2:
        print("You walk left to the control room.")
        # Choice 3
        print("In the basement, you can investigate the [wheel], [control board], or [rug].")
        c3 = input("WHat do you investigate?")
        if "wheel" in c3:
            print("You spin the wheel revealing a huge key......")
        elif "board" in c3:
            print("You investigate the board.")
            c5 = input("Do you move on or play with the board?")
            if "investigate" or "board" in c5:
                print("You slide the board away revevealing a picture")
            else:
                print("You  move on")
        else:
            print("You walk towards the rug.")
            c4 = input("Do you want to uncover the rug or move on")
            if "rug" or "uncover" in c4:
                print("You slide away the rug revealing a trap door")
                c6 = input("Do you want to investigate the trap door")
                if "yes" or "trap" or "investigate" in c6:
                    print("You open the trap door revialing a ominous basement")
                else:
                    print("You move on and leave")
            else:
                print("You move on and go back to shore.")
                print("Game over")
    else:
        print("You walk right to the bathroom.")
else:
    print("You decide to explore the rooms.")

