import os
import psycopg2
import urlparse
from config import Config
basedir = os.path.abspath(os.path.dirname(__file__))
os.environ['DATABASE_URL'] = 'postgresql+psycopg2://scott:tiger@localhost/app'

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    DEBUG_TB_ENABLED = False
    STRIPE_SECRET_KEY = 'foo'
    STRIPE_PUBLISHABLE_KEY = 'bar'
    SQLALCHEMY_TRACK_MODIFICATIONS =True

    ADMINS = [
        '"Deepak" <deepak.dubey@vertisinfotech.com>',
    ]
    # Web-server related settings
    PORT_NUMBER= 5000
