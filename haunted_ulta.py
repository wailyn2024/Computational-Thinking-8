# Intro
print("You enter a scary ulta.")
print("The cash register beeps behind you.")
print("Will you be able to find the person who works there?")


# choice 1
c1 = input("Do you decide to look for a someone who works there or find the ELF power grip primer?")
if "ELF" in c1:
    print("You found one, do you steal it, (yes or no)?")
elif "yes" in c1:

    #A shelf falls down behind you!
    print("The police pop up out of nowhere and catch you! Game over...")
elif "Look for someone who works there" in c1:
    c3 = input("You find someone working there! They offer you a deal for a free sold out ELF power grip primer, do you except?")

    if "yes" in c3: 
        print( "Good choice, you won the game")
        c5 = input("What do you want for your prize, option 1 or 2!")
        if "1" in c5:
            print("Congrats you won a piece of gum!")
        else:
            print("you won bragging rights.")
            
            c6 = input("Would you like to try for another prize?")
        if "yes" in c6:
            print("Should've said no you lost your prize !")
        else:
            print("You get a piece of gum still.")

    #It's scary in here! 

    else:
        print("Game over it was a good deal!")
else: 
    print("Good choice,you won the game, close call!")

    #Game over now!
