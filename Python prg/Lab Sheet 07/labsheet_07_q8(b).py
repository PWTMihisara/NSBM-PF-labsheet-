def smallest(x:int, y:int, z:int)->int:
    return min(x, y, z)

x = int(input("Enter the first number : "))
y = int(input("Enter the second number : "))
z = int(input("Enter the third number : "))

print(smallest(x, y, z))