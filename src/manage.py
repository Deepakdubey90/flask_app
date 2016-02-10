import os
from flask.ext.script import Manager
from flask import Blueprint
from flask.ext.migrate import Migrate, MigrateCommand
import flask.ext.restless
from app import app, db
from utils.base import BaseModel
from user.models import User
from feature.models import Feature
from document.models import Document
from blog.models import Blog
from settings import *
from user.views import *
import urls


migrate = Migrate(app, db)
manager = Manager(app)

# creating blue prints

#*******************************************************
# Create the Flask-Restless API manager.
mgr = flask.ext.restless.APIManager(app, flask_sqlalchemy_db=db)

# Create API endpoints, which will be available at /api/<tablename> by
# default. Allowed HTTP methods can be specified as well.

mgr.create_api(User, methods=['GET', 'POST', 'PUT', 'DELETE'])

#******************************************************

manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()
