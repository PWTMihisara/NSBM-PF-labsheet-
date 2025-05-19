no1=int(input("Enter the first number: "))
no2=int(input("Enter the sencond number: "))
no3=int(input("Enter the third number: "))
if(no1>no2):
    hig1=no1
else:
    hig1=no2
if(hig1>no3):
    hig2=hig1
else:
    hig2=no3
print("")
print("The highest number is",hig2)
if(no1>no2):
    low1=no2
else:
    low1=no1
if(low1<no3):
    low2=low1
else:
    low2=no3
print("The lowest number is",low2)
