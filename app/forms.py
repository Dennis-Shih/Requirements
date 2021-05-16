from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username')
    password = PasswordField('Password')

    login = SubmitField('Sign In')
    register = SubmitField('Need an account?')
    home = SubmitField('Return to home')
class RegisterForm(FlaskForm):
    username = StringField('Set Username')
    password = PasswordField('Set Password', validators=[DataRequired()])
    confirmpass = PasswordField('Confirm Password', validators=[DataRequired()])

    register = SubmitField('Register')

class CreateTaskForm(FlaskForm):
    title = StringField('Task name',validators=[DataRequired()])
    desc = StringField('Task Description')
    ispriority=BooleanField('Set as Priority?')
    submit = SubmitField('Create task')

class TaskForm(FlaskForm):
    title = StringField('Task name',validators=[DataRequired()])
    desc = StringField('Task Description')
    ispriority=BooleanField('Set as Priority?')
    save = SubmitField('Save task')
    collab = StringField('Collaborator(s)')

#ONLY SHOW LOGIN BUTTON IF NOT LOGGED IN
class HomeForm(FlaskForm):
    #if not logged in, the 'view tasks' should redirect to login page
    viewTasks = SubmitField('View tasks')
    login = SubmitField('Login')
    register = SubmitField('Register')
    logout = SubmitField('Logout')
class ListForm(FlaskForm):
    createTask=SubmitField('New task')
    edit=SubmitField('Edit')
