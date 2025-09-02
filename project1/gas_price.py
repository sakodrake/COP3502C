
gas_capacity = float(input("How big is your car's gas tank: "))
gas_current = float(input("How many gallons are in your tank now: "))
gas_price = float(input("What is the price of gas per gallon: "))

gas_needed = gas_capacity - gas_current #already an float no need to declare
total_price = gas_needed * gas_price

print(f"Your gas will cost ${total_price:.2f}")