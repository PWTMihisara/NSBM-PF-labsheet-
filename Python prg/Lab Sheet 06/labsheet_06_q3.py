param1_x= int(input("Enter the first number : "))
param2_x= int(input("Enter the second number : "))
param3_x= int(input("Enter the thrid number : "))

output_x= pow(param1_x, param2_x, param3_x)

print("")
print("\033[31mParameter 1           parameter 2           parameter 3               expansion              output\033[0m")
print(f"     {param1_x}                   {param2_x}                        {param3_x}                    ({param1_x}^{param2_x})%{param3_x}                  {output_x}")