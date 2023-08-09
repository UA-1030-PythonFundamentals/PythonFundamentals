from random import choice


class Ghost(object):
    __color = ["white", "yellow", "purple", "red"]

    def __init__(self):
        self.color = choice(Ghost.__color)
