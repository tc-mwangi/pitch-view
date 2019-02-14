import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('secretbunny') or 'beachbunny'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    MAIL_SERVER =os.environ.get('MAIL_SERVER')
    MAIL_PORT =int(os.environ.get('MAIL_PORT') or 25)
    # TLS- transport layer security to enable encryption
    MAIL_USE_TLS=os.environ.get('MAIL_USE_TLS') is not None
    MAIL_USERNAME=os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')
    ADMINS= ['saber.dangermouse@gmail.com']


# import os
# basedir = os.path.abspath(os.path.dirname(__file__))


# class Config(object):
#     DEBUG = False
#     TESTING = False
#     CSRF_ENABLED = True
#     SECRET_KEY = 'beachbunny'
#     SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


# class ProductionConfig(Config):
#     DEBUG = False


# class StagingConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True


# class DevelopmentConfig(Config):
#     DEVELOPMENT = True
#     DEBUG = True


# class TestingConfig(Config):
#     TESTING = True
