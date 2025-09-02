price = float(input("What is the listed price of the item: "))
tax_rate = 0.06
paid = float(input("How much did the customer pay: " ))

change = paid - (price + (price * tax_rate))

print(f"They get ${change:.2f} in change")

