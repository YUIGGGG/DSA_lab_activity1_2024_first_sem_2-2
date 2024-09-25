type = input("What type do you wanna solve")
if type == ("Voltage"):
    current = float(input("What is your Current(I)?"))
    resistance = float(input("What is your resistance(R)?"))

    voltage = current * resistance
    print(f"{voltage}")

elif type == ("Current"):
    voltage = float(input("What is your Voltage(V)?"))
    resistance = float(input("What is your resistance(R)?"))

    current = voltage * resistance
    print(f"{current}")

elif type == ("Resistance"):
    voltage = float(input("What is your voltage(v)? "))
    current = float(input("What is your current(I)? "))

    resistance = voltage * current
    print(f"{resistance}")

else:
    print("ValueError!")