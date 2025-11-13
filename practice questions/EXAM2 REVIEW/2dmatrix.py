# given a 2d list (matrix) of integers, write a function that returns a new list containing the sum of each row.

def twod_matrix(list):
    result = []
    for i in list:
        result.append(sum(i))
    return result

def twod_matrix_recursion(list):
    if len(list) == 0:
        return []
    else:
        result = sum(list[0])
    return [result] + twod_matrix_recursion(list[1:])

# take a list of numbers as input, where the list can contain nested lists, and print the sum of all the numbers in the list.

def sum_of_list(lst):
    if len(lst) == 0:
        return 0
    elif type(lst[0]) == list:
        result = sum(lst[0])
    else:
        result = (lst[0])
    return result + sum_of_list(lst[1:])



# takes a string as an argument and retruns a dictionary containing vowels as keys and their counts as values
"""
def count_vowels(string):
    result = {}
    for i in string:
        if i not in result:
            result[i] += 0
            result[i] += 1
        else: 
            result[i] += 1

print(count_vowels("Hello World"))

def count_vowels_prof(string):
    vowels = 'aeiou'
    vowel_count = {}

    for char in string:
        char_lower = char.lower()

        if char_lower in vowels:
            if char_lower in vowel_count:
                vowel_count[char_lower] += 1
            else:
                vowel_count[char_lower] = 1
    return vowel_count         

def count_vowels(text):
    if len(text) == 0:
        return {}
    letter = text[-1].lower()
    counts = count_vowels_
"""

# write a recursive function that takes a list of numbers and returns True if the list is sorted in ascending order and False otherwise.

def is_sorted(lst):
    isSorted = True
    if len(lst) == 0:
        return True
    if len(lst) == 1:
        return True 
    elif lst[0] > lst[1]:
        isSorted = False
    else:
        return is_sorted(lst[1:])
    return isSorted

print(is_sorted([1,2,3,2,4]))
            
