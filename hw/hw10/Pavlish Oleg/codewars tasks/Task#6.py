def class_name_changer(cls, new_name):
    if new_name[0].isupper() and new_name.isalnum():
        cls.__name__=new_name
    else:
        raise Exception("HERE IS ERROR MY BRUDA :)))))))))))))))))))))))))))))")