import math

current_result = 0.0
total_sum = 0
menu_selection = 'placeholder'
still_using = True
skip_menu = False

def calculator_menu():
    print("Calculator Menu")
    print('---------------')
    print('0. Exit Program')
    print('1. Addition')
    print('2. Subtraction')
    print('3. Multiplication')
    print('4. Division')
    print('5. Exponentiation')
    print('6. Logarithm')
    print('7. Display Average')
    return ''

def addition(num1, num2):
    sum = float(num1)+ float(num2)
    return sum

def subtraction(num1, num2):
    difference = float(num1) - float(num2)
    return difference

def multiplication(num1,num2):
    num1 = float(num1)
    num2 = float(num2)
    product = num1*num2
    return product

def division(num1,num2):
    quotient = float(num1) / float(num2)
    return quotient

def exponentiation(num1,num2):
    exponent = float(num1) ** float(num2)
    return exponent

def logarithm(num1,num2):
    num1 = float(num1)
    num2 = float(num2)
    logarithm = math.log(num2, num1)
    return logarithm

count = 0
while still_using:
    if not skip_menu:
        print(f'Current Result: {current_result}')
        print('')
        print(calculator_menu())
    skip_menu = False

    menu_selection = int(input('Enter Menu Selection: '))
    
    if menu_selection == 0:
        print('Thanks for using this calculator. Goodbye!')
        still_using = False
        break

    elif menu_selection == 1:
        num1 = (input('Enter first operand: '))
        num2 = (input('Enter second operand: '))
        if num1 == 'RESULT':
            num1 = current_result
        if num2 == 'RESULT':
            num2 = current_result
        current_result = addition(num1,num2)
        count = count + 1
        total_sum += current_result
    elif menu_selection == 2:
        num1 = input('Enter first operand: ')
        num2 = (input('Enter second operand: '))
        if num1 == 'RESULT':
            num1 == current_result
        if num2 == 'RESULT':
            num2 = current_result
        current_result = subtraction(num1,num2)
        count = count + 1
        total_sum += current_result
    elif menu_selection == 3:
        num1 = (input('Enter first operand: '))
        num2 = (input('Enter second operand: '))
        if num1 == 'RESULT':
            num1 == current_result
        if num2 == 'RESULT':
            num2 = current_result
        current_result = multiplication(num1,num2)
        count = count + 1
        total_sum += current_result
    elif menu_selection == 4:
        num1 = (input('Enter first operand: '))
        num2 = (input('Enter second operand: '))
        if num1 == 'RESULT':
            num1 == current_result
        if num2 == 'RESULT':
            num2 = current_result
        current_result = division(num1,num2)
        count = count + 1
        total_sum += current_result
    elif menu_selection == 5:
        num1 = (input('Enter first operand: '))
        num2 = (input('Enter second operand: '))
        if num1 == 'RESULT':
            num1 == current_result
        if num2 == 'RESULT':
            num2 = current_result
        current_result = exponentiation(num1,num2)
        count = count + 1
        total_sum += current_result
    elif menu_selection == 6:
        num1 = (input('Enter first operand: '))
        if num1 == 'RESULT':
            num1 = current_result
        num2 = (input('Enter second operand: '))
        if num2 == 'RESULT':
            num2 = current_result
        current_result = logarithm(num1,num2)
        count = count + 1
        total_sum += current_result
    elif menu_selection == 7:
        if count == 0:
            print("Error: No calculations yet to average!")
            print('')
            skip_menu= True
            continue
        else:
            print(f'Sum of calculations: {total_sum}')
            print(f'Number of calculations: {count}')
            print(f'Average of calculations: {total_sum/count:.2f}')
            print('')
            skip_menu = True
            continue
    else:
        print('Error: Invalid selection!')
        print('')
        skip_menu = True
        continue

    