def flatten(lst):
    result = []
    for item in lst:
        if type(item) == list:
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

def mystery1(n):
    a, b, c, d, e = 1, 2, 3, 4, 5
    for i in range(n):
        a, b, c, d, e, = b, c, d, e, a - c + e
    return a

def mystery2(n):
    if n == 0:
        return 0 
    else:
        return (n % 10) + mystery2(n//10)

def collatz_sequence(integer):
    print(integer, end=" ")
    if integer == 1:
        print()
        return
    elif integer % 2 == 0:
        collatz_sequence(integer // 2)
    else:
        collatz_sequence(3*integer+1)

        