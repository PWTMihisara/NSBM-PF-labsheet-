file = open("xyz.txt", "w")
for i in range(5):
    name = input("Enter your name : ")
    file.write(name + "\n")
file.close()