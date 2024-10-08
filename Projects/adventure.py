# intro
# start
print("your in a basketball game")
print("you are down by four with 1 min left")
print("will you and your team win thr game in the final miniute")

# choice 1
c1 = input ("do you choose to [shoot the 3] or [pass to your teamate]")
if "shoot the 3" in c1:
    print("you miss the 3. you are still down by 4 with 48 seconds left")
    c2 = input("you have to play defense do you [go for the steal] or [play for the rebound]")
    if "go for the steal" in c2:
        print("you get drove by and they get a layup you are now down 6 with 36 seconds left")
    else:
        print("you get the rebound down by 2 with 40 seconds left")
else:
    print("you pass to your teamate and he scores a layup. you are now down by two with 48 seconds left")
    c3 = input("you have to play defense do you [go for the steal] or [play for the rebound]")
    if "play for the rebound" in c3:
        print("you get the rebound down by 2 with 40 seconds left")
        c4 = input("you get to [drive in for the layup] or [pass the ball]")
        if "drive in for layup" in c4:
            print("you score and are now tied with 30 seconds left")
            c6 = input ("your playing defense and your opponet drives in do you [go for the block] or [dont let him drive in]")
            if "go for the block" in c6:
                print("you get pumped faked and he gets a layup")
# your losing
            else:
                print("you get the steal and now on a fats break")

        else:
            print("you make a bad pass and it is a turnover, you are still down 6 with 30 seconds left")
        c5 = input("you get to [drive in for they layup] or [pass the ball]")
        if "pass the ball" in c5:
            print("you make a bad pass and it is a turnover, you are still down 6 with 30 seconds left")
            c7 = input ("your playing defense and your opponet drives in do you [go for the block] or [dont let him drive in]")
            if "go for the block" in c7:
                print("you get the block and our now on a fast break")
            else:
                print("you get the steal and you are now on a fast break")
            c7 = input ("you go for the [dunk] or you go for the [layup]")
        elif "dunk" in c8:
            c8 = input ("you make the dunk and win the game")
        else: 
            print("you abseloutly whiff the layup and lose")
#this is the end of the game


            