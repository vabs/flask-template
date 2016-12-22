from flask import Flask

from flask.ext.sqlalchemy import SQLAlchemy

from sqlalchemy import create_engine

#app
app = Flask(__name__)

#db
engine = create_engine('postgres://postgres:postgres@localhost:5432/testdb')
db = SQLAlchemy(app)

from appname import models
from appname import views