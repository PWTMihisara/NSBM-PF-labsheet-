def main():
    students = []
    
    print("Please enter the names of five students:")
    for i in range(5):
        name = input(f"Enter the name of student {i+1} : ")
        students.append(name)
    
    students.sort()
    
    print(f"The first name in the sorted register is : {students[0]}")
    print(f"The last name in the sorted register is  : {students[-1]}")

if __name__ == "__main__":
    main()
