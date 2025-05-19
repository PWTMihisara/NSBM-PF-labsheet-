def password_strength(password):
    if len(password) >= 8:
        return True
    else:
        return False

def main():
    while True:
        print()
        password = input("\033[33mPlease enter your password :\033[0m ")
        
        if password_strength(password):
            print()
            print("\033[32mNew Password accepted.\033[0m")
            print()
            break
        else:
            print()
            print("\033[31mPassword is weak. Please enter a password with at least 8 characters.\033[0m")
            print()
            
if __name__ == "__main__":
    main()
