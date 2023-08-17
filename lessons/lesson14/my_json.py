import json

x = '{ "name":"Liubov", "age":25, "city":"Lviv"}' # some JSON
y = json.loads(x) # parse x
print("Data from JSON: ", y)
print(type(y)) # the result is a Python dictionary
print("Age: ", y["age"])
from pprint import pprint
with open("data.json") as file:
    data = json.load(file)
    pprint(data, indent=3)
print(data.get("hobbies"))


class A():
    def __str__(self):
        return "test"

a = A()
d = {
    a.__str__(): 10,
    "a": "a",
    100:100
}
print(json.dumps(d))