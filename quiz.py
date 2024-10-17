#Beginning

cat_points = 0
dog_points = 0
both_points = 0
#Middle

# question 1:
answer = input("On a weekend would you rather A) nap all day, B) go on a hike, or C) both?")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	both_points += 1

# question 2:
answer = input("Are you A) an extrovert, B) an introvert, or C) both?")
if answer == "A":
	dog_points += 1
elif answer == "B":
	cat_points += 1
elif answer == "C":
	both_points += 1

# question 3:
answer = input("Would you rather eat lunch A) by yourself, B) with a group, or C) both?")
if answer == "A":
	cat_points += 1
elif answer == "B":
	dog_points += 1
elif answer == "C":
	both_points += 1

# question 4:
answer = input("Would you rather A) sing karaoke with friends, B) listen to your playlist by yourself, or C) both?")
if answer == "B":
	cat_points += 1
elif answer == "A":
	dog_points += 1
elif answer == "C":
	both_points += 1

# question 5:
answer = input("Would you rather A) listen to Bruno Mars, B) listen to Faye Webster, or C) both?")
if answer == "B":
	cat_points += 1
elif answer == "A":
	dog_points += 1
elif answer == "C":
	both_points += 1

# end of quiz:
if cat_points >= dog_points:
	print("You are a cat person.")
elif cat_points <= dog_points:
	print("You are a dog person.")
elif both_points >= dog_points:
	print("You're a dog person AND a cat person!")
elif both_points >= cat_points:
	print("You're a dog person AND a cat person!")