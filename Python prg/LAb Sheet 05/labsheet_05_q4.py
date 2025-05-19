no=int(input("Enter a number: "))
x=no
sum=0
while no>0:
    digit=no%10
    sum=sum+digit
    no=no//10
print(f"Given number: {x}")
print(f"Sum of digits: {sum}")