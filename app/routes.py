from flask import render_template, redirect, flash, url_for, request, session
from app import app
from app import db
from app.forms import ListForm,LoginForm, RegisterForm, CreateTaskForm, TaskForm,createTask
from app.forms import HomeForm
from app.models import User, Task, Collab
from datetime import datetime, date
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
            return redirect(url_for('list'))
        elif request.form.get('login', False):
            return redirect(url_for('login'))
        #Only appears if user is logged in
        elif request.form.get('logout', False):
            return redirect(url_for('logout'))
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
        new_task = None
        t=Task.query.filter_by(title=form.title.data).first()
        if t is not None:
            exists=True
            flash('Task already exists under that name')
            return redirect(url_for('newtask'))
        #convert string to datetime
        try:
            format = "%Y/%m/%d"
            deadlineToDate = datetime.now()
            if form.deadline.data:
                deadlineToDate = datetime.strptime(form.deadline.data, format)

            new_task=Task(title=form.title.data,desc=form.desc.data,ispriority=form.ispriority.data, deadline=deadlineToDate)

        except:
            print("Incorrect format. Please enter deadline in yyyy/mm/dd format")


        flash(form.ispriority.data)

        db.session.add(new_task)
        db.session.commit()

        return redirect(url_for('list'))

    return render_template('newtask.html', form=form)

@app.route('/task/<int:id>', methods=['GET', 'POST'])
def task(id):
    task=Task.query.filter_by(id=id).first()
    form = TaskForm(title=task.title, desc=task.desc, ispriority=task.ispriority, deadline=task.deadline)

    if 'Save' in request.form:
        if (form.title.data == ''):
            flash("Name cannot be empty!")
            return redirect(url_for('task', id=id))
        #maybe stick function here with these param assignments
        task.title=form.title.data
        task.desc=form.desc.data
        task.ispriority=form.ispriority.data
        format = "%Y-%m-%d"
        deadlineToDate = datetime.now()
        if form.deadline.data:
            deadlineToDate = datetime.strptime(form.deadline.data, format)
            task.deadline=deadlineToDate
        

        if form.collab.data != '':
            u=User.query.filter_by(username=form.collab.data).first()
            #if collaborator is not an existing user
            if u is None:
            	flash('Cannot find user of that name')
            	return redirect(url_for('task', id=id))

            #if collaborator is not already collaborator
            c=Collab.query.filter_by(name=form.collab.data).first()
            if c is None:
            	new_collab=Collab(name=form.collab.data)
            	db.session.add(new_collab)
            	
        

        db.session.add(task)
        db.session.commit()
        return redirect(url_for('list'))

    if request.form.get('makeCopy'):
    	copy=Task(title=form.title.data, desc=task.desc, ispriority=task.ispriority)
    	copy.title='Copy of ' +form.title.data
    	db.session.add(copy)
    	db.session.commit()
    	flash('Successfully copied')
    	return redirect(url_for('list'))
    	
    if request.form.get('deleteTask'):
        db.session.delete(task)
        db.session.commit()
        return redirect(url_for('deleteTask',id=id))
    	
    return render_template('task.html', form=form)

@app.route('/deleteTask/<int:id>')
def deleteTask(id):
    
    return render_template('deleted_task.html', deletedtask=task)

#lists all the existing tasks
@app.route('/tasklist', methods=['GET','POST'])
def list():
    form =createTask()
    list=Task.query.all()
    if form.validate_on_submit():
        if request.form.get('createTask'):
            return redirect(url_for('newtask'))

    return render_template('list.html', all_tasks=list,form=form)

