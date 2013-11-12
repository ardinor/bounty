from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager

from bounty.settings import DEBUG, SECRET_KEY
from bounty.moment_js import moment_js

from bounty.views.fundraisers import fundraiser_bp
from bounty.views.admin import admin_bp

app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY

db = SQLAlchemy(app)

from bounty import models

manager = Manager(app)

app.jinja_env.globals['moment_js'] = moment_js

app.register_blueprint(fundraiser_bp, url_prefix='/')
app.register_blueprint(admin_bp, url_prefix='/admin')
