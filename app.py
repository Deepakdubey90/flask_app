import os
import flask
from flask import Flask, render_template, request, json
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.sqlalchemy import SQLAlchemy
from flask_admin import Admin
import config


os.environ['APP_SETTINGS']="config.DevelopmentConfig"
app = flask.Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import User

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

@app.route('/showSignUp')
def showSignUp():
    """
    Display signup page for registration.
    """
    return render_template('signup.html')

@app.route('/showSignIn')
def showSignIn():
    """
    Display signin page for login.
    """
    return render_template('signin.html')

@app.route('/showServices')
def showServices():
    """
    Display services .
    """
    return render_template('services.html')

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

@app.route('/signUp',methods=['POST'])
def signUp():
    """
    views to make registration.
    """
    # read the posted values from the UI
    name = request.form['inputName']
    email = request.form['inputEmail']
    password = request.form['inputPassword']

    if name and email and password:
        return json.dumps({'html':'<span>All fields good !!</span>'})
    else:
        return json.dumps({'html':'<span>Enter the required fields</span>'})


if __name__ == '__main__':
    db.create_all()

    x = User("test", "test@gmail.com")
    db.session.add(x)
    db.session.commit()
    app.debug=True
    app.run()
