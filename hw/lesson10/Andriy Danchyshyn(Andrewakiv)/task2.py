class Human:
    def __init__(self, name):
        self.name = name

    def hello(self):
        return f'Hello, {self.name}'

    @classmethod
    def species(cls):
        return 'This is a species of Homosapiens'

    @staticmethod
    def any_method():
        return 'Static method from this class'


h = Human('Andriy')
print(h.hello())
print(Human.species())
print(Human.any_method(), h.any_method())
