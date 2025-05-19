print()
base = int(input("Enter the base number : "))
expo = int(input("Enter the exponent number : "))
x = 0
fin = 1

while x < expo:
    fin = fin * base
    x = x + 1
print()
print(f"nth power of given integer : {fin}")
print()