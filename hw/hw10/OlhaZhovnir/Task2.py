class Human:
    species = "Homosapience"
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"Welcome {self.name}"

    @staticmethod
    def staticmethod():
        return "Arbitrary message"
    @classmethod
    def show_species(cls):
        print("It is a species of",cls.species)


Human.show_species()