import random


class Ghost(object):
    arr = ['white', 'yellow', 'purple', 'red']

    def __init__(self):
        self.color = random.choice(Ghost.arr)
