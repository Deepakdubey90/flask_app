import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import flask.ext.restless
import config
from app import app, db
from models import User
import views


app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)


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
