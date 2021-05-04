from app import db

class User(db.Model):

    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(70), unique=True, index=True, nullable=False)
    password=db.Column(db.String(70), nullable=False)
    def __repr__(self):
        return f'<User {self.name}>'

#Task has a title and description
class Task(db.Model):
    #description of a task can be left empty when creating one
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(70), unique=True, nullable=False)
    desc=db.Column(db.String(70), unique=False, nullable=True)
    ispriority=db.Column(db.Boolean, nullable=True)
    def __repr__(self):
        return f'<Task {self.title}>'

db.create_all()
