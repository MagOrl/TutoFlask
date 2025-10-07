from flask import Flask 
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app=Flask(__name__)
login_manager = LoginManager(app)
login_manager.login_view = "login"
app.config.from_object('config')

# Create database connection object
db = SQLAlchemy()
db.init_app(app)

