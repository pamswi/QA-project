from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

db = SQLAlchemy

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)


# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
import application.routes