

from click import password_option
from flask_login import login_user
from codejana_flask import app, db, bcrypt
from flask import Flask, render_template, url_for, redirect, flash
from codejana_flask.forms import RegistrationForm,LoginForm,ResetRequestForm
from codejana_flask.models import User
from flask_login import login_user,logout_user,current_user,login_required


@app.route('/')
@app.route('/home')
def homepage():
  return render_template('homepage.html', title='Home')



@app.route('/about')
def about():
  return render_template('About.html', title='About')

@app.route('/aboutAna')
def aboutAna():
    return render_template('AboutAna.html', title='AboutAna')

@app.route('/aboutIvan')
def aboutIvan():
    return render_template('AboutIvan.html', title='AboutIvan')

@app.route('/aboutJulio')
def aboutJulio():
    return render_template('AboutJulio.html', title='AboutJulio')
    
@app.route('/account')
def account():
  return render_template('Account.html', title='Account')

@app.route('/games')
def games():
    return render_template('games.html', title='Games')

@app.route('/about/user')
def user():
    return render_template('user.html', title='User')

@app.route('/register', methods=['POST', 'GET'])
def register():
  if current_user.is_authenticated:
    return redirect(url_for('account'))

  form=RegistrationForm()
  if form.validate_on_submit():
    encrypted_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
    user=User(username=form.username.data,email=form.email.data,password=encrypted_password)
    db.session.add(user)
    db.session.commit()
    flash(f'Account created successfully for {form.username.data}', category='success')
    return redirect(url_for('login'))
  return render_template('register.html', title='Register', form=form)

@app.route('/login', methods=['POST', 'GET'])
def login():
  if current_user.is_authenticated:
    return redirect(url_for('account'))
  form=LoginForm()
  if form.validate_on_submit():
        #encrypted_password=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        #user=User(username=form.username.date,email=form.email.data,password=encrypted_password)
    user=User.query.filter_by(email=form.email.data).first()
        #if user and form.password.data==user.password:
    if user and bcrypt.check_password_hash(user.password,form.password.data):
      login_user(user)
      flash(f'Login successful for {form.email.data}', category='success')
      return redirect(url_for('account'))
    else:
      flash(f'Login unsuccessful for {form.email.data}', category='danger')
  return render_template('login.html', title='Login', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/ElliotP')
def ElliotP():
    return render_template('ElliotP.html', title='ElliotP')

@app.route('/AnaP')
def AnaP():
    return render_template('AnaP.html', title='AnaP')

@app.route('/JulioP')
def JulioP():
    return render_template('JulioP.html', title='JulioP')

@app.route('/IvanP')
def IvanP():
    return render_template('IvanP.html', title='IvanP')

def send_mail():
 pass

@app.route('/reset_password',methods=['GET','POST'])
def reset_request():
  form=ResetRequestForm()
  if form.validate_on_submit():
    user=User.query.filter_by(email=form.email.data).first()
    if user:
      send_mail()
      flash('Reset request sent. Check your email.','success')
      return redirect(url_for('login'))

  return render_template('Reset_request.html', title='Reset',form=form, legend='ResetPassword')
