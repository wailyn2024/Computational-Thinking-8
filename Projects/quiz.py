# Beginning 
intro_points = 0
extro_points = 0

print ("This is a personality quiz to see if you are more extroverted or introverted! Take your time, and please answer Q's with either a CAPITAL A or a CAPITAL B. Enjoy!!!")

# Middle: Question 1
answer = input("When your not busy, would you rather A) go to the mall with friends, or B) Stay inside and cook/bake with your significant other?")
if answer == "A":
    extro_points += 1
elif answer == "B":
    intro_points += 1

# Question 2
answer = input("Would you rather have A) a cat, or B) a dog?")
if answer == "A":
    intro_points += 1
elif answer == "B":
    extro_points += 1

# Question 3
answer = input("Whats sounds easier to complete things, A) Do one thing at a time, or B) Multitask?")
if answer == "A":
    intro_points += 1
elif answer == "B":
    extro_points += 1

# Question 4
answer = input("On the weekend would you rather A) Go to a party, or B) play a board game with family?")
if answer == "A":
    extro_points += 1
elif answer == "B":
    intro_points += 1

# Question 5
answer = input("Whats sounds more exciting, A) Playing a new video game, or B) Go to a new restaurant?")
if answer == "A":
    intro_points += 1
elif answer == "B":
    extro_points += 1

# Question 6
answer = input("Would you rather A) Take a pottery class, or B) Practice a musical instrument?")
if answer == "A":
    extro_points += 1
elif answer == "B":
    intro_points += 1

# Question 7
answer = input("Would you rather A) Sing in the forest, or B) Dance in the rain?")
if answer == "A":
    intro_points += 1
elif answer == "B":
    extro_points += 1

# Question 8
answer = input("At school, would you rather take a A) Debate class, or a B) Programming class?")
if answer == "A":
    extro_points += 1
elif answer == "B":
    intro_points += 1

# Question 9
answer = input("What option sounds easier to complete work, A) Working with a group, or B) by yourself?")
if answer == "A":
    extro_points += 1
elif answer == "B":
    intro_points += 1

# Question 10
answer = input("What sounds better, A) going on a hike, or B) going to a sports game?")
if answer == "A":
    intro_points += 1
elif answer == "B":
    extro_points += 1

# Question 11
answer = input("When you have a problem, would rather A) Talk to someone about it, or B) Bottle it up?")
if answer == "A":
    extro_points += 1
elif answer == "B":
    intro_points += 1

# Question 12
answer = input("Would you rather drink A) Hot tea, or B) Iced tea?")
if answer == "A":
    intro_points += 1
elif answer == "B":
    extro_points += 1

# Question 13
answer = input("What sounds cooler, A) A piercing, or B) A tattoo?")
if answer == "A":
    extro_points += 1
elif answer == "B":
    intro_points += 1

# Question 14
answer = input("What sounds better, A) Have a group of friends, or B) Have your dream best friend?")
if answer == "A":
    extro_points += 1
elif answer == "B":
    intro_points += 1

# Question 15
answer = input("Would you rather A) Go to the spa, or B) Go Rock climbing?")
if answer == "A":
    intro_points += 1
elif answer == "B":
    extro_points += 1

# Question 16
answer = input("What love language do you prefer, A) Physical touch, or B) Quality time?")
if answer == "A":
    extro_points += 1
elif answer == "B":
    intro_points += 1

# Question 17
answer = input("What place would you rather travel to, A) Tokyo, Japan, or B) Paris, France? ")
if answer == "A":
    extro_points += 1
elif answer == "B":
    intro_points += 1

# Question 15
answer = input("Pick a season, A) Spring or B) Autumn?")
if answer == "A":
    intro_points += 1
elif answer == "B":
    extro_points += 1

# End: Determine results
if extro_points > intro_points:
    print ("You are more of an Extrovert!")
elif intro_points > extro_points:
    print ("You are more Introverted!")
elif extro_points == intro_points:
    print ("You are an ambivert! You are equally introverted and extroverted!!!")