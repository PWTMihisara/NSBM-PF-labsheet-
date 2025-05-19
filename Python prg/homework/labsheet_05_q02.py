x = 1
tot = 0

while (x<=10):
    print()
    marks = int(input("\033[32mEnter your marks :\033[0m "))
    tot = tot + marks
    x+=1

avg = tot / 10

print()
print(f"\033[33mTotal of your marks :\033[0m \033[34m{tot}\033[0m\033[33m.\033[0m")
print()
print(f"\033[33mAverage of your marks :\033[0m \033[34m{avg}\033[0m\033[33m.\033[0m")
print()

if marks < 50:
    print("\033[31mYou are fail.\033[0m")
else:
    print("\033[32mYou are pass.\033[0m")
print()