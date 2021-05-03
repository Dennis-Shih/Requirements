from flask import render_template, redirect, flash

from app import app
from app import db
from app.forms import LoginForm, RegisterForm
from app.models import User

@app.route('/')
@app.route('/index.html')
def index():
    return "Home"

@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        flash('Login requested for user {}'.format(
        form.username.data))
        return redirect('/')
    return render_template('login.html', form=form)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegisterForm()
    return render_template('register.html', form=form)

@app.route("/logout")
def logout():
    flash('logout')
