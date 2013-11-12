from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

from settings import DEBUG, SECRET_KEY
from moment_js import moment_js

from views.fundraisers import fundraiser_bp

app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY

db = SQLAlchemy(app)

from bounty import models

app.jinja_env.globals['moment_js'] = moment_js

app.register_blueprint(fundraiser_bp, url_prefix='/fundraisers')
