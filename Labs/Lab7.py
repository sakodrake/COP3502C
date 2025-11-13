"""
PROBLEM 1
"""

#thoughts: i want to take the values of "type" and put them into a set so they dont have duplicates, then make those keys in a dictionary. then i want to add a 
#dictionary to each of those keys... 

# additionally, the original data is stored as a list. 

def reformat(data):
    result = {}
    for item in data:
        item_type = item["type"] 
        item_name = item["name"]
        item_price = item["price"]

        if item_type not in result:
            result[item_type] = {}
        
        result[item_type][item_name] = item_price
    return result

"""
PROBLEM 2
"""
# i can't use loops so i have to find a way to use recursion.
# maybe i can turn it into a list and then delete "n" indexes and return index 0 of the list...
def nth(data,n):
    if n == 0:
        return data[0]
    if data == None:
        return None
    
    return nth(data[1], n - 1)

"""
PROBLEM 3
"""

def where(data):
    if type(data) == str:
        return 1 if data == "Waldo" else 0
    
    elif type(data) == list:
        if not data:
            return 0 
        return where(data[0]) + where(data[1:])
    
    elif type(data) == dict:
        count = 0
        for key, value in data.items():
            count += where(key)
            count += where(value)
        return count
    
    else:
        return 0


    
    






    
    

