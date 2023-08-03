class Human:
    def __init__(self, name):
        self.name = name

    def greetings(self):
        return f"Hello, {self.name}, welcome!"

    @classmethod
    def homo(cls):
        return "You are \"Homosapiens\"."

    @staticmethod
    def mesage():
        return "I don't understand, why we need use that methods."
    
man = Human(input("Enter your name:\n"))
print(man.greetings())
print(man.homo())
print(man.mesage())