from flask import render_template, redirect, flash

from app import app
from app import db
from app.forms import LoginForm, RegisterForm
from app.models import User

@app.route('/')
@app.route('/index.html')
def index():
    return "Home"

#logs the user in when they type in a username and password
@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()
    if form.validate_on_submit():
        '''Check that the user exists,
         show user error message if account doesnt exist'''
        #flash('Login requested for user {}'.format(
        #form.username.data, form.password.data))

        exists = False

        users =User.query.all()
        the_user = None
        for u in users:
            if u.author == form.author:
                exists=true
                the_user=u
                return redirect('/')
        if not exists:
            flash('User {} does not exist.'.format(
            form.username.data, form.password.data))
    return render_template('login.html', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegisterForm()
    #this should create new user if name available then redirect to home page
    if form.validate_on_submit():
        flash('Register user {}','Password {}','Confirm password {}'.format(
        form.username.data, form.password.data, form.confirmpass.data))
        return redirect('/')

    return render_template('register.html', form=form)


@app.route("/logout")
def logout():
    flash('logout')
