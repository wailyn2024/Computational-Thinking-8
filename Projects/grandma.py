
vowels = "aeiouAEIOU"
 





while True:
    word = input("WHat do you think grandma likes?")
    count = sum(word.count(vowel) for vowel in vowels)


    if count > 2:
        print(f"Grandma doesn't like {word}!")
    else:
        print(f"Grandma likes {word}")

    print("")


