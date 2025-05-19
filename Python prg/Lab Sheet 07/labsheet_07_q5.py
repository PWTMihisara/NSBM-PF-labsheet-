def summation(no1, no2):
    sum_1 = no1 + no2
    return sum_1

def main():
    for _ in range(3):
        no1 = float(input("Enter the first number : "))
        no2 = float(input("Enter the second number : "))

        print(f"Summation : {summation(no1, no2)}")

main()