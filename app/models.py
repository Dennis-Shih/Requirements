from app import db

class User(db.Model):

    id=db.Column(db.Integer, primary_key=True)
    author=db.Column(db.String(70), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.author}>'

#Task has a title and description
class Task(db.Model):
    #description of a task can be left empty when creating one
    id=db.Column(db.Integer, primary_key=True)
    title=db.Column(db.String(70), unique=True, nullable=False)
    description=db.Column(db.String(70), unique=False, nullable=True)
    def __repr__(self):
        return f'<Task {self.title}>'



db.create_all()
