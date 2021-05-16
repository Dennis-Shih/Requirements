from app import db
from werkzeug.security import generate_password_hash, check_password_hash
from app import login
from flask_login import UserMixin

class User(UserMixin, db.Model):

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(70), unique=True, index=True, nullable=False)
    password=db.Column(db.String(300), nullable=False)
    def set_password(self, password):
        self.password=generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)
    def __repr__(self):
        return f'<User {self.name}>'

#Task has a title and description
class Task(db.Model):
    #description of a task can be left empty when creating one
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(70), unique=True, nullable=False)
    desc=db.Column(db.String(70), unique=False, nullable=True)
    ispriority=db.Column(db.Boolean, nullable=True)
    collab = db.Column(db.String(70), unique=False, nullable=True)
    def __repr__(self):
        return f'<Task {self.title}>'
'''
@login.user_loader
def load_user(id):
    return User.get(id)
'''
@login.user_loader
def load_user(id):
    return User.query.get(int(id))
