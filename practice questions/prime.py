def is_prime(n):
    if n <= 1:
        print("Not prime!")
        return
    
    count = 0
    for i in range(2,n):
        if n % i == 0:
            count += 1
   
    if count == 0:
        print("It's prime!")
    else:
        print("Not prime!")


#def identical_digits(num):
    #outputs = []
    #for i in range(num, 91):
        #new = str(i)
        #for i in new:


def print_triangle(base):
    for i in range(0,base +1):
        print("*" * i)

def print_inverse_triangle(base):
    for i in range(0, base + 1):
        print("*" * (base - i))

print_inverse_triangle(5)

            
        

