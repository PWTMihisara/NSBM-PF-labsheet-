basic_salary = []
while True:
    print()
    emp_no = int(input("\033[32mEnter the Employee No (or -999 to stop) :\033[0m "))

    if emp_no == -999:
                break

    bs = float(input(f"\033[33mEnter the basic salary for Employee No \033[34m{emp_no}\033[0m \033[33m:\033[0m "))
    basic_salary.append(bs)

above_5000 = sum(1 for salary in basic_salary if salary >= 5000 )
print()
print(f"\033[31mNumber of employees with a basic salary >= 5000 :\033[0m {above_5000}")
print("\n")