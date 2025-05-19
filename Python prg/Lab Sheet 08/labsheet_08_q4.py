def celsius(fah):
    cel = (5/9)*(fah - 32)
    return cel

def fahrenheit(cel):
    fah = ((9/5)*cel) + 32
    return fah

print()
print("\033[33m\033[1m\033[4mCelsius to Fahrenheit and Fahrenheit to Celsius Conversion\033[0m")
print()
print("------------------------------------------------------------------")
print(f"| {'Celsius(°C)':<15} {'Fahrenheit(F)':<16} | {'Fahrenheit(F)':<15} {'Celsius(°C)':<10} |" )
print("------------------------------------------------------------------")

for i in range(101):
    print(f"|  {i:<15} {round(fahrenheit(i), 1):<15} |  {round(32 + (i * (180 / 100)), 1):<15} {round(celsius(32 + (i * (180 / 100))), 1):<10} |")

print("------------------------------------------------------------------")