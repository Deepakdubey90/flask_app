import os
from config import Config
basedir = os.path.abspath(os.path.dirname(__file__))

os.environ['DATABASE_URL'] = 'postgresql+psycopg2:///mydatabase'

class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
    DEBUG_TB_ENABLED = False
    STRIPE_SECRET_KEY = 'foo'
    STRIPE_PUBLISHABLE_KEY = 'bar'
