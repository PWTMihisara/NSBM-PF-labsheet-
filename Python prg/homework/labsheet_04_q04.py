while True:
    print()
    char = input("\033[32mEnter the character : \033[0m")
    vowel = "aeiouAEIOU"
    print()

    if char in vowel:
        print("\033[33mThis character is a vowel.\033[0m")
    else:
        print("\033[33mThis character is not a vowel.\033[0m")
        print()

    