from kodpanik.core.config.common_settings import *

DEBUG = False
TESTING = False
SECRET_KEY = '3b4d1d066742f07b0deb29d2'
SQLALCHEMY_DATABASE_URI = "sqlite:////tmp/example.db"
ENV = "development"
MAIL_BACKEND = "console"

try:
    from kodpanik.core.config.local_settings import *
except ModuleNotFoundError:
    pass
