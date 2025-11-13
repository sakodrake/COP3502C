def is_strictly_increasing(numbers):
    compare = []
    if len(numbers) < 2:
        return True
    for i in range(1, len(numbers)):
        if i == numbers:
            break
        if numbers[i] < numbers [i +1]:
            return True
        else: 
            return False
        
print(is_strictly_increasing([1,2,3,2]))