import re


def class_name_changer(cls, new_name):
    if re.match(r'^[A-Z][a-zA-Z0-9-_]*$', new_name):
        cls.__name__ = new_name
    else:
        raise Exception('Invalid Class Name')


class MyClass:
    pass


class_name_changer(MyClass, "NewClass")

print(MyClass.__name__)
