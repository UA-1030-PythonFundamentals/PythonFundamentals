# Will you make it?

def zero_fuel(distance_to_pump, mpg, fuel_left):
    distance_possible = fuel_left * mpg
    return True if distance_to_pump <= distance_possible else False


print(zero_fuel(100, 50, 1))
print(zero_fuel(50, 25, 2))
