number_of_items = int(input("Number of items: "))
total_price = 0
for i in range(0, number_of_items):
    total_price += float(input("Price of item: "))
if total_price > 100:
    total_price = total_price * 0.9 # Apply 10% discount
print(f"Total price for {number_of_items} items is ${total_price: .2f}")