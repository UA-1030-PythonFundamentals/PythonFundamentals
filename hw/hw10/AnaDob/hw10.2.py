class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        return f"Welcome, {self.name}!"

    @classmethod
    def species_info(cls, name):
        return f"{name} is a species of Homosapiens."

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."

name_input = input("Enter your name: ")
person = Human(name_input)

print(person.welcome_message())
print(Human.species_info(name_input))

print(Human.arbitrary_message())
