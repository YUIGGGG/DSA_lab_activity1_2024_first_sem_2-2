temp = float(input("Input a temperature."))
conv_type = input("Celsius to Fahrenheit or Fahrenheit to Celsius")

if conv_type in ("Celsius" or "Cel" or "c"):
    answer = (9/5 * temp) - 32
    print(answer)
elif conv_type in ("Fahrenheit" or "F"):
    answer = (temp - 32) * 5/9
    print(answer)
else:
    print("What you doin', that ain't the right input.")
