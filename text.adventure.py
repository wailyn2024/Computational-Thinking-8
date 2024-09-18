#Intro
print("You walk into the dark quiet green forrest that your cat ran into, you get a shiver down your spine.")
print("You see a small house...")
print("A little girl peaks out at you from one of the windows")
print("Will ever you find your cat?")

#choice 1
c1 = input("Do you [knock] on the door and talk to the little girl or do you run away from the house and keep looking for your cat [elsewhere]?")
if "knock" in c1:
    print("You cautiously up to the door and knock 4 times")
    c2 = input("The little girl opens the door and asks what you want. Up close you can see her skin is very pale, and she is holding a needle and pouch. Do you ask her if she has seen your [cat] anywhere, or do you [ask] her about the needle and pouch?")
    if "cat" in c2:
        print("She says she hasn't seen any cats, but invites you inside her house for dinner.")
else:
    print(You hurry away from the creepy little house to a pond in the forrest)

