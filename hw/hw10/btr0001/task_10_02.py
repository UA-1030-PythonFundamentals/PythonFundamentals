class Human:

    def __init__(self, name):
        self.name = name

    def greeting(self):
        print(f'Hello {self.name}')

    def info(self):
        print(f'{self.name} is a species of "Homosapiens"')

    @staticmethod
    def arbitrary(mess):
        print(f'This is an arbitrary message: {mess}')


h = Human('Петро')

h.greeting()
h.info()
h.arbitrary('просто повідомлення')