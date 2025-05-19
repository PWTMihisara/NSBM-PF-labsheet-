print("Enter the prices of 10 items:")
prices = [float(input()) for _ in range(10)]

average_price = sum(prices)

items_over_200 = sum(1 for price in prices if price > 200)

print(f"Average value of an item: {average_price:.2f}")
print(f"Number of items with price greater than 200: {items_over_200}")
