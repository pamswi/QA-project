from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)


app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv("DATABASE_URI")
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False




# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
import application.routes