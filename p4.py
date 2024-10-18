cat_points = 0
dog_points = 0
weirdo_points =0

# question 1:
answer = input("On a weekend would you rather A) nap all day, or B) go on a hike?")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1

# question 2:
answer = input("Are you A) an extrovert, or B) an introvert?")
if answer == "A":
	dog_points += 1
elif answer == "B":
	cat_points += 1

# question 3:
answer = input("Would you rather eat lunch A) by yourself, or B) with a group?")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1

# question 4:
answer= input ("would u rather eat A)cat food or B)dog food")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points+= 1
	
    #5
answer= input ("are you allergic to A) cats B) dogs C)nothing")
if answer == "A":
    dog_points += 1
elif answer == "B":
    cat_points += 1
elif answer == "C":
     weirdo_points += 100
	
    # end of quiz:
if cat_points > dog_points and cat_points> weirdo_points :
	print("You are a cat person")
elif dog_points > cat_points and dog_points> weirdo_points:
	print("You are a dog person")
elif weirdo_points> dog_points and weirdo_points> cat_points:
	print ("your a damn weirdo sorry for the language josh")
