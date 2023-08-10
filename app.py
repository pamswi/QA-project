from flask import Flask
from application import app, db
import os, requests









if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')