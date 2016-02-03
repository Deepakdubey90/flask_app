import os


basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    """
    should contain common configuration part.
    """
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


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
