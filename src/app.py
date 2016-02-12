"""
app module for basic configuration.
"""
import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask_admin import Admin
from flask_mail import Mail, Message
from flask_wtf.csrf import CsrfProtect
import settings


# Include the right settings
try:
    from settings.local import *
    os.environ['APP_SETTINGS'] = "settings.local.DevelopmentConfig"
    print("called in local")
    print(os.environ['DATABASE_URL'])
except ImportError as e:
    from settings.production import *
    print("called in production")
    print(os.environ['DATABASE_URL'])
    os.environ['APP_SETTINGS'] = "settings.production.ProductionConfig"

app = Flask(__name__)
app.config['DEFAULT_RENDERERS'] = [
    'flask.ext.api.renderers.JSONRenderer',
    'flask.ext.api.renderers.BrowsableAPIRenderer',
]
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
