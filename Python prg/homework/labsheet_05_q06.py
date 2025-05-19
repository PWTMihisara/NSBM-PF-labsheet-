print()
first = 0
second = 1

for i in range(10):
    if i <= 1:
        next = i
    
    else:
        next = first + second
        first = second
        second = next

    print(next)
    print()