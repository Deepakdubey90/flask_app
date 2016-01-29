import os
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
import config
from app import app, db
from waitress import serve


os.environ['APP_SETTINGS']="config.DevelopmentConfig"
app.config.from_object(os.environ['APP_SETTINGS'])
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)
"""
if __name__ == '__main__':
    manager.run()
"""
if __name__ == "__main__":
    os.environ['APP_SETTINGS']="config.DevelopmentConfig"
    manager.run()
    #app.run(host='0.0.0.0', port=port)
else:
    os.environ['APP_SETTINGS']="config.ProductionConfig"
    manager.run()
    serve(app, port=port)
