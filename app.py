"""
app module for basic configuration.
"""
import os
from flask import Blueprint, Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_mail import Mail, Message
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

#app = Flask(__name__)
app = Flask(__name__, static_folder = os.path.join(os.path.dirname(__file__), "static"))

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
csrf = CsrfProtect(app)

db = SQLAlchemy(app)
db.create_all()

admin = Admin(app, name='Admin', template_mode='bootstrap3')
