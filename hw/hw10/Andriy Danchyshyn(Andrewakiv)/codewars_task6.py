def class_name_changer(cls, new_name: str):
    if new_name.isalnum() and new_name[0].isupper():
        cls.__name__ = new_name
    else:
        raise ValueError('Invalid name')
