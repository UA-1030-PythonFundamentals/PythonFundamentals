celsium = int(input("Enter a temperature in Celsium: "))
fahrenheit = None

if celsium < -273.15:
    print("Error: Temperature below absolute zero (-273.15 °С)")
else:
    fahrenheit = (celsium * 9 / 5) + 32
    print(f"{celsium} °С is equivalent to {fahrenheit} °F")