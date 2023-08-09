class Human:
    def __init__(self, name):
        self.__name = name

    def greeting(self):
        print(f"Welcome, {self.__name}")

    def species(self):
        print("You are a Homosapiens")

    @staticmethod
    def arbitrary():
        print("Static method")

human = Human("Nick")
human.greeting()
human.species()
human.arbitrary()
