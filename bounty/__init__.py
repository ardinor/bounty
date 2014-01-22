from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.script import Manager
from flask.ext.login import LoginManager

from bounty.settings import DEBUG, SECRET_KEY
from bounty.moment_js import moment_js

from bounty.views.fundraisers import fundraiser_bp
from bounty.views.admin import admin_bp
from bounty.views.users import user_bp

app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY

db = SQLAlchemy(app)

from bounty import models

manager = Manager(app)

app.jinja_env.globals['moment_js'] = moment_js

app.register_blueprint(fundraiser_bp, url_prefix='/')
app.register_blueprint(admin_bp, url_prefix='/admin')
app.register_blueprint(user_bp, url_prefix='/user')

lm = LoginManager()
lm.setup_app(app)
lm.login_view = 'user.login'
lm.session_protection = "strong"

@lm.user_loader
def load_user(userid):
    return User.get(userid)
