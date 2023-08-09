from flask import Flask, redirect, url_for, request, render_template

app = Flask(__name__)


class User:
    __count = 0

    def __init__(self, name, age, city, gender):
        self.id = self.__get_new_id()
        self.name = name
        self.age = age
        self.city = city
        self.gender = gender

    @classmethod
    def __get_new_id(cls):
        cls.__count += 1
        return cls.__count


USERS = []


@app.route('/')
def index():
    error_msg = request.args.get("error_msg")
    return render_template('home.html', users=USERS, error_msg=error_msg)


@app.route('/user', methods=['GET', 'POST'])
def user():
    if request.method == 'POST':
        data = {
            "name": request.form["name"],
            "age": request.form["age"],
            "city": request.form["city"],
            "gender": request.form["gender"]
        }
        print(data)
        USERS.append(User(**data))
        return redirect(url_for("index"))
    else:
        return render_template('create_user_form.html')
@app.route('/user/<int:user_id>')
def user_delete(user_id):
    for i in range(len(USERS)):
        if USERS[i].id == user_id:
            del USERS[i]
            break
    else:
        return redirect(url_for("index", error_msg=f"user(id:{user_id}) not found"))
    return redirect(url_for("index"))


if __name__ == '__main__':
    USERS = [
        User("Alice", 25, "New York", "Female"),
        User("Bob", 30, "Los Angeles", "Male"),
        User("Eve", 22, "Chicago", "Female"),
        User("Charlie", 28, "San Francisco", "Male"),
        User("Grace", 29, "Seattle", "Female")
    ]
    app.run()
