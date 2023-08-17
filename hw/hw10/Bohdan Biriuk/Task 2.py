class Human:
    def __init__(self, name):
        self.name = name


    def welcome_massage(self):
        return(f"Hello {self.name}, nice to meet you)")

    def homo(self):
        return(f"This is {self.name}, species of homosapiens")

    @staticmethod
    def st():
        return ("How are you?")






a = Human("Dan")
a1 = a.welcome_massage()
print(a1)
a1 = a.homo()
print(a1)
a1 = a.st()
print(a1)