money = int(input("How much money do you have: "))
candy = money // 4

wrappers = candy 

while wrappers >= 3:
    extra = wrappers // 3
    candy += extra
    wrappers = wrappers % 3 + extra

print(f"You can purchase {candy} candy bars!")