from flask import render_template, redirect

from app import app
from app import db
from app.forms import LoginForm, RegisterForm
from app.models import User

@app.route('/')
@app.route('/index.html')

def index():
    return "Index!"

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        print("placehold")
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])

def register():
    form=RegisterForm()
    return render_template('register.html', form=form)

