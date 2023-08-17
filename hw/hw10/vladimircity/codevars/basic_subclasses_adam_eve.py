class Human:
    def __init__(self, name):
        self.name = name


class Man(Human):
    def __init__(self, name):
        super().__init__(name)


class Woman(Human):
    def __init__(self, name):
        super().__init__(name)


def God():
    return [Man("Adam"), Woman("Eve")]


paradise = God()

print(paradise[0].name)
print(paradise[1].name)
