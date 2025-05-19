name=input("Enter the name: ")
bs=float(input("Enter the basic salary: "))
if(bs<5000):
    ns=bs+bs*(5/100)
elif(bs<10000):
    ns=bs+bs*(10/100)
else:
    ns=bs+bs*(15/100)
print("")
print(f"Mr. {name} your new salary is {ns}")
print()