celsius = int(input('Enter the temperature in Celsius: '))
print('Temperature below absolute zero (-273.15°C)' if celsius < -273.15 else \
          f'{celsius}°C is equivalent to {int((celsius * 9/5) + 32)}°F')
