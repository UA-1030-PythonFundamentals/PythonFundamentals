from flask import Flask, url_for, request

my_app = Flask(__name__)


@my_app.route('/')
def hello_world():
    return "Method used: %s" % request.method

@my_app.route("/check_method", methods=['GET', 'POST'])
def check_method():
    if request.method == 'POST':
        return "You are using POST"
    else:
        return "You are probably using GET"
@my_app.route("/name")
def get_name():
    return "liubomyr"


@my_app.route("/<name>")
def get_custom_name(name: str):
    return name.capitalize()


@my_app.route("/<name>/<int:age>")
def get_CV(name: str, age):
    return f"My name is {name.capitalize()}, age: {age}"


if __name__ == '__main__':
    # my_app.run(host="0.0.0.0", port=80)
    my_app.run()
