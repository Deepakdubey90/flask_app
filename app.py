import os
import flask
from flask.ext.login import login_user, logout_user, current_user, login_required
from flask.ext.login import LoginManager
from flask import Flask, render_template, request, json, flash, redirect, url_for
from werkzeug import generate_password_hash, check_password_hash
from flask.ext.sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_wtf.csrf import CsrfProtect
import config


os.environ['APP_SETTINGS']="config.DevelopmentConfig"
app = flask.Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
CsrfProtect(app)

csrf = CsrfProtect()

login_manager = LoginManager()
login_manager.init_app(app)

db = SQLAlchemy(app)
from models import User # specify the models which you have defined.

admin = Admin(app, name='Admin', template_mode='bootstrap3')

from routes import *

if __name__ == '__main__':
    db.create_all()

    x = User("test", "test@gmail.com")
    db.session.add(x)
    db.session.commit()
    app.debug=True
    app.run()
