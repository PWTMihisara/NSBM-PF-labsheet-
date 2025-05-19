marks = []

for i in range (10):
    print()
    mark = float(input(f"\033[32mEnter marks {i + 1}   :\033[0m "))
    marks.append(mark)

    max_mark = max(marks)
    min_mark = min(marks)
    avg_mark = sum(marks) / len(marks)

print()
print(f"\033[34mMaximum marks  :\033[0m \033[33m{max_mark}\033[0m")
print(f"\033[34mMinimunn marks :\033[0m \033[33m{min_mark}\033[0m")
print(f"\033[34mAverage mark   :\033[0m \033[33m{avg_mark}\033[0m")
print()