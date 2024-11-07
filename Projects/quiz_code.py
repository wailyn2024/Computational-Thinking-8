cat_points = 0
dog_points = 0
questions_answered = 0

#beginning
# question 1:
answer = input("On a weekend would you rather A) nap all day, or B) go on a hike?")
if answer == "A":
	cat_points += 1
	questions_answered += 1
elif answer == "B":
	dog_points += 1
	questions_answered += 1

# question 2:
answer = input("Are you A) an extrovert, or B) an introvert?")
if answer == "A":
	dog_points += 1
	questions_answered += 1
elif answer == "B":
	cat_points += 1
	questions_answered += 1

# question 3:
answer = input("Would you rather eat lunch A) by yourself, or B) with a group?")
if answer == "A":
	cat_points += 1
	questions_answered += 1
elif answer == "B":
	dog_points += 1
	questions_answered += 1
	
    # question 4:
answer = input("Are you more of a A) morning person, or B) night owl?")
if answer == "B":
	cat_points += 1
	questions_answered += 1
elif answer == "A":
	dog_points += 1
	questions_answered += 1
	
    # question 5:
answer = input("Would you rather A) eat food alone, or B) eat with friends and family?")
if answer == "A":
	cat_points += 1
	questions_answered += 1
elif answer == "B":
	dog_points += 1
	questions_answered += 1
	
    # question 6:
answer = input("What hobbies do you prefer? A) collecting and reading books, or B) exercising/playing sports?")
if answer == "A":
	cat_points += 1
	questions_answered += 1
elif answer == "B":
	dog_points += 1
	questions_answered += 1
	
    # question 7:
answer = input("How affectionate are you? Do you A) greet everyone with a smile and a hug, or B) does it take a while for you to warm up to people?")
if answer == "B":
	cat_points += 1
	questions_answered += 1
elif answer == "A":
	dog_points += 1
	questions_answered += 1
	
     # question 8:
answer = input("What music do you prefer? A) Pop and upbeat music, or B) Lo-fi and smooth jazz?")
if answer == "B":
	cat_points += 1
	questions_answered += 1
elif answer == "A":
	dog_points += 1
	questions_answered += 1
	
    # question 9:
answer = input("How many people are in your friend group. A) More then 10, or B) only a couple of people.")
if answer == "B":
	cat_points += 1
	questions_answered += 1
elif answer == "A":
	dog_points += 1
	questions_answered += 1
	
    # question 10:
answer = input("On weekends do you sleep in? A) yes, or B) no.")
if answer == "A":
	cat_points += 1
	questions_answered += 1
elif answer == "B":
	dog_points += 1
	questions_answered += 1

	# question 11:
answer = input("How do you feel right now? A) meh, or B) good?")
if answer == "A":
	cat_points += 1
	questions_answered += 1
elif answer == "B":
	dog_points += 1
	questions_answered += 1

	# question 12:
answer = input("Choose a scent! A) Warm vanilla sugar, or B) Hot cocoa")
if answer == "B":
	cat_points += 1
	questions_answered += 1
elif answer == "A":
	dog_points += 1
	questions_answered += 1

	# question 13:
answer = input("What movie do you prefer? A) The Incredibles, or B) Zootopia?")
if answer == "A":
	cat_points += 1
	questions_answered += 1
elif answer == "B":
	dog_points += 1
	questions_answered += 1

	# question 14:
answer = input("Choose a tv show to binge watch. A) The Office, or B) Glee?")
if answer == "B":
	cat_points += 1
	questions_answered += 1
elif answer == "A":
	dog_points += 1
	questions_answered += 1
	
# question 15:
answer = input("Last question! Is the glass A) half empty or B) half full?")
if answer == "A":
	cat_points += 1
	questions_answered += 1
elif answer == "B":
	dog_points += 1
	questions_answered += 1

# end of quiz:
if cat_points > dog_points:
	print("You are a cat person!")
elif dog_points > cat_points:
	print("You are a dog person!")