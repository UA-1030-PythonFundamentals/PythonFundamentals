
def greeting(name):
    if name.lower() == "johnny":
        return f"Hello, dearJ {name.capitalize()}!"
    else:
        return f"Hello, {name.capitalize()}!"

def main():
    user_name = input("Enter your name: ")
    result = greeting(user_name)
    print(result)

if __name__ == "__main__":
    main()

