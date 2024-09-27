conv_type = input("Celsius to Fahrenheit or Fahrenheit to Celsius?\n"
                  "(Input 'F' for Fahrenheit or 'C' for Celsius): ").strip().lower()
temp = float(input("Input a temperature: "))

if conv_type in ("c", "celsius"):
    answer = (temp * 9/5) + 32  # Correct formula for Celsius to Fahrenheit
    print(f"{temp}°C is {answer}°F.")
elif conv_type in ("f", "fahrenheit"):
    answer = (temp - 32) * 5/9  # Correct formula for Fahrenheit to Celsius
    print(f"{temp}°F is {answer}°C.")
else:
    print("What you doing? That ain't the right input.")
