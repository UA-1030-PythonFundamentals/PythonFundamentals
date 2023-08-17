import re

def change_class_name(old_class_name, new_class_name):
    if not re.match(r'^[A-Z][A-Za-z0-9]*$', new_class_name):
        raise ValueError("Invalid class name. Class names must start with an uppercase letter and contain only alphanumeric characters.")

    old_class = globals()[old_class_name]

    if globals().get(new_class_name):
        raise ValueError(f"Class name '{new_class_name}' is already defined in the global namespace.")

    new_class = type(new_class_name, old_class.__bases__, dict(old_class.__dict__))

    globals()[new_class_name] = new_class

    del globals()[old_class_name]

    return new_class

