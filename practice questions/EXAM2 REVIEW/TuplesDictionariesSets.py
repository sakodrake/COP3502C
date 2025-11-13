def is_anagram(word_1, word_2):
    if len(word_1) != len(word_2):
        return False
    
    wordlist_1 = list(word_1)
    for i in wordlist_1:
        if i in word_2:
            wordlist_1.remove(i)
        else:
            return False
    return True

def dupe_letter(word):
    result = []
    for i in word:
        if i not in result:
            result.append(i)
    return ''.join(result)
            