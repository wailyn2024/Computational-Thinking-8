#beginning: 
extrovert_points = 0
introvert_points = 0
ambivert_points = 0 

#question 1:
answer = input("On a weekend would you rather A) go out with friends, B) stay home alone, or C) Go to a cafe and read?")
if answer == "A":
	extrovert_points += 1
elif answer == "B":
	introvert_points += 1
elif answer == "C":
	ambivert_points +=1

#question 2:
answer = input("Would you rather own A) a dog, B) a cat, or C) a rabbit?")
if answer == "A":
	extrovert_points += 1
elif answer == "B":
	introvert_points+= 1
elif answer == "C":
    ambivert_points += 1 

#question 3:
answer = input("Would you rather eat lunch A) with a large group, B) with no one or 1 person, or C) with a small group?")
if answer == "A":
	extrovert_points += 1
elif answer == "B":
	introvert_points += 1
elif answer == "C": 
	ambivert_points += 1
#middle
#question 4: 
answer = input("Would you rather at a social gathering A) be the center of attention, B) be in the background, or C) talk with a few people")
if answer == "A":
	extrovert_points += 1
elif answer == "B":
	introvert_points += 1
elif answer == "C": 
	ambivert_points += 1

#question 5
answer = input("After a day of talking with with people is your social battery low or not A) whats a social battery? B) depends, or C) usually low")
if answer == "A":
	extrovert_points += 1
elif answer == "B":
	introvert_points += 1
elif answer == "C": 
	ambivert_points += 1

#question 6
answer = input("In general do you enjoy talking to people? A) yes, B) no, or C) yes and no")
if answer == "A":
	extrovert_points += 1
elif answer == "B":
	introvert_points += 1
elif answer == "C": 
	ambivert_points += 1

#end:
if introvert_points >extrovert_points:
	print("You are a cat person")
elif extrovert_points > introvert_points:
	print("You are a dog person")
elif ambivert_points >= introvert_points+extrovert_points: 
	print("You are both a dog person and a cat person")