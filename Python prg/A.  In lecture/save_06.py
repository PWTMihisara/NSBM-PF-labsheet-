positive_count = 0
negative_count = 0
zero_count = 0

print("Enter 10 numbers:")
numbers = [float(input()) for _ in range(10)]

for num in numbers:
    if num > 0:
        positive_count += 1
    elif num < 0:
        negative_count += 1
    else:
        zero_count += 1

print(f"Number of positive numbers: {positive_count}")
print(f"Number of negative numbers: {negative_count}")
print(f"Number of zeros: {zero_count}")
