positive_count = 0
negative_count = 0
zero_count = 0

print()
print("\033[32mEnter 10 numbers : \033[0m")
print()

for _ in range (10):
    num = float(input())
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print()
print(f"\033[33mNumber of positive numbers :\033[0m {positive_count}")
print(f"\033[33mNumber of negative numbers :\033[0m {negative_count}")
print(f"\033[33mNumber of zeros :\033[0m {zero_count}")
print()