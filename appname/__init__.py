from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine

#app
app = Flask(__name__)

#db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://postgres:amdigit@localhost:5432/testdb'
engine = create_engine(app.config['SQLALCHEMY_DATABASE_URI'])
db = SQLAlchemy(app)

from appname import models
from appname import views