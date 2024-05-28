import os
from dotenv import load_dotenv

BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    load_dotenv()

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(BASE_DIR, 'database', 'ecourse.sqlite3')
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_ADMIN_SWATCH = 'lux'