for i in range(7):
     temperatures = []
     print()
temperatures.append(float(input(f"Enter the tempertures for day {i + 1} : ")))

Average_temperature=sum(temperatures)/len(temperatures)

print("\n")
print(f"The Average temperture for the week is {Average_temperature} degrees.")
print()