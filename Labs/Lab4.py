def fibonacci(n):
    a = 0
    b = 1
    if n == 1:
        return 0
    if n == 2:
        return 1
    for i in range(3, n+1):
       a, b = b , b + a
    return b

print(fibonacci(6))

def is_prime(n):
    if n == 1 or n <= 0:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    elif n % 3 == 0:
        return False
    elif n % 5 == 0:
        return False
    else:
        return True
    
def print_prime_factors(n):
    factors = []
    original_number = n 
    while n % 2 ==0:
        factors.append(n)
        n = n // 2
    while n % 3 == 0:
        factors.append(n)
        n = n // 3
    while n % 5 == 0 :
        factors.append(n)
    return print(f"{original_number} = {factors}")

print(print_prime_factors(10))