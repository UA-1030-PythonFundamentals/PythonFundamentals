class Human:
    typ='Homosapiens'
    def __init__(self, name):
        self.name=name

    def hello_message(self):
        print(f'Hi, {self.name}!')

    def show_inf(typ):
        return f'This is a {typ}'

    def __str__(self, typ=typ):
        return f'INFO: Type - {typ}, Name - {self.name}'
#Human Bob
Human.show_inf=staticmethod(Human.show_inf)
human_Bob=Human('Bob')
human_Bob.hello_message()
print(human_Bob.show_inf(Human.typ))
print(human_Bob)
print('        NEXT              ')
#Human Jo
human_Jo=Human('Jo')
human_Jo.hello_message()
print(human_Jo.show_inf(Human.typ))
print(human_Jo)