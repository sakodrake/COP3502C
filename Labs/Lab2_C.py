unit_from =  input("Enter the unit you are converting from: ")
unit_to = input("Enter the unit you are converting to: ")
enter_temp = float(input(f"Enter the temperature in {unit_from}: "))

if unit_from ==  "Fahrenheit" and unit_to == "Celsius":
    final = (enter_temp - 32) * (5/9)
    print(f"That is {final:.1f} degrees Celsius.")
elif unit_from =="Fahrenheit" and unit_to == "Kelvin":
    final = ((enter_temp - 32) * (5/9)) + 273.15
    print(f"That is {final:.1f} degrees Kelvin.")
elif unit_from == "Fahrenheit" and unit_to == "Fahrenheit":
    print(f"That is {enter_temp} degrees in Fahrenheit.")

if unit_from == "Celsius" and unit_to == "Celsius":
    print(f"That is {enter_temp:.1f} degrees Celsius.")
elif unit_from =="Celsius" and unit_to == "Fahrenheit":
    final = (enter_temp * (9/5)) + 32
    print(f"That is {final:.1f} degrees Fahrenheit.")
elif unit_from == "Celsius" and unit_to == "Kelvin":
    final = enter_temp + 273.15
    print(f"That is {final:.1f} degrees Kelvin.")

if unit_from == "Kelvin" and unit_to == "Fahrenheit":
    final = (enter_temp - 273.15) * (9/5) + 32
    print(f"That is {final:.1f} degrees Fahrenheit.")
elif unit_from =="Kelvin" and unit_to == "Celsius":
    final = enter_temp - 273.15
    print(f"That is {final:.1f} degrees Celsius.")
elif unit_from == "Kelvin" and unit_to == "Kelvin":
    print(f"That is {enter_temp:.1f} degrees Kelvin.")
