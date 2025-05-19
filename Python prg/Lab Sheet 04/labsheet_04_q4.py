while True:
    char=input("Enter a character: ")
    print("")
    vowels="aeiouAEIOU"
    if char in vowels:
        print(f"The character '{char}' is a vowel")
    else:
        print(f"The character '{char}'is not a vowel")
    print("\n")
