from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# configure session
app.config["SESSION_PERNAMENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
app.secret_key = 'key'


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db = SQLAlchemy(app)
import application.routes