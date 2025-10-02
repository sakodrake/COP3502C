def bin(decimal):
    remainders = []
    if decimal == 0:
        return '0'
    while decimal > 0:
        if decimal % 2 == 0:
            remainders.append(0)
            decimal = decimal // 2
        elif decimal % 2 == 1:
            remainders.append(1)
            decimal = decimal // 2
    
    final_binary =''
    for i in range(len(remainders) -1, -1 ,-1):
        final_binary += str(remainders[i])
        
    return final_binary

def capitalize(string):
    words = []
    current_word = ""
    
    for i in string:
        if i != " ":
            current_word += i
        else:
            words.append(current_word)
            current_word = ""
    if current_word != "":
        words.append(current_word)

    final_words = []
    for word in words:
        if word == "":
            continue
        first_letter = word[0]
        rest = word[1:].lower()
        if first_letter.lower() not in ('o', 'u', 's', 'n', 'd'):
            first_letter = first_letter.upper()
        else:
            first_letter = first_letter.lower()
        final_words.append(first_letter + rest)

    return " ".join(final_words)
    


def partition(list, size):
    result = []
    for i in range(0,len(list), size):
        sublist = list[i: i + size]
        result.append(sublist)
    return result


    
        
    