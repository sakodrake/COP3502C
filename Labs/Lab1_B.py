#Calculate sales tax 

item_price = float(input('Enter the price of the item: '))
sales_tax = float(input('Enter the sales tax percentage: ')) * 0.01
final_price = item_price + (item_price * sales_tax)

print(f'Your total is ${final_price:.2f}')