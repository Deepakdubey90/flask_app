import os
from config import Config
basedir = os.path.abspath(os.path.dirname(__file__))


os.environ['DATABASE_URL'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
#"postgresql://scott:tiger@localhost/app"


class DevelopmentConfig(Config):
    DEBUG = False
    CSRF_ENABLED = True
    SECRET_KEY = 'secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    DEVELOPMENT = True
    DEBUG = True
