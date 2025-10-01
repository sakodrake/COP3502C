operation = input("Enter the operation: ")
operand = float(input("Enter the first operand: "))
operand2 = float(input('Enter the second operand: '))

if operation == 'add':
    result = operand + operand2
elif operation == 'sub':
    result = operand - operand2
elif operation == 'mul':
    result = operand * operand2
elif operation == 'div':
    result = round(operand / operand2, 2)

print(f'Result is {result}') 
