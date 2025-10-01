def sum(*nums):
    sum = 0.0
    for num in nums:
        sum += float(num)
    return sum

def print_range(num1, num2):
    for i in range(num1, num2):
        print(f"{i},", end =' ')
    print(num2)

def sum_of_digits(number):
    number = str(number)
    sum =[]
    result = 0
    for i in number:
        sum.append(i)
    for i in sum:
        result += int(i)
    return result


            
       




