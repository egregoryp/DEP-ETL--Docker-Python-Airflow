from flask_sqlalchemy import SQLAlchemy
from api import app

DATABASE_CONNECTION = 'mysql://root:root@192.168.2.21:3310/retail'

app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_CONNECTION
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)