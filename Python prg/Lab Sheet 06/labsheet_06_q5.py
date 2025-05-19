item1 = "Apple"
amount1 = 2.3
price = "5.99"

item2 = "Orange"
amount2 = "3"
price2 = 3.50

item3 = "Mango"
amount3 = 5
price3 = 2

Total_item = round(amount1)+int(amount2)+amount3
Total_price = round(amount1)*float(price)+int(amount2)*price2+amount3*price3

print()
print(f"\033[34mTotal Items:\033[0m {Total_item}")
print(f"\033[34mTotal Price:\033[0m Rs.{round(Total_price,2)}/=")
print()