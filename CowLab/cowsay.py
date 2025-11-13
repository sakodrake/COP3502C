import sys
import heifer_generator 
from dragon import Dragon
# from ice_dragon import IceDragon

def list_cows():
    cows = heifer_generator.get_cows()
    for c in cows:
        print(c.get_name(), end=" ")

def find_cow(name):
    cows = heifer_generator.get_cows()
    for c in cows:
        if c.get_name() == name:
            return c
    return None
    
args = sys.argv [1:]

if args[0] == "-l":
    print("Cows available: ", end = "")
    list_cows()
elif args[0] == "-n":
    cow_name = args[1]
    cow = find_cow(cow_name)
    message = " ".join(args[2:])
    if cow == None:
        print(f"Could not find {cow_name} cow!")
    else:
        print(message)
        print(cow.get_image())
        if isinstance(cow, Dragon):
            if cow.can_breath_fire():
                print("This dragon can breathe fire.")
            else:
                print("This dragon cannot breathe fire.")
else:
    message = " ".join(args)
    cows = heifer_generator.get_cows()
    default_cow = cows[0]
    print(message)
    print(default_cow.get_image())

    
