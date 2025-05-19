x=1
tot=0
while(x<=10):
    mark=int(input("Enter your marks: "))
    tot=tot+mark
    x+=1
avg=tot/10
print("")
print("Totle marks: ",tot)
print("Average: ",avg)
if(avg<50):
    print("You're failed.")
else:
    print("You're passed.")
