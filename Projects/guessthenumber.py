import random
max = random.randint(10,100)
number = random.randint(1,max)
game = True
guesses = 0
while game:
    print("guess a number from 1-"+str(max))
    guess = int(input(""))
    if guess == number:
        print("Good job!")
        guesses += 1
        print("You took "+str(guesses))
        game = False
    elif guess > number:
        print("too large")
    elif guess < number:
        print("too small")