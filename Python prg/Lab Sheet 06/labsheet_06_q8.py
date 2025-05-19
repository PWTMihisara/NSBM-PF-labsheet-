print()
sentence = input("\033[33mEnter a sentence :\033[0m ")
search_term = input("\033[33mEnter a search term :\033[0m ")

index_position = sentence.find(search_term)

if index_position != -1:
    print()
    print(f"\033[32mThe search term\033[0m \033[34m'{search_term}'\033[0m \033[32mis found at index position :\033[0m {index_position}")
    print()
else:
    print()
    print("\033[31mSearch term not found in the sentence.\033[0m")
    print()