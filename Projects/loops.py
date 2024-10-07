import random

# Pick a word at random
word_list = ["loopy","heart","audio","laugh","trial"]
hidden_word = random.choice(word_list)

# Repeat for 6 guesses
for i in range(6):
    # Guess a word
    guess_word = input()
    output = ""

    # First letter (in python, counting starts at 0 not 1)
    if guess_word[0] == hidden_word[0]:
        output += "green"
    elif guess_word[0] in hidden_word:
        output += "orange"
    else:
        output += "black"


        # Result
        print(output) 
        if output == "green green green green green":
            print("you win")
            break

print(f"You used {i+1}guesses")   