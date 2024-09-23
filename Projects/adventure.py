###############################################
### SETUP ###
import codesters
from codesters import StageClass
stage = StageClass()
###############################################
#Intro
print("You enter the remote haunted house after walking for days in the cold rain.")
print("     ")
print("Do you dare to explore?")
print("     ")
name = input("What is your name?")
message1 = codesters.Text(f"Congratulations! {name}",0,220,"red")
stage.set_background("winter")
#Choice1(entering-house)
c1 = input("Do you choose to go into the [small house] or [mansion] or [barn]? ")
if "small house" in c1:
    print("************************")
    print("You walk around the premises and enter the small house and are locked in the house!  ")
    print("************************")
    print("You see a television set from the 1980's and read.....")
    print(".......")
    print("THE END!")
elif "mansion" in c1:
    print("************************")
    print("You walk straight ahead and enter into the mansion")
    print("************************")
#choice2
    c2 = input("You enter the mansion and see a trapdoor. Do you go through downstairs to the [trapdoor]  or [straight]? ")
    if "trapdoor" or "downstairs" in c2:
        print("You survived the trick!")
    #choice4
        c4 = input("Do you choose to [exit] and maybe die or [stay and fight]? ")
        if "stay" or "fight" in c4:
            print("Great Job! You are on your way out!")
            #choice5
            c5 = input("Do you choose to [Climb Roof] or [Go Sleep]? ")
            if "climb roof " or "roof" or "climb" in c5:
                print("You climb the Roof and Create a Smoke Signal and are on your way to win!")
                #choice6
                c6 = input("Are you a [Sigma] or [Beta]? ")
                if "Sigma" or "sigma" in c6:
                    print("You win, Open the Port to see your win screen!")
                else:
                    print("You Lose!")
            else:
                print("You lost! Game Over!")
        else:
            print("You chicken! GET OUT!")
            print("The End")
    else:
        print("You died! Adventure Over")
else:
    #choice3
    c3 = input("You enter the barn but it's black and gloomy! Do you [leave] or [stay]")
    if "leave"in c3:
        print("Adventure over, THE END!")
    else:
        print("You die! Adventure Over")
