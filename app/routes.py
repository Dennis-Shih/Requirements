from flask import render_template, redirect, flash, request, url_for
from app import app
from app import db
from app.forms import LoginForm, RegisterForm, CreateTaskForm, HomeForm
from app.models import User, Task
from flask_login import LoginManager

@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html')
def index():
    form=HomeForm()
    if form.validate_on_submit():
        if request.form.get('login'):
            return redirect(url_for('login'))
        if request.form.get('register'):
            return redirect(url_for('register'))
        if request.form.get('newtask'):
            return redirect(url_for('newtask'))
        if request.form.get('tasklist'):
            return redirect(url_for('list'))
    return render_template('home.html', form=form)

#logs the user in when they type in a username and password
@app.route('/login', methods=['GET', 'POST'])
def login():
    form=LoginForm()

    if form.validate_on_submit():
        '''Check that the user exists (and that they have a correct password),
         show user error message if account doesnt exist'''
        #flash('Login requested for user {}'.format(
        #form.username.data, form.password.data))

        exists = False

        users =User.query.all()
        print(users)
        new_user = None
        for u in users:
            print(u.name)
            #reminder to self: form.username.data is the string for name, not form.username
            if u.name == form.username.data:
                exists=True
                new_user=u
                return redirect('/')
        if not exists:
            flash('User {} does not exist.'.format(
            form.username.data))
    return render_template('login.html', form=form)

@app.route("/logout")
def logout():
    flash('logout placeholder')

@app.route('/register', methods=['GET', 'POST'])
def register():
    form=RegisterForm()


    '''this should create new user if name is available,
    then redirect to home page'''
    if form.validate_on_submit():
        #flash('Register user {}','Password {}','Confirm password {}'.format(
        #form.username.data, form.password.data, form.confirmpass.data))
        exists = False

        users =User.query.all()
        new_user = None
        print(users)

        for u in users:
            print(u.name)
            if u.name == form.username.data:
                exists=True
                flash('Username {} is taken.'.format(
                u.name))

                break

        if not exists:
            new_user=User(name=form.username.data,
            password=form.password.data)
            db.session.add(new_user)
            db.session.commit()
            return redirect('/')

    return render_template('register.html', form=form)

@app.route('/newtask', methods=['GET', 'POST'])
def newtask():
    form=CreateTaskForm()

    if form.validate_on_submit():
        '''Creates new task when title is filled out'''
        exists = False
        tasks =Task.query.all()

        new_task = None
        for t in tasks:
            if t.title == form.title.data:
                exists=True
                flash('Task already exists under that name')
        if not exists:
            new_task=Task(title=form.title.data,desc=form.desc.data)
            db.session.add(new_task)
            db.session.commit()
            return redirect('/tasklist')
    return render_template('newtask.html', form=form)

#lists all the existing tasks
@app.route('/tasklist')
def list():
    list=Task.query.all()
    return render_template('list.html', all_tasks=list)

