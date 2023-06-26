c = float(input("Enter a temperature in Celsius:\n"))

f = (c * 9/5) + 32

if c > -273.15:
    print(f"You enter: {c}°C ")
    print(f"{c}°C is equivalent to {f}°F")
else:
    print(f"You enter: {c}°C ")
    print("Temperature below absolute zero (-273.15°C)")