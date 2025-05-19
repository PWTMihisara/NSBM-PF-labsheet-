file = open("abc.txt", "r")
file.seek(5)
content = file.read()
print(content)