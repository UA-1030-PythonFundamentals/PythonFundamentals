class Human:
    def __init__(self, name):
        self.name = name

    def Hello(self):
        print(f"Hello {self.name}")

    def information(self):
        print(f"{self.name} is a species of 'Homosapiens'")

    @staticmethod
    def arbitrary(message):
        print(f"This is arbitrary message {message}")


h = Human("Vlad")
h.Hello()
h.information()
h.arbitrary('message')
