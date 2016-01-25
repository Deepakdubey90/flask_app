import os
import flask
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext.login import LoginManager
from flask import Flask, render_template, request, json, flash, redirect, url_for
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.sqlalchemy import SQLAlchemy
from flask_admin import Admin
import config


os.environ['APP_SETTINGS']="config.DevelopmentConfig"
app = flask.Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
from models import User # specify the models which you have defined.

admin = Admin(app, name='Admin', template_mode='bootstrap3')

# routing configuration.
@app.route('/')
def index():
    """
    Displays the index page accessible at '/'
    """
    return flask.render_template('index.html')

@app.route('/hello/<name>/')
def hello(name):
    """
    Displays the page greats who ever comes to visit it.
    """
    return flask.render_template('hello.html', name=name)

@app.route('/showServices')
def showServices():
    """
    Display services .
    """
    return render_template('services.html')

@app.route('/about')
def about():
     """
     Display portfolio.
     """
     return render_template('about.html')

@app.route('/showPortfolio')
def showPortfolio():
     """
     Display portfolio.
     """
     return render_template('portfolio.html')

@app.errorhandler(404)
def page_not_found(error):
    """
    Display error page if url not matched.
    """
    return render_template('error.html')

@login_manager.user_loader
def user_loader(user_id):
    user = User.query.filter_by(id=user_id)
    if user.count() == 1:
	return user.one()
    return None

@app.route('/signUp',methods=['GET', 'POST'])
def signUp():
    """
    views to make registration.
    """
    if request.method == 'GET':
	return render_template('signup.html')
    elif request.method == 'POST':
	# read the posted values from the UI
	username = request.form['userName']
	email = request.form['email']
	password = request.form['password']
	if username and password:
	    user = User.query.filter_by(username=username)
	    if user.count() == 0:
		user = User(username=username, password=password)
		db.session.add(user)
		db.session.commit()
		user = User.query.all()
		print("users are :: ", user)
		flash('You have registered the username {0}. Please login'.format(username))
		#return json.dumps({'status':'OK','user':username,'pass':password});
		print("@@@@@@@@@@@@@@@@@@@@@ redirected to showSignIn part")
		return redirect(url_for('index'))
	    else:
		print("@@@@@@@@@@@@@@@@@@@@@ redirected to showSignUp part")
		flash('The username {0} is already in use.  Please try a new username.'.format(username))
		return redirect(url_for('signUp'))
	else:
	    return json.dumps({'html':'<span>Enter the required fields</span>'})
    else:
	return abort(405)

@app.route('/signIn',methods=['GET', 'POST'])
def signIn():
    """
    view to make user login.
    """
    if request.method == 'GET':
	return render_template('signin.html')
    elif request.method == 'POST':
	username = request.form['username']
	password = request.form['password']
	user = User.query.filter_by(username=username).filter_by(password=password)
	print(user, "user detail is ::")
	if user.count() == 1:
	    login_user(user.one())
	    flash('Welcome back {0}'.format(username))
	    print("@@@@@@@@@@@@Login successfully!!!!!")
	    return (url_for('index'))
	else:
	    flash('Invalid login')
	    print("@@@@@@@@@@@@Login Failed!!!!!")
	    return (url_for('signIn'))
    else:
	return abort(405)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

if __name__ == '__main__':
    db.create_all()

    x = User("test", "test@gmail.com")
    db.session.add(x)
    db.session.commit()
    app.debug=True
    app.run()
