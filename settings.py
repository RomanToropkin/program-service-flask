from os import environ
from datetime import timedelta

SQLALCHEMY_DATABASE_URI = environ.get("DB_URL")
SQLALCHEMY_TRACK_MODIFICATIONS = False
DEBUG = True
AUTH_SECRET = environ.get("AUTH_SECRET")