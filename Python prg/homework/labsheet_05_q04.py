print()
no = int(input("Enter a number : "))
sum = 0

while no > 0:
    digits = no % 10
    sum = sum + digits
    no = no // 10

print()
print(f"Sum of digits : {sum}") 