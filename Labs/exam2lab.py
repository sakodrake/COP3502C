def print_backwards(word):
    if len(word) == 0:
        return
    if word == "":
        return ""
    else: 
        print_backwards(word[1:])
        print(word[0], end ="")

def format_names(list):
    if list == []:
        return list
    if "," in list[0]:
        formatted = list[0]
    elif " " in list[0]:
        news = list[0].split(" ")
        formatted = news[1] + ', ' + news[0]
    return [formatted] + format_names(list[1:])

def sum_a(list):
    if list == []:
        return 0
    if 'a' in list[0]:
        value = int(list[0]['a'])
    else:
        value = 0 
    return value + sum_a(list[1:])

def process_list(list):
    result = []
    for i in range(0, len(list), 2):
        result.append(str(list[i]))
    for i in range(1, len(list), 2):
        result.append(list[i] * 10)
    return result



