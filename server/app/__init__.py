from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from app import configs
from .api import Api

app = Flask(__name__)
app.config.from_object(configs.Config)
jwt = JWTManager(app=app)
api = Api(
    app=app,
    contact="zin.it.dev@gmail.com",
    contact_email="zin.it.dev@gmail.com",
    version='1.0.0',
    title='eCourse Swagger',
    description='RESTful APIs for eCourse application 🌶️',
    doc="/",
    license='Apache License 2.0',
    terms_url='https://www.google.com/policies/terms/'
)
ma = Marshmallow(app)
db = SQLAlchemy(app=app)
migrate = Migrate(app=app, db=db)
login_manager = LoginManager(app=app)

with app.app_context():
    from app import models
