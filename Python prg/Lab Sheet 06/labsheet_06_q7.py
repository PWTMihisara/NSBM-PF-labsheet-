enco_pwd ='K8$%j'
deco_pwd =''

for character in enco_pwd:
    ascii_value= ord(character)
    deco_pwd= deco_pwd + str(ascii_value)

print()
print(f"\033[92mThe decoded password is : \033[0m {deco_pwd}")
print()