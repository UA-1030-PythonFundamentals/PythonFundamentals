import json

file_cars = open("cars.json", "r")
file_cars2 = open("cars2.json", "r")
result_file = open("result.json", "w")
cars = json.load(file_cars)
cars2 = json.load(file_cars2)
cars.append(cars2)
cars_sorted = sorted(cars, key=lambda d: d['max_speed'])
json.dump(cars_sorted, result_file)

for file in [file_cars, file_cars2, result_file]:
    file.close()
