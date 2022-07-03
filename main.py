from flask import Flask, render_template, url_for

app = Flask(__name__)

menu = ["Установка", "Первое приложение", "Обратная связь"]


@app.route("/index")
@app.route("/")
def index():
    return render_template("index.html", title='Index', menu=menu)


@app.route("/about")
def about():
    return render_template("about.html", title="About")


@app.route("/profile/<username>")
def profile(username):
    return f"Пользователь: {username}"

with app.test_request_context():
    print(url_for('index'))
    print(url_for('about'))
    print(url_for('profile', username="selfedu"))


if __name__ == "__main__":
    app.run(debug=True)
