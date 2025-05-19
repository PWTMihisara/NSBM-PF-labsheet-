print("Menu")
print("Select the operation;")
print("   C: Circumference of a circle")
print("   A: Area of a circle")
print("   V: Volume of a sphere")
while True:
    print("\n")
    opr=input("Enter the operation: ")

    rad=int(input("Enter the radius: "))
    pi=3.14159
    if opr=="C":
        fr=2*pi*rad
    elif opr=="A":
        fr=pi*rad**2
    elif opr=="V":
        fr=4/3*(pi*rad**3)
    else:
        fr="Invalid operation."
    print("")
    print("Result: ",fr)
