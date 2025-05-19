price = []
for i in range (10):
    print()
    no = int(input("\033[32mEnter price of item : \033[0m"))
    price.append(no)


avg = sum(price)/len(price)
greater = sum(1 for no in price if no > 200)

print()
print(f"\033[34mAverage value of an items        :\033[0m {avg}")
print(f"\033[34mNumber of items greater than 200 :\033[0m {greater}")
print("\n")