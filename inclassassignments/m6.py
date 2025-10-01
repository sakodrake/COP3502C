

def fourbonacci(n):
    if n == 1:
        return 1
    if n == 2:
        return 4
    if n == 3:
        return 7
    if n == 4:
        return 8
    
    a = 1
    b = 4
    c = 7
    d = 8
    fourbonacci = 0
    for i in range(5, n+1):
        fourbonacci = 4*a + 3*b + 2*c + 1*d
        a , b , c , d = b, c , d , fourbonacci
    return d



def odd_squares(n):
    count = 0
    num = 1
    while count < n:
        root = int(num**0.5)
        if root * root == num and root % 2 == 1:
            print(num)
            count = count + 1
        num = num + 1
        
   
def diamond(n):
    spaces = 0
    for i in range(1, n+1, 2):
        spaces = (n- i) // 2
        for s in range(spaces):
            print(" ",end = "")
        for j in range(1, i+1):
            print(j, end="")
        print()
    for i in range (n-2,0,-2):
        spaces = (n-i) // 2
        for s in range(spaces):
            print(" ", end="")
        for j in range(1, 1+i):
            print(j, end="")
        print()
        

