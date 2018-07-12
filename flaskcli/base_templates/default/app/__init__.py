from flask import Flask, jsonify, render_template, url_for, request, redirect, json, make_response
from flask_sqlalchemy import SQLAlchemy, functools
from flask_cors import CORS, cross_origin
from datetime import datetime, timedelta

import pymysql, os, math, requests, uuid

from flask_bcrypt import Bcrypt
from functools import wraps

pymysql.install_as_MySQLdb()

import cherrypy
from cherrypy import log

import logging
from logging.handlers import *
import logging.config

logger = logging.getLogger()
db_logger = logging.getLogger('db')

from flask_cache import Cache


app = Flask(__name__)
cache = Cache(app,config={'CACHE_TYPE': 'simple'})
CORS(app)

def close(self):
	self.session.close()


def clearCache():
	#clear the cache data
	with app.app_context():
		cache.clear()

def Logger(requestType,funcName, endPoint, message, metaData, Lang):
	#Open new data file
	return cherrypy.log('requestType: [{}], timeStamp: {}, funcName : {}, api : {}, message : {}, metaData : {}, lang : {}'.format(requestType,datetime.now(), funcName, endPoint, message, metaData, Lang))


# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/claims_db'
# app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['SQLALCHEMY_DATABASE_URI']
app.config['VERSION'] = 'v1'
app.config['SECRET_KEY'] = 'somestrongstring'  # YOU MUST NEVER CHANGE THIS
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
app.config['BCRYPT_LOG_ROUNDS'] = 13  # YOU MUST NEVER CHANGE THIS
app.config['COMPANY_NAME'] = ''

app.config['CACHE_DURATION'] = 86400 ## Equal to a day


bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

# from routes import 