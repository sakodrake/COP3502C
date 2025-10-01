total_income = float(input("Enter your total income this year: "))

if total_income <= 11600:
    final = total_income * 0.10
    print(f"You owe ${final:.2f} this year.")

elif total_income <= 47150:
    final = (11600 * 0.10) + ((total_income - 11600) * 0.12)
    print(f"You owe ${final:.2f} this year.")

elif total_income <= 100525:
    final = (11600 * 0.10) + ((47150 - 11600) * 0.12) + ((total_income - 47150) * 0.22)
    print(f"You owe ${final:.2f} this year.")

elif total_income <= 191950:
    final = (11600 * 0.10) + ((47150 - 11600) * 0.12) + ((100525 - 47150) * 0.22) + ((total_income - 100525) * 0.24)
    print(f"You owe ${final:.2f} this year.")

elif total_income <= 243725:
    final = (11600 * 0.10) + ((47150 - 11600) * 0.12) + ((100525 - 47150) * 0.22) + ((191950 - 100525) * 0.24) + ((total_income - 191950) * 0.32)
    print(f"You owe ${final:.2f} this year.")

elif total_income <= 609350:
    final = (11600 * 0.10) + ((47150 - 11600) * 0.12) + ((100525 - 47150) * 0.22) + ((191950 - 100525) * 0.24) + ((243725 - 191950) * 0.32) + ((total_income - 243725) * 0.35)
    print(f"You owe ${final:.2f} this year.")

else:
    final = (11600 * 0.10) + ((47150 - 11600) * 0.12) + ((100525 - 47150) * 0.22) + ((191950 - 100525) * 0.24) + ((243725 - 191950) * 0.32) + ((609350 - 243725) * 0.35) + ((total_income - 609350) * 0.37)
    print(f"You owe ${final:.2f} this year.")
