
while True:
    word = input ("try to guess the rule?!")

    if "s" not in word or "e" not in word:
        print (f"you lost;( {word}")
    else:
        print(f"you won! {word}")

    print ("")