def is_armstrong(number):
    
    str_number = str(number)
    
    num_digits = len(str_number)
    sum_of_powers = sum(int(digit) ** num_digits for digit in str_number)
    
    return sum_of_powers == number

number = int(input("Enter a number: "))

if is_armstrong(number):
    print(f"{number} is an Armstrong number.")
else:
    print(f"{number} is not an Armstrong number.")