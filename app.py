import os
import flask
from flask.ext.login import LoginManager
from flask import Flask, render_template, request, json, flash, redirect, url_for
from flask.ext.sqlalchemy import SQLAlchemy
from flask_admin import Admin
import flask.ext.restless
from flask_mail import Mail, Message
from models import User
import views
from flask_wtf.csrf import CsrfProtect
import config


# Include the right settings
try:
    from local import *
    os.environ['APP_SETTINGS'] = "local.DevelopmentConfig"
    print("called in local")
    print(os.environ['DATABASE_URL'])
except ImportError as e:
    from production import *
    print("called in production")
    print(os.environ['DATABASE_URL'])
    os.environ['APP_SETTINGS'] = "production.ProductionConfig"

app = flask.Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])

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
db.create_all()

admin = Admin(app, name='Admin', template_mode='bootstrap3')

#*******************************************************
# Create the Flask-Restless API manager.
#manager = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.

#manager.create_api(models.User, methods=['GET', 'POST', 'PUT', 'DELETE'])

#******************************************************

from routes import *
