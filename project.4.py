# Beginning: create variables
julio_points = 0
nicholas_points = 0
drew_points = 0

# Middle : ask questions
# question 1 :
answer = input("What would you rather watch in your free time A) anime , B) murder mystery, C) outer banks?/n")
if answer == "A":
    julio_points += 1
elif answer == "B":
    nicholas_points += 1
elif answer == "C":
    drew_points += 1

    # question 2 :
answer = input("Are you more A) active, or B) homebody?/n")
if answer == "A":
    julio_points += 1
elif answer == "B":
    nicholas_points += 1
    drew_points += 1

    # question 3 :
answer = input("Would you rather eat lunch A) with your team, B) with your sibling, or C) with friends?/n")
if answer == "A":
    julio_points += 1
elif answer == "B":
    nicholas_points += 1
elif answer == "C":
    drew_points += 1

    # question 4 :
answer = input("Would you rather travel to A) the Dominican Republic, B) Texas , or C) north carolina?/n")
if answer == "A":
    julio_points += 1
elif answer == "B":
    nicholas_points += 1
elif answer == "C":
    drew_points += 1

    # question 5 :
answer = input("Would you rather do A) football, B) baseball, or C) acting?/n")
if answer == "A":
    nicholas_points += 1
elif answer == "B":
    julio_points += 1
elif answer == "C":
    drew_points += 1

    # End: determine results
    if julio_points> drew_points and julio_points> nicholas_points:
        print("You are more like Julio Rodriguez!")
    elif drew_points> julio_points and drew_points> nicholas_points:
        print("You are more like Drew Starkey!")
    elif nicholas_points> julio_points and nicholas_points> drew_points:
        print("You are more like Nicholas Alexander Chavez")