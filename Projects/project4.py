
#Beginning
Summer = 0
Winter = 0
Fall = 0

#Middle
# question 1:
answer = input("Would you rather A) Eat pumpkin pie , or B) Drink Hot-Cocoa, C) Lemonade?")
if answer == "A":
	Fall += 1
elif answer == "B":
	Winter += 1
else:
	Summer += 1

# question 2:
answer = input("Would you rather A) go skiing , or B) go to a pumpkin patch, C) go to the beach?")
if answer == "A":
	Winter += 1
elif answer == "B":
	Fall += 1
else:
	Summer += 1


# question 3:
answer = input("Would you rather eat lunch A) by yourself, or B) with a group, C) not eat lunch?")
if answer == "A":
	Fall += 1
elif answer == "B":
	Winter += 1
else:
	Summer += 1


# question 4:
answer = input("Would you rather go to the mall A) by yourself, or B) with a group, C) not go ?")
if answer == "A":
	Summer += 1
elif answer == "B":
	Fall += 1
else:
	Winter += 1

# question 5:
answer = input("Would you rather  A) blast music, or B) listen loud on headphones, C) not listen? ")
if answer == "A":
	Fall += 1
elif answer == "B":
	Winter += 1
else:
	Summer += 1



# end of quiz:
if Fall > Winter and Fall > Summer:
	print("You are a Fall person")
elif Winter > Fall and Winter > Summer:
	print("You are a Winter person")
else:
	print("You are a summer person!")