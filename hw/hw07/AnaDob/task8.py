def can_reach_pump(distance, fuel_left, mpg=25):
    max_distance = fuel_left * mpg
    return max_distance >= distance
distance = 50
fuel_left = 2
print(can_reach_pump(distance, fuel_left)) 
