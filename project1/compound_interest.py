initial_principal = float(input("Initial principle1: "))
interest_rate = float(input("Interest rate: ")) * 0.01
num_appliedperyear = float(input("How many times does interest apply annually: "))
years_past = float(input("How many years have passed: "))

compund_interest = initial_principal * ((1 + (interest_rate/num_appliedperyear))**(num_appliedperyear*years_past))

print(f"You now have ${compund_interest:.2f}")
