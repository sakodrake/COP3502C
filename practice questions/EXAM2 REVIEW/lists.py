def find_prime_factors(n):
    prime_factors = []      # make an empty list to put prime factors in
    for i in range(2, n+1):     # looking for factors, but now i need to check if these factors are prime
        if n % i == 0:
            for x in range(2, i):   # taking the factor found from previous if statement, and seeing if it's prime.
                if i % x == 0:  # if the factors has a divisor before itself, the function will break
                    break
            else:                               # if the for-loop breaks, this else statement activates.
                prime_factors.append(i)
    return prime_factors


def higher_course_level(courses1, courses2):
    course1_nums = []  
    course2_nums = []
    for courses in courses1:
        course1_nums.append(int(courses[3:7]))
    for courses in courses2:
        course2_nums.append(int(courses[3:7]))
    
    course1_avg = sum(course1_nums) / len(course1_nums)
    course2_avg = sum(course2_nums) / len(course2_nums)

    if course1_avg > course2_avg:
        return 1
    elif course2_avg > course1_avg:
        return 2
    else: 
        return 0
    
def higher_course_level1(courses1, courses2):
    courses1_avg = sum(int(courses[3:7]) for courses in courses1) / len(courses1)
    courses2_avg = sum(int(courses[3:7]) for courses in courses2) / len(courses2)

    if courses1_avg > courses2_avg:
        return 1
    elif courses2_avg > courses1_avg:
        return 1
    else: 
        return 0
    
def unique_in_order(seq):
    result = []
    for i in seq:
        if i not in result:
            result.append(i)
    return result


