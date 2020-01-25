from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.config['SECRET_KEY'] = '526669b03620e2ed8bb3a81010d8'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db  = SQLAlchemy(app)
bcrypt = Bcrypt(app)

from flaskblog import routes