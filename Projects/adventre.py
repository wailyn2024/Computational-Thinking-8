#intro
print("you walk into a basketball court.")
print("they start chanting your name.")
print("")
print("are you able to get playing time.")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")

# choice 1
c1 = input("do you take the [three] or the [dunk]?")
if "three" in c1:
    print("you make it")

else:
    print("you miss it")

# choice 2
print("you have a wide open pass to the left and a wide open to the right teammate.")
c2 = input("do you pass [left] or [right]?")
if "left" in c2 or "pass" in c2:
    print("you pass to the left")
else:
    print("you pass to the right")

# choice 3
print("in the game you can [shoot], [pass], or [drive]")
c3 = input("what do you do?")
if "shoot" in c3:
    print("you shoot it......")
elif "pass" in c3:
    print("you pass it......")
else:
    print("you dive in and dunk it on bruno ")

# choice 4
print("you get subbed off you can go to the bathroom, or sit on the bench")
c4 = input("do you go to the [bathroom] or [sit]")
if "bathroom" in c4:
    print("you go to the bathroom")
else:
    print("sit on the bench")

# choice 5
c5 = input("do you yell at [coach] or stay [quiet]")
if "yell" in c5:
    print("you get sat")

else:
    print("you get put back in")

# choice 6
c6 = input("do you take the game wining [shot] or [pass]")
if "shot" in c6:
    print("you make it")

else:
    print("they miss it")