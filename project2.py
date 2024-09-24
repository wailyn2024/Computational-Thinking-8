#intro
print("You walk past a scary cold field.")
print("something in the wind tells you to walk in farther.")
print("")
print("will you be able to make it through?")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# choice 1
c1 = input ("do you go to the [park] or [field]?")
if "park"in c1:
    print ("You slowly walk towards the park")

    # choice 2
    print ("You decide to go to the park.")
    c2 = input ("Do you go [left] or [right]?")
    if "left" in c2 or "right" in c2:
        print ("You walk left towards the right.")
    else:
        print ("You walk right towards the trees [walk past] or [look around].")

print ("you look around and a snake comes and bites your leg and you pass out")

print ("you walk past and get home nice and safely")
#choice 3

print ("You decide to go right towards the field")

print ("you ether [call your friend] or [go home]")
c3= input ("what do you do?")
if "call go home.:":
   print("you go home and are fine ")
elif "call your friend"in c3:

    print("you call your friend and get chased by dogs.")

else:
    print("you go home and are fine and have a good sleep.")