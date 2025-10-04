
def hex_char_decode(digit):
    digit = digit.upper()
    if '0' <= digit <= '9':
        return int(digit)
    if digit == 'A':
        return 10
    if digit == 'B': 
        return 11
    if digit == 'C':
        return 12
    if digit == 'D':
        return 13
    if digit == 'E':
        return 14 
    if digit == 'F':
        return 15
        

def hex_string_decode(hex):
    if len(hex) >= 2 and (hex[0] == '0') and (hex[1] in ['x', 'X']):
        hex = hex[2:]
    
    total = 0
    length = len(hex)
    for i in range(length):
        digit = hex[i]
        power = length - i - 1
        total += hex_char_decode(digit) * (16 ** power)

    return total

def binary_string_decode(binary):
    if len(binary) >=2 and binary[0] == '0' and binary[1] in ['b', 'B']:
        binary = binary[2:]
    
    total = 0
    length = len(binary)
    for i in range(length):
        digit = binary[i]
        power = length - i - 1
        if digit not in ['0', '1']:
            print(f'Invalid binary digit: {digit}')
        total += int(digit) * (2 ** power)
    return total 

def binary_to_hex(binary):
    decimal_value = binary_string_decode(binary)

    if decimal_value == 0:
        return "0x0"
    
    hex_digits = []
    while decimal_value > 0:
        remainder = decimal_value % 16
        decimal_value = decimal_value // 16

        if remainder <10:
            hex_digits.append(str(remainder))
        else:
            if remainder == 10:
                hex_digits.append('A')
            elif remainder == 11:
                hex_digits.append('B')
            elif remainder == 12:
                hex_digits.append('C')
            elif remainder == 13:
                hex_digits.append('D')
            elif remainder == 14:
                hex_digits.append('E')
            elif remainder == 15:
                hex_digits.append('F')
    
    hex_str = ''
    for i in range(len(hex_digits) -1 ,-1, -1):
        hex_str += hex_digits[i]
    
    return hex_str


def main():
    while True:
        print("\nDecoding Menu")
        print("-------------")
        print("1. Decode hexadecimal")
        print("2. Decode binary")
        print("3. Convert binary to hexadecimal")
        print("4. Quit")

        option = input("\nPlease enter an option: ")

        if option == '1':
            hex = input('Please enter the numeric string to convert: ')
            result = hex_string_decode(hex)
            print(f'Result: {result}')
        elif option == '2':
            binary = input('Please enter the numeric string to convert: ')
            result = binary_string_decode(binary)
            print(f'Result: {result}')
        elif option == "3":
            binary = input("Please enter the numeric string to convert: ")
            result = binary_to_hex(binary)
            print(f"Result: {result}")
        elif option == "4":
            print("Goodbye!")
            break
        else: 
            print("Invalid option. Please try again.")


if __name__ == "__main__":
    main()


     

        

            



   



    

    
