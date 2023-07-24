class Animal:
    def __init__(self, name, species, number_of_legs):
        self.name = name
        self.species = species
        self.legs = number_of_legs

    def make_sound(self):
        return "Animal noise"


class Mammal(Animal):
    def __init__(self, name, species, number_of_legs):
        super().__init__(name, species, number_of_legs)

    def give_birth(self):
        pass

    def make_sound(self):
        return "Roar"


class Bird(Animal):
    def __init__(self, name, species, number_of_legs):
        super().__init__(name, species, number_of_legs)

    def lay_eggs(self):
        pass

    def make_sound(self):
        return "Squawk"


class Reptile(Animal):
    def __init__(self, name, species, number_of_legs):
        super().__init__(name, species, number_of_legs)

    def shed_skin(self):
        pass

    def make_sound(self):
        return "Hiss"


if __name__ == '__main__':

    animals = [Mammal("Lion", "Mammal", 4),
               Bird("Falcon", "Bird", 2),
               Reptile("Python", "Reptile", 4)]

    for animal in animals:
        print(f"Animal: {animal.name}, "
              f"Species: {animal.species}, "
              f"Legs: {animal.legs}, "
              f"Sound: {animal.make_sound()}")
