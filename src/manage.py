import os
from flask.ext.script import Manager
from flask import Blueprint
from flask.ext.migrate import Migrate, MigrateCommand
import flask.ext.restless
from app import app, db
from utils.base import BaseModel
from settings import *
import urls


migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()
