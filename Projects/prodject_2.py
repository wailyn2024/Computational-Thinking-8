print("hello")
print("welcome")
#choice 1
choice1 = input("do you know where you are?")
if "yes" in choice1:
    print("where are you? in a chair, behind a computer thinking this is just game")
    print("no, you don't have a clue where you are")
else:
    print("does that scare you? being lost, a stranger in a strange land")
print(" ")
print("I guess it wouldn't hurt to tell you what you're seeing")
print("you're on a stage in an old theatre")
print("no ones there. there's no spotlight, you've never been here a day in your life")
print("so why do you feel so nervous, like theres a crowd judging everything about you")\
#choice 2
choice2 = input("do you know your lines")
if "yes" in choice2:
#choice 3
    print("well say them")
    print("they're waiting")
    choice3 = input("do you want to [say your lines] or [stay in silence]")
    if "lines" in choice3:
        print("you try to say something, but you can't it feels like you're choking on your own words")
        print("you can't breathe")
        print("you die")
    elif "silence":
        print("so you resign yourself to this stage choosing to forever live in silence in front of an audience of nobody")
    else:
        print("so you choose to run away, maybe that's for the best, I'll miss you, but I'm sure you'll remember me. stranger")
else:
    print("well come up with something") 
    choice4 = input("do you [improvise] or stay [silent]")
    
    if "improvise" or "lines" in choice4:
        print("words spill out your mouth faster than you can think")
        print("I don't know what you said, neither do you though, but I find it hard to believe you've never rehearsed it. it seemed almost like it was always i the back of your mind")
        print("don't you agree?")
        print("at last the you no longer feel the need to satisfy an audience that isn't there")
        print("the curtain starts to close, it seems like it is time to take your leave")
        choice5 = input("do you [stay on stage] or [leave]")
        if "stay" in choice5:
            print("the shows over, and you weren't preforming for anyone anyways, you can go now.")
            print("but if you must stay, answer this question fo me")
            print("how sure are you that anything is real")
            print("how sure are you that you're not just the backdrop to some strange preformance not much different to the one ypu just did")
            choice6 = input("are you real, or not or do you even know")
            if "idk" or "who knows" or "I don' know" in choice6:
                print("I guess we'll never find out")
            else: print("how can you be so sure")
    else:
         print("so you resign yourself to this stage choosing to forever live in silence in front of an audience of nobody")
 