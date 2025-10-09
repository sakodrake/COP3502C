def parse_student(data):
    id = int(data[:8])
    birth_month = data[-4:-2]
    birth_year = data[-2:]
    name = data[8:-4]
    
    return {
        "id": id,
        "name": name, 
        "birthdate": f"{birth_month}/{birth_year}"
    }

def count_items(list):
    counts = {}
    for val in list:
        if val in counts:
            counts[val] += 1
        else:
            counts[val] = 1
    return counts

def list_fighters(battle_data):
    fighters = set()

    for name, results in battle_data.items():
        fighters.add(name)
        fighters.update(results["win"])
        fighters.update(results["loss"])

    fighters = list(fighters)
    fighters.sort()
        
    return fighters 
    