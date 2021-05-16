import os

from flask_sqlalchemy import SQLAlchemy

from flask_login import LoginManager
# include Flask class from file flask
from flask import Flask


# for the location of the current file, what is its directory
basedir = os.path.abspath(os.path.dirname(__file__))

# create an instance of Flask class
# __name__ is a predefined setup variable
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY = 'you-will-never-guess',
    # location of database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS = False
)

db = SQLAlchemy()
db.init_app(app)

login = LoginManager()
login.init_app(app)
login.login_view=login

from app import routes, models

if __name__ == '__main__':
    db.create_all()
    app.run(host="0.0.0.0", port=port)
