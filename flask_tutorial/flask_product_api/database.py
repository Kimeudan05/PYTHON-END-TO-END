from flask_sqlalchemy import SQLAlchemy
from flask import Flask

db=SQLAlchemy()

def init_db(app):
    # credentils to connect to the database
    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:2013%40Wewe@localhost/flask_products"
    app.config["SQLALCHEMY_TRACK_NOTIFICATIOBS"] = False
    db.init_app(app)
    
    