from flask import Flask, render_template, url_for, flash, redirect
from forms import RegistrationForm, LoginForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'be9e99d0f713db9e947de2831ae8864c'

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

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()

    if form.validate_on_submit():
        flash(f'Account created for {form.userName.data}!', category="success")
        return redirect(url_for('home'))

    return render_template("register.html", title="Register", form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()

    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'password':
            flash('You have been logged in!', 'success')
            return redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check username and password', 'danger')
    return render_template("login.html", title="Login", form=form)