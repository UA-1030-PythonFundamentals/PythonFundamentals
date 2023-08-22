def add_tag(tag):
    def decorator(func):
        m = func()
        def wrapper():
            tagged_text = f"{tag}{m}{tag}"
            return tagged_text
        return wrapper
    return decorator