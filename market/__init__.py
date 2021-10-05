from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///market.db"
app.config['SECRET_KEY'] = 'bed0b3c89d25f30eae4de1b2'
db = SQLAlchemy(app)

from market import routes
