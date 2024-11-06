# Starting points

cat_points = 0
dog_points = 0

#  middle question 1:
answer = input("On a weekend would you rather A) nap all day, or B) go on a hike?, or C) run around all day")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	dog_points += 1
#  middle question 2:
answer = input("Are you A) an extrovert, or B) an introvert?, or C) in the middle")
if answer == "A":
	dog_points += 1
elif answer == "B":
	cat_points += 1
elif answer == "C":
	dog_points += 1
# middle question 3:
answer = input("Would you rather eat lunch A) by yourself, or B) with a group?, or C) in the dark")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	cat_points += 1

# middle question 4:
answer = input("Are you A) a night person, or B) an morning person, or C) or are you nocturnel?")
if answer == "A":
	cat_points += 2
elif answer == "B":
	dog_points += 2
elif answer == "C":
	cat_points += 5
# middle question 5:
answer = input("Do you like big A) small spaces, or B) big spaces, or C) super big spaces")
if answer == "A":
	cat_points += 2
elif answer == "B":
	dog_points += 2
elif answer == "C":
	dog_points += 5
# End of quiz
if cat_points > dog_points:
	print("You are a cat person")
elif dog_points > cat_points:
	print("You are a dog person")