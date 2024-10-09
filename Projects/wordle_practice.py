import random
word_list = []
hidden_word = random.choice(word_list)

for i in range (6):
    guess_word = input()
    output = ""
    if guess_word[0] ==hidden_word[0]:
        output+= " 🟩"
    elif guess_word[0] in hidden_word:
        output+= "🟨"
    else:
        output+= "⬛"
    if guess_word[1] ==hidden_word[1]:
        output+= " 🟩"
    elif guess_word[1] in hidden_word:
        output+= "🟨"
    else:
        output+= "⬛"
    if guess_word[2] ==hidden_word[2]:
        output+= " 🟩"
    elif guess_word[2] in hidden_word:
        output+= "🟨"
    else:
        output+= "⬛"
    if guess_word[3] ==hidden_word[3]:
        output+= " 🟩"
    elif guess_word[3] in hidden_word:
        output+= "🟨"
    else:
        output+= "⬛"
    if guess_word[4] ==hidden_word[4]:
        output+= " 🟩"
    elif guess_word[4] in hidden_word:
        output+= "🟨"
    else:
        output+= "⬛"
    
    print(output)
    if output == "🟩🟩🟩🟩🟩":
        print("You've Won")
        break