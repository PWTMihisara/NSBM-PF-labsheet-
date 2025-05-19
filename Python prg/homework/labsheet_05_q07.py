print()
try:
    no = int(input("Enter a number : "))
except ValueError:
    print()
    print("\033[31mPlease enter an integer value.\033[0m")
    print()
    quit()

x = no
sum = 0
mul = 1
dc = len(str(no))
for i in range(dc):
    digits = no % 10
    mul = digits**dc
    sum = sum + mul
    no = no//10

print()

if sum == x:
    print(f"\033[32mNumber {x} is a armstrong number.\033[0m")
else:
    print(f"\033[31mNumber {x} isn't a armstrong number number.\033[0m")
print()
