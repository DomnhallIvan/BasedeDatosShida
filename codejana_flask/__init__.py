from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app=Flask(__name__)

app.config['SECRET_KEY']='ef1f56we61fwe51cwe51c51wc6ewc5'
#app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///database/cjflask.db'
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://cjpostgres:cjflask@localhost:5435/cjflaskapp'

db = SQLAlchemy(app)
bcrypt=Bcrypt(app)

login_manager=LoginManager(app)
app.config
from codejana_flask import routes

#a



