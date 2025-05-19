def tovertime_payment(hw):
    if hw <= 40:
        return hw * 150
    else:
        return (40 * 150) + ((hw - 40) * 200)

def main():
    emp_data = []
    emp_count = 0
    count_4000 = 0

    while True:
        print()
        emp_number = int(input("Enter Employee Number (-999 to end): "))
        if emp_number == -999:
            break

        hw = float(input("Enter Hours Worked: "))

        overtime_payment = tovertime_payment(hw)
        emp_data.append((emp_number, overtime_payment))
        emp_count += 1

        if overtime_payment > 4000:
            count_4000 += 1

    if emp_count > 0:
        percentage = (count_4000 / emp_count) * 100
    else:
        percentage = 0

    print("\nEmployee Number | Over Time Payment")
    print("-----------------------------------")
    for emp in emp_data:
        print(f"{emp[0]:<16}| Rs. {emp[1]:.2f}")
    print("-----------------------------------")

    print(f"\nPercentage of employees with Over Time Payment exceeding Rs. 4000: {percentage:.2f}%")
    print()

if __name__ == "__main__":
    main()

