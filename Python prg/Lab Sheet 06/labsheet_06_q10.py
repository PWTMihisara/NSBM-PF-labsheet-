def main():
    numbers = []
    
    print("Please enter 10 numbers:")
    for i in range(10):
        while True:
            try:
                number = float(input(f"Enter number {i+1} : "))
                numbers.append(number)
                break
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    
    max_number = max(numbers)
    min_number = min(numbers)
    
    print(f"The maximum number entered is : {max_number}")
    print(f"The minimum number entered is : {min_number}")

if __name__ == "__main__":
    main()
