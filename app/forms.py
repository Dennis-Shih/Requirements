from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, IntegerField
from wtforms.validators import DataRequired

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    submit = SubmitField('Sign In')

class RegisterForm(FlaskForm):
    username = StringField('Set Username',validators=[DataRequired()])
    password = PasswordField('Set Password', validators=[DataRequired()])
    confirmpass = PasswordField('Confirm Password', validators=[DataRequired()])

    submit = SubmitField('Register')

class CreateTaskForm(FlaskForm):
    title = StringField('Task name',validators=[DataRequired()])
    desc = StringField('Task Description')
    ispriority=BooleanField('Set as Priority?')
    submit = SubmitField('Create task')
