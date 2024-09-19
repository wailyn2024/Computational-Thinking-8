# intro

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
    print("You found costumes that will be delivered later today. Perfect! There are so many to choose from.")
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
print("You have made a list of the candies that you want to have by the end of trick-or-treating.")
print("Your list is: 8 KitKats, 3 packs of M&Ms, 4 packs of skittles, 8 lollipops, and one Twix.")
print("You leave the house and walk outside to see all the kids of your neighborhood in their costumes, running around with their candy.")
print("What house should you stop at first? Maybe the big blue house with the giant candy bars? Or the decorated haunted house with a cauldron full of candy?")

#c3
c3 = input("Do you walk up to the [blue] house or the [haunted] house?")
