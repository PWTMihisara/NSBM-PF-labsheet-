count_salary_over_5000 = 0

print("Enter the employee number and basic salary (enter -999 for employee number to exit):")
while True:
    employee_no = int(input("Employee number (-999 to exit): "))
    if employee_no == -999:
        break 
    basic_salary = float(input("Basic salary: "))
    
    if basic_salary >= 5000:
        count_salary_over_5000 += 1

print(f"Number of employees with basic salary >= 5000: {count_salary_over_5000}")
