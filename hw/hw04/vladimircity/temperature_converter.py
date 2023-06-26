celsius = float(input('Enter the temperature in °C: '))

if celsius < -273.15:
    print('Error: Temperature below absolute zero (-273.15°C)')
else:
    fahrenheit = round(celsius * 9/5 + 32, 2)
    print(f'{celsius}°C is equivalent to {fahrenheit}°F')