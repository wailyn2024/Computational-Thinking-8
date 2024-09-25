# intro

print("      ")
print("Tomorrow is halloween, and you have still not chosen a costume")
print("You have to figure out what you will dress up as before its too late!")
print("You were going to wear your old dinosaur costume but you're not sure anymore.")
print("-----------------------------------------------------------------------------")
print("You go online and start looking at different costumes. But there are so many to choose!")

#c1
c1 = input("Do you want to dress up as a[dinosaur] or something [scary?]")
if "scary" in c1:
    print("You have chosen to find a scary costume!")

    #c2
    print("You found costumes online that will be delivered later today. Perfect! There are so many to choose from.")
    c2 = input("Choose between the creepy [clown] or [zombie].")
    if "clown" in c2:
        print("You have chosen to be a creepy clown for Halloween!")
    else:
        print("You have chosen to be a zombie for halloween!")
    print("You hear your doorbell ring and run to grab your package. You then open it and pull out your new costume!")

else:
    print("You have decided to wear your old dinosaur costume!")
print("      ")
print("- A few hours later -")
print("You put on your costume and grab your bag for candy.")
print("Your goal is twenty pieces of candy by the end of the day.")
print("You leave the house and walk outside to see all the kids of your neighborhood in their costumes, running around with their candy.")
print("What house should you stop at first? Maybe the big blue house with the giant candy bars? Or the decorated haunted house with a cauldron full of candy?")

#c3
c3 = input("Do you walk up to the [blue] house or the [haunted] house?")
if "blue" in c3:
        print("You walk up to the blue house and ring the doorbell.")
        print("The door opens and a smiling lady dressed as a witch compliments your costume. She hold out a bag of candy and tells you to take as many as you want. You grab five jolly ranchers and thank her.")
else:
        print("You walk up to the decorated haunted house and ring their doorbell.The door creaks open and two hand hold out a cauldron full of candies. A shrill voice says 'take fiveeeee.' You laugh, take the candy, and walk back to the street.")    
#c4
print("You walk down the road and see a pile of scattered candy on the ground. Someone must have dropped it!")
c4 = input("Do you [leave] it, [return] it, or [take] it for yourself?")
if "leave" in c4:
     print:("You are not greedy! And as a reward, three pieces of candy fall from the sky. You now have 8 pieces of candy!")

elif "return" in c4:
     print("You find the owner of the candy and they are so grateful that they let you have it! You now whohave 11 pieces of candy!")

else: 
     print("You eat the candy but it was expired. You feel sick now:(")

#c5
c5 = input(" You keep walking and see more houses. Do you walk up to the [mansion] or the [boring] house?")
if "mansion" in c3:
    print("You walk up to the mansion and ring the 24k gold doorbell.")
    print("The door opens and an old man opens the door and throws candy at you. You pick up the 3 pieces and run off.")
else:
    print("You walk up to the boring haunted house and knock. The door opens and a smiling lady hands you 3 boxes of candied raisins.")

#c6
c6 = input ("There is one house left. You walk up to it and the door opens. A little kid stands at the dorr and says 'take one!' Do you take [one] or do run off with the [whole bucket]?")
if "one" in c3:
     print("    ")
     print("You take on piece and return home. You did not get 20 pieces of candy but you had a fun time.")
else:
    print("    ")
    print("You return home with your bucket and the kid's bucket of candy. You feel guilty but now you have so much candy!")

    #