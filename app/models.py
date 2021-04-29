from app import db

class User(db.Model):

    id=db.Column(db.Integer, primary_key=True)
    author=db.Column(db.String(70), unique=True, nullable=False)

    def __repr__(self):
        return f'<User {self.author}>'



db.create_all()
