print("Simple Calculator")
print("Select the operator;")
print("   1: Addition (+)")
print("   2: Substraction (-)")
print("   3: Division (/)")
print("   4: Multipication (*)")
while True:
    print("\n")
    opr=input("Enter the operation: ")

    no1=int(input("Enter first nuumber: "))
    no2=int(input("Enter second nuumber: "))

    if(opr=="1"):
        fr=no1+no2
    elif(opr=="2"):
        fr=no1-no2
    elif(opr=="3"):
        fr=no1/no2
    elif(opr=="4"):
        fr=no1*no2
    else:
        fr="Invalid operation."
    print("")
    print("Result: ",fr)
