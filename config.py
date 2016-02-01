import os
basedir = os.path.abspath(os.path.dirname(__file__))
os.environ['DATABASE_URL'] = 'sqlite:///' + os.path.join(basedir, 'app.db')


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

    # mail settings
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 875
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False

    # gmail authentication
    MAIL_USERNAME = 'deepak.dubey@vertisinfotech.com'
    MAIL_PASSWORD = 'hpjefjctuctmeqoe'

    # mail accounts
    MAIL_DEFAULT_SENDER = 'deepak.dubey@vertisinfotech.com'


class ProductionConfig(Config):
    DEBUG = False
    SECRET_KEY = 'my_precious'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://scott:tiger@localhost/app'
    DEBUG_TB_ENABLED = False
    STRIPE_SECRET_KEY = 'foo'
    STRIPE_PUBLISHABLE_KEY = 'bar'


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
