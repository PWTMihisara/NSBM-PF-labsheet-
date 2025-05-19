def even(no):
    if no%2 == 0:
        return 1
    else:
        return 0

while True:

    try:
        no = str(input("Enter an integer.(enter 'exit' to exit) : "))
        if no.lower() == 'exit':
            break
        no = int(no)
    except ValueError:
        print("\033[31mInvalid input. Enter an integer.\033[0m")
        print()
        continue

    if even(no) == 1:
        print(f"\033[32m{no} is an even number.\033[0m")
    else:
        print(f"\033[32m{no} is an odd number.\033[0m")
    print()
