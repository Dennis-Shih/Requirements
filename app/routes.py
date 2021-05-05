from flask import render_template, redirect, flash
from app import app
from app import db
from app.forms import LoginForm, RegisterForm, CreateTaskForm
from app.models import User, Task

from flask_login import current_user, login_user, logout_user
from flask_login import LoginManager
from flask_login import login_required

@app.route('/')
@app.route('/index.html')
def index():
    return render_template('home.html')

#logs the user in when they type in a username and password
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        the_user = User.query.filter_by(name=form.username.data).first()
        if the_user is None or not the_user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect('/login')
        #if login works
        login_user(the_user)
        return redirect('/')

    return render_template('login.html', title='Login', form=form)

    '''form=LoginForm()

    if form.validate_on_submit():

        exists = False

        users =User.query.all()
        print(users)
        the_user = None
        for u in users:
            print(u.name)
            #reminder to self: form.username.data is the string for name, not form.username
            if u.name == form.username.data:
                exists=True
                the_user=u
                return redirect('/')
        if not exists:
            flash('User {} does not exist.'.format(
            form.username.data))
    return render_template('login.html', form=form)'''

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect('/')

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
            new_user.set_password(form.password.data)
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
            priority=False
            if form.ispriority(): priority=True
            new_task=Task(title=form.title.data,desc=form.desc.data,ispriority=priority)
            db.session.add(new_task)
            db.session.commit()
            return redirect('/tasklist')
    return render_template('newtask.html', form=form)

@app.route('/task', methods=['GET', 'POST'])
def task():
    form = TaskForm()
    if 'Save' in request.form:
        db.session.add(form)
        db.session.commit()
    return render_template('task.html', form=form)

#lists all the existing tasks
@app.route('/tasklist')
def list():
    list=Task.query.all()
    return render_template('list.html', all_tasks=list)

