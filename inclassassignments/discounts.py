price = float(input('Enter the price: '))
black_friday = input('Is it black friday [y/n]: ')
coupon = input('Do you have a coupon [y/n]: ')
employee_discount = input('Do you have an employee discount [y/n]: ')

if black_friday =='y':
    price = price - (price*0.4)
if coupon =='y':
    price = price - (price*0.05)
if employee_discount == 'y':
    price = price - (price*0.2)


print(f'The final price is: ${price:.2f}')