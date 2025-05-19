def validate_email(email):
    if '@' in email and '.' in email:
        return True
    else:
        return False

print()
email = input("\033[33mPlease enter your email address :\033[0m ")

if validate_email(email):
    print()
    print("\033[32mThe entered email address is valid.\033[0m")
    print()
else:
    print()
    print("\033[31mThe entered email address is not valid.\033[0m")
    print()