# Beginning: create variables
cat_points = 0
dog_points = 0
frog_points = 0

# Middle: Ask questions
# question 1:
answer = input("On a weekend would you rather A) nap all day, or B) go on a hike?, or go swimming")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	frog_points +=1


# question 2:
answer = input("(Would you rather eat out A) or B) cook at home, or cook at home with family")
if answer == "A":
	dog_points += 1
elif answer == "B":
	cat_points += 1
elif answer == "C":
	frog_points +=1

# question 3:
answer = input("Would you rather eat lunch A) by yourself, or B) with a group, or eat with your best friend?")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	frog_points += 1

# question 4:
answer= input ("Are you A) an extrovert, or B) an introvert?/n, or kinda in the middle")
if answer == "A":
	dog_points += 1
elif answer == "B":
	cat_points += 1
elif answer == "C":
	frog_points += 1

# question 5:
answer= input ("Would you rather go Skydiving, or B) Go on a hot air ballon?, or go kart racing")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	frog_points += 1


# End: determine results 
if cat_points > dog_points and cat_points > frog_points:
	print("You are a cat person")
elif dog_points > cat_points and dog_points > frog_points:
	print("You are a dog person")
elif frog_points > dog_points and frog_points > cat_points:
	print("You are a frog person")