from flask import render_template, redirect

from app import app
from app import db
from app.forms import LoginForm
from app.models import User

@app.route('/')
@app.route('/index.html')
def index():
    return "Index!"

@app.route('/login')
def login():
    form=LoginForm()
    return render_template('login.html', form=form)
@app.route('/register')
def register():
    return "<h1>Stick register stuff here</h1>"

