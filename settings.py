from os import environ

SQLALCHEMY_DATABASE_URI = environ.get("DB_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = environ.get("SQL_TRACK_MODIFICATIONS", False)
DEBUG = environ.get("DEBUG_MODE", False)
AUTH_SECRET = environ.get("AUTH_SECRET")