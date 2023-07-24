class Human:
    def __init__(self, name):
        self.name = name

    def welcome_message(self):
        print(f"Welcome, {self.name}!")

    @classmethod
    def species(cls):
        return "Homosapiens"

    @staticmethod
    def arbitrary_message():
        return "This is an arbitrary message."


human = Human("Mary")

human.welcome_message()
print(Human.species())
print(Human.arbitrary_message())

