type_of_calculation = input("What type do you want to solve (Voltage, Current, or Resistance)? ").strip().lower()

if type_of_calculation == "voltage":
    current = float(input("What is your Current (I) in Amperes? "))
    resistance = float(input("What is your Resistance (R) in Ohms? "))

    voltage = current * resistance
    print(f"Voltage (V) = {voltage} Volts")

elif type_of_calculation == "current":
    voltage = float(input("What is your Voltage (V) in Volts? "))
    resistance = float(input("What is your Resistance (R) in Ohms? "))

    current = voltage / resistance  # Correct formula for Current
    print(f"Current (I) = {current} Amperes")

elif type_of_calculation == "resistance":
    voltage = float(input("What is your Voltage (V) in Volts? "))
    current = float(input("What is your Current (I) in Amperes? "))

    resistance = voltage / current  # Correct formula for Resistance
    print(f"Resistance (R) = {resistance} Ohms")

else:
    print("Invalid input! Please enter Voltage, Current, or Resistance.")
