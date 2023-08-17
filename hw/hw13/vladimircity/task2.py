def add_tag(tag):
    def decorator(func):
        def wrapper():
            return f'{tag}{func()}{tag}'
        return wrapper
    return decorator




@add_tag("<strong>")
def get_message():
    return "Hello, World!"

print(get_message())