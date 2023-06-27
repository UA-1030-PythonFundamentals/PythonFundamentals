ABS_ZERO = -273.15

temp = float(input("Enter a temperature in Celsius:"))

if temp < ABS_ZERO:
    print(f"Error: Temperature below absolute zero ({ABS_ZERO}\u00b0C)")
else:
    temp_Fahr = (temp * 9 / 5) + 32
    print(f"{temp} is equivalent to {temp_Fahr}\u00b0F")