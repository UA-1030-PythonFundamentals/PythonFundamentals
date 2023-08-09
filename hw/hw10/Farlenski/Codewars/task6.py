def class_name_changer(cls, new_name):
    if new_name[0].isupper() and new_name.isalnum():
        cls.__name__ = new_name
    else:
        raise Exception("Invalid class name. "
                        "Class names must start with an uppercase letter and contain only alphanumeric characters.")

class Func:
    pass

check = Func()
class_name_changer(Func, "UsefulClass")
print(Func.__name__)