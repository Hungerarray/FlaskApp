from flask import Flask, render_template

app = Flask(__name__)

posts = [
    {
        "author": "Kata Feliciano",
        "title": "Silent Theft",
        "content": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Molestias, culpa accusantium nam ipsa cum sapiente.",
        "date": "April 5, 2020"
    },
    {
        "author": "Laura Rizwan",
        "title": "Elves of kiss",
        "content": "Lorem ipsum dolor, sit amet consectetur adipisicing elit. Molestias, culpa accusantium nam ipsa cum sapiente.",
        "date": "June 10, 2020"
    }
]


@app.route("/home")
@app.route("/")
def home():
    return render_template("home.html", posts=posts)


@app.route("/about")
def about():
    return render_template("about.html", title="about")
