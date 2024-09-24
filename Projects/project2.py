#Intro to Story
print("You're a player on a very good under 17 soccer team.")
print("You play as starting striker, and your team is in the final of World Championships. ")
print("You're in training the week before the game..")


#Choice 1
c1=input("Do you choose to work on your [Dribbling] or [Shooting]?")
if "hooting" in c1:
    print("You work on your long shots and score some beautiful goals!")
    #Choice 2A
    print("A few days have passed, and you're warming up for your game now.")
    print("The game kicks off, and you get the ball in the opponent half.")
    c2A=input("Do you try to dribble a defender or do you pass the ball to your teammate")
    if "ribble" in c2A:
         print("You try to dribble the defender but fail. The other team gets the ball and they score!")
    else: 
        print("You pass the ball to your teammate, but the attack fails.")




else:
    print("You work on your dribbling and impress your teammates!")
#Choice 2B
    print("A few days have passed, and you're warming up for your game now.")
    print("The game kicks off, and you get the ball in the opponent half.")
    c2B=input("Do you try to [dribble] a defender or do you [pass] the ball to your teammate")
    if "ribble" in c2B:
        print("You dribble the first defender and get past them!")
        print("You're open on goal and score!!!!!!")


    else:
        print("You pass the ball to your teammate, but the attack fails!")
#Choice 2BB
        print("The game is ending soon, with the score 0,0")
        print("Your teammate sends a through ball to you, and you're alone against the keeper.")
        c2BB=input("Do you shoot [left] or [right]?")
        if "eft" in c2BB:
            print("You shoot left but the keeper saves it!")
        else:
            print("You shoot right and Score!!")

#Choice 2BBB
        print("It turns out your run was offsides. ")
        print("Now your team is on the defense")
        print("An opposing player is in front of you, with just you standing between him and goal in the last minute of the game.")
        c2BBB=input("Do you slide tackle him or wait for backup?")
        if "lide" or "ackle" in c2BBB:
            print("You slide tackle but the attacker flicks over you.")
            print("He passes the ball to his teammate, who shoots.")
            print("He scores!")
            print("You have lost the final.")
            print("The end")
        else:
            print("You  wait for backup, and successfully defend the attack! ")
            print("The game goes to penalties.")
            print("You are taking the fifth penalty. If you score, your team wins. ")
            print("Good luck.")
            c2BBBB=input("Do you shoot [middle],[left],or [right]?")
            if "iddle" in c2BBBB:
                print("You shoot down the middle...")
                print("and SCORE!")
                print("You lift the the trophy with your team.")
                print("SUCCESS!")
            elif "eft" in c2BBBB:
                print("You shoot left...")
                print("But the keeper saves it!")
                print("Better luck next time.")
            else:
                print("You shoot right...")
                print("and SCORE!!!")
                print("You lift the trophy with your team!")
                print("VICTORY!!")

