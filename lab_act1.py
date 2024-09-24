temp = float(input("Input a temperature."))
conv_type = input("Celsius to Fahrenheit or Fahrenheit to Celsius")

if conv_type == ("Celsius" or "Cel" or "c"):
    answer = (9/5 * temp) - 32
    print(answer)