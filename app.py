import os
import flask
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext.login import LoginManager
from flask import Flask, render_template, request, json, flash, redirect, url_for
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.sqlalchemy import SQLAlchemy
from flask_admin import Admin
import flask.ext.restless
from flask_mail import Mail, Message
from flask_wtf.csrf import CsrfProtect
import config


os.environ['APP_SETTINGS']="config.DevelopmentConfig"
app = flask.Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

app = Flask(__name__, static_url_path='/static')
CsrfProtect(app)

# updateing mail_configuration.
app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'deepak.dubey@vertisinfotech.com',
    MAIL_PASSWORD = 'hpjefjctuctmeqoe'
))
mail=Mail(app)

csrf = CsrfProtect()

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
from models import User # specify the models which you have defined.
import views

admin = Admin(app, name='Admin', template_mode='bootstrap3')

#*******************************************************
# Create the Flask-Restless API manager.
manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.
manager.create_api(User, methods=['GET', 'POST', 'PUT', 'DELETE'])

#******************************************************

from routes import *

if __name__ == '__main__':
    db.create_all()
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
