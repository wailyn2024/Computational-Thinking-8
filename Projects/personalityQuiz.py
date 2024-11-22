# Initialize points
extrovert_points = 0
introvert_points = 0

# question 1
answer = input("On a weekend, would you rather A) nap all day, or B) go on a hike?")
if answer == "A":
    introvert_points += 1
elif answer == "B":
    extrovert_points += 1

# question 2
answer = input("would you rather A) go out?, or B) stay in?")
if answer == "A":
    extrovert_points += 1
elif answer == "B":
    introvert_points += 1

# question 3
answer = input("Would you rather eat lunch A) by yourself, or B) with a group?")
if answer == "A":
    introvert_points += 1
elif answer == "B":
    extrovert_points += 1

# question 4
answer = input("Would you rather play sports A) or B) do art and read")
if answer == "A":
    extrovert_points += 1
elif answer == "B":
    introvert_points += 1

# question 5
answer = input("Do you like swimming in the ocean A), or B) walking in the park?")
if answer == "A":
    extrovert_points += 1
elif answer == "B":
    introvert_points += 1

# end of quiz
if extrovert_points > introvert_points:
    print("You are an extrovert.")
elif extrovert_points < introvert_points:
    print("You are an introvert.")
else:
    print("You are a balanced mix of both.")

