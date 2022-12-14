

from flask_wtf import FlaskForm
from flask_wtf.file import FileField,FileAllowed
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class RegistrationForm(FlaskForm):
    username=StringField(label='Username', validators=[DataRequired(), Length(min=3,max=20)] )
    email=StringField(label='Email', validators=[DataRequired(), Email()])
    password=PasswordField(label='Password' ,validators=[DataRequired(), Length(min=6,max=16)])
    confirm_password=PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField(label='Signed Up')

class LoginForm(FlaskForm):
    email=StringField(label='Email', validators=[DataRequired(), Email()])
    password=PasswordField(label='Password' ,validators=[DataRequired(), Length(min=6,max=16)])
    submit=SubmitField(label='Login')

class ResetRequestForm(FlaskForm):
    email=StringField(label='Email', validators=[DataRequired(), Email()])
    submit=SubmitField(label='Reset Password', validators=[DataRequired()])

class ResetPasswordForm(FlaskForm):
    password=PasswordField(label='Password' ,validators=[DataRequired()])
    confirm_password=PasswordField(label='Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit=SubmitField(label='Change Password', validators=[DataRequired()])

class AccountUpdateForm(FlaskForm):
  picture=FileField(label="Update Profile Picture",validators=[FileAllowed(['jpg','png'])])
  submit=SubmitField(label='Update Account')