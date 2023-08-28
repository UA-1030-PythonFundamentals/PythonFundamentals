import json

file_cars = open("cars.json", "r")
file_cars2 = open("cars2.json", "r")
result_file = open("result.json", "w")
cars_data = json.load(file_cars)
cars2_data = json.load(file_cars2)
cars_data.append(cars2_data)
sorted_cars = sorted(cars_data, key=lambda car: car['max_speed'])
json.dump(sorted_cars, result_file)
file_cars.close()
file_cars2.close()
result_file.close()