while True:
    no=int(input("Enter a number: "))
    x=1
    counter=0
    while x<=no:
        #divide=no/x
        if(no%x==0):
            counter=counter+1
        x=x+1
    print("")
    if(counter==2):
        print(f"\033[92mNumber {no} is a prime number.\033[0m")
    else:
        print(f"\033[31mNumber {no} is not a prime number.\033[0m")
    print("\n")