print("\n")
no1 = int(input("Enter the first number  : "))
no2 = int(input("Enter the second number : "))
no3 = int(input("Enter the third number  : "))
count = 0

for i in range(no1,(no2+1)):
    div = i % no3
    if div == 0:
        count += 1

print()        
print(count)
print()