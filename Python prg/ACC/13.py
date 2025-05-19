file = open("xyz.txt", "w+")
for i in range (5):
    name = input("Enter your name : ")
    file.writelines(name + "\n")

file.seek(0)   
print(file.read())
file.close()