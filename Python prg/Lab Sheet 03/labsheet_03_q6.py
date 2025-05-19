bs=int(input("Enter the basic salary: "))
sy=int(input("Enter service years: "))
city=input("Enter the working city(input character 'C' if the city is Colombo): ")
ms=int(input("Enter the monthly sales: "))
if(sy>5):
    n1=bs+(bs*(10/100))
else:
    n1=bs
if(city=="C"):
    n2=n1+2500
else:
    n2=n1
if(ms<=25000):
    n3=n2+(ms*(10/100))
elif(ms<50000):
    n3=n2+(ms*(12/100))
else:
    n3=n2+(ms*(15/100))
print("The gross monthly remuneration is: ",n3)