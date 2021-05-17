from flask import render_template, redirect, flash, url_for, request, session
from app import app
from app import db
from app.forms import ListForm,LoginForm, RegisterForm, CreateTaskForm, TaskForm,createTask
from app.forms import HomeForm
from app.models import User, Task

from flask_login import current_user, login_user, logout_user
from flask_login import LoginManager
from flask_login import login_required
app.secret_key = 'hb0/s?4v\_pxfTN7'

@app.route('/', methods=['GET', 'POST'])
@app.route('/index.html')
def index():
    form = HomeForm()
    if form.validate_on_submit():
        #need 2 buttons, one for login/register and one to 'view tasks'
        if request.form.get('viewTasks', False):
            return redirect('/tasklist')
        elif request.form.get('login', False):
            return redirect('/login')
        #Only appears if user is logged in
        elif request.form.get('logout', False):
            return redirect('/logout')
        elif request.form.get('register', False):
            return redirect(url_for('register'))
    return render_template('home.html', form=form)

#logs the user in when they type in a username and password
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if request.form.get('register', False):
            return redirect(url_for('register'))
        elif request.form.get('login', False):
            '''This checks that the form textfields are not left blank instead 
            of DataRequired, as DataRequired prevents the form from doing anything
            until textfields are filled.'''
            if not request.form.get('username'):
                flash('That field is required.')
                return redirect(url_for('login'))
            #if field is filled, this checks user data with the username entered
            the_user = User.query.filter_by(name=form.username.data).first()
            if the_user is None or not the_user.check_password(form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('login'))
            #if correct username and password, logs in
            login_user(the_user)
            return redirect('/')
        elif request.form.get('home', False):
            return redirect('/')

    return render_template('login.html', title='Login', form=form)

@app.route('/logout')
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
            login_user(new_user)
            return redirect('/')

    return render_template('register.html', form=form)


@app.route('/newtask', methods=['GET', 'POST'])
@login_required
def newtask():
    form=CreateTaskForm()

    if form.validate_on_submit():
        '''Creates new task when title is filled out'''
        exists = False
        tasks =Task.query.all()

        new_task = None
        t=Task.query.filter_by(title=form.title.data).first()
        if t is not None:
            exists=True
            flash('Task already exists under that name')
            return redirect(url_for('newtask'))
        '''if not exists:
            priority=False
            flash (form.ispriority())
            if form.ispriority():
                priority=True
                flash("priority")'''
        new_task=Task(title=form.title.data,desc=form.desc.data,ispriority=form.ispriority.data)
        flash(form.ispriority.data)
        db.session.add(new_task)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('newtask.html', form=form)

@app.route('/task/<int:id>', methods=['GET', 'POST'])
def task(id):
 
    task=Task.query.filter_by(id=id).first()
    form = TaskForm(title=task.title.data, desc=form.desc.data, ispriority=form.priority.data)
    if 'Save' in request.form:
        db.session.add(form)
        db.session.commit()
        return redirect(url_for('list'))
    return render_template('task.html', form=form)

#lists all the existing tasks
@app.route('/tasklist', methods=['GET','POST'])
def list():
    form =createTask()
    list=Task.query.all()
    if form.validate_on_submit():
        if request.form.get('createTask'):
            return redirect(url_for('newtask'))

    return render_template('list.html', all_tasks=list,form=form)

