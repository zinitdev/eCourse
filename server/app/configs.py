import os
import cloudinary
from dotenv import load_dotenv
from datetime import timedelta

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_USERNAME = os.environ.get('DB_USERNAME')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')

class Config(object):
    load_dotenv()

    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + \
        os.path.join(BASE_DIR, 'database', 'ecourse.sqlite3')
    # SQLALCHEMY_DATABASE_URI = f'mysql+pymysql://{DB_USERNAME}:{
    #     DB_PASSWORD}@{DB_HOST}/{DB_NAME}?charset=utf8mb4'

    SQLALCHEMY_TRACK_MODIFICATIONS = True
    FLASK_ADMIN_SWATCH = 'lux'

    cloudinary.config(
        cloud_name=os.environ.get('CLOUD_NAME'),
        api_key=os.environ.get('API_KEY'),
        api_secret=os.environ.get('API_SECRET')
    )
    JWT_SECRET_KEY = os.environ.get('SECRET_KEY')
    JWT_ACCESS_TOKEN_EXPIRES = timedelta(hours=1)
    JWT_TOKEN_LOCATION = ['headers']
    JWT_COOKIE_SECURE = False
    PAGE_SIZE = 10


class LocalConfig(Config):
    DEBUG = True
    DEBUG_TB_INTERCEPT_REDIRECTS = False
    SQLALCHEMY_RECORD_QUERIES = True
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 300

class ProductionConfig(Config):
    DEBUG = False
