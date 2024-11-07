# intro
print("welcome to 'zombie apocalypse'")
print("you wake up in a world overrun by zombies. Your goal is to survive.")
print("you will face decisions that will determine if you live or not.")


# First decision: Choose a starting location
print("/nYou are in a deserted city. Where do you want to go?")
print("1. search the nearby supermarket for supplies")
print("2. head to the police station for weapons")
print("3. look for other survivors in the park")
print("4. stay in your home")
print("5. use your phone and contact everyone you know to see if any survived")

choice1 = input("Enter your choice (1, 2, 3, 4, or 5): ")

if choice1 == "1":
        print("/nYou enter the supermarket. It's dark and silent...")
        print("suddenly, a zombie appears! Do you:")
        print("1. Fight it off with a can.")
        print("2. Run for the exit.")

        choice2 = input("enter your choice (1 or 2): ")
        if choice2 == "1":
                print("/nYou manage to knock the zombie out, but you sustained an injury. You take some supplies before leaving.")
        elif choice2 == "2":
            print("/nYou sprinted out, but the zombie chased you. You barely escape but lose some supplies.")
        else:
               print("Invalid choice!")

elif choice1 == "2":
        print("/nYou make your way to the police station. It's flooded with zombies!")
        print("Do you:")
        print("1. try to sneak in through the back.")
        print("2. create a distraction to lure them away.")

        choice2 = input("enter your choice (1 or 2): ")
        if  choice2 == "1":
            print("/nYou successfully sneak inside and find a stash of weapons!")
        elif choice2 == "2":
              print("/nYour distraction works, but you still have to find your way inside.")
        else:
              print("Invalid choice!")

elif choice1 == "3":
        print("/nIn the park, you spot a few other survivors. Do you:")
        print("1. approach and try to team up.")
        print("2. keep your distance for safety.")

        choice2 = input("Enter your choice (1 or 2): ")
        if choice2 == "1":
              print("/nYou successfully form a small group! Together, You're stronger. ")
        elif choice2 == "2":
              print("/nYou survived. But you're now alone. Trust is hard to come by.")
        else:
              print("invalid choice!")
              
elif choice1 == "4":
        print("/nIn your home, you hear something outside your door:")
        print("1. climb out the window incase it's zombies.")
        print("2. open the dor incase it's survivors.")

        choice2 = input("Enter your choice (1 or 2): ")
        if choice2 == "1":
              print("/nYou escaped the zombies outside your door. ")
        elif choice2 == "2":
              print("/nYou were caught by the zombies. game over.")
        else:
              print("invalid choice!")

elif choice1 == "5":
        print("/nYou call everyone in your contacts, and someone answers:")
        print("1. go to find them.")
        print("2. stay put and communicate a plan.")

        choice2 = input("Enter your choice (1 or 2): ")
        if choice2 == "1":
              print("/nYou didn't have a plan and got caught. game over")
        elif choice2 == "2":
              print("/nYou came up with a successful plan and lived.")
        else:
              print("invalid choice!")
else:
       print("Invalid choice! you were spotted by zombies, and it was game over.")

# conclusion
print("/nThank you for playing!")
