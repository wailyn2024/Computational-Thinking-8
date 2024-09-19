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
        else:
            print("You walk towards the rug.")
    else:
        print("You walk right to the bathroom.")
else:
    print("You decide to explore the rooms.")

