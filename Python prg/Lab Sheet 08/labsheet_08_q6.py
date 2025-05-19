def reverse(no):
    reverse = 0
    no_str = str(no)
    counter = len(no_str)

    for _ in range(counter):
        last_digit = no % 10

        reverse_num = reverse * 10 + last_digit

        no = no // 10
    
    return reverse_num

no = int(input("Enter a number : "))

print()
print(f"Reversed version of the number : {reverse(no)}")