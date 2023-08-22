class InputError(Exception):
    def __init__(self, data):
        self.data = data


def check(text):
    if type(text) is not str:
        raise InputError("Type text error")
    elif len(text) < 3:
        raise InputError("Short text error")
    elif len(text) > 15:
        raise InputError("Long text error")

    else:
        return True