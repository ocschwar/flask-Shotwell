#!/usr/bin/python

from flask import Flask, request
from flask_restful import Resource, Api, reqparse, abort
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.login import LoginManager
#from flask.ext.bcrypt import Bcrypt


from config import basedir

app = Flask(__name__)
db = SQLAlchemy(app)

app.config.from_object('config')
app.secret_key = 'Shotwell secret key'
app.config['SESSION_TYPE'] = 'filesystem'
#bcrypt = Bcrypt(app)
import shotwell.views
import shotwell.Photo
import shotwell.Video

