print("Enter the marks of 10 students:")
marks = [float(input()) for _ in range(10)]

max_marks = max(marks)
min_marks = min(marks)
avg_marks = sum(marks)

print(f"Maximum marks: {max_marks}")
print(f"Minimum marks: {min_marks}")
print(f"Average marks: {avg_marks:.2f}")
