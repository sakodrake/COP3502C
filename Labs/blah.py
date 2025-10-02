def hex_char_decode(digit):
            check_first2 = []
            for i in digit:
                check_first2.append(i)

            if check_first2[0] == 0 and check_first2[1] == x:
                digit = digit[:0] + digit[2:]

            value = 0
            if int(digit) < 10:
                value = digit
            if digit == 'A':
                value = 10
            if digit == 'B': 
                value = 11
            if digit == 'C':
                value = 12
            if digit == 'D':
                value = 13
            if digit == 'E':
                value = 14 
            if digit == 'F':
                value = 15
            return value 

def hex_string_decode(hex):
      check_first2 = []
      hex = str(hex)
      for i in hex:
            check_first2.append(i)
      if check_first2[0] == '0' and check_first2[1] == 'x':
                hex = hex[:0] + hex[2:]
      else:
        hex = hex
      
      total = 0 
      for i in hex:
            total += hex_char_decode(i) * 16**(str(len(hex)) - i) # need to find a way to calculate the index of the number!
            return total


hex_string_decode('0x573632')