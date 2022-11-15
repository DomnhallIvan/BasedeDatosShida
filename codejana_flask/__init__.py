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
app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT']=587
app.config['MAIL_USE_TLS']=True

app.config['MAIL_USERNAME']='pagbasededatos11@gmail.com'
app.config['MAIL_PASSWORD']='amerike2021'

mail=Mail(app)
from codejana_flask import routes

#a



