Game = True
while Game:
    word = input("what does grandpa like? ")

    if "e" in word and len(word) < 6 and not "a" in word or "c" in word and not "f" in word:
        print("grandpa likes " + word)
        False
    else:
        print("grandpa doesn't like "+ word)

    print("")