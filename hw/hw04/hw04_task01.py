celsius_input = float(input("Enter the temperature in Celsius: "))

if celsius_input < -273.15:
    print("Critical temperature: Temperature below absolute zero (-273.15°C or −459,67 °F)")
else:
    temperature_converted = (celsius_input * 9/5) + 32
    print(f"{celsius_input}°C is equivalent to {temperature_converted}°F")
