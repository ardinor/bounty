from flask import Flask

from flask.ext.script import Manager
from flask.ext.login import LoginManager

#from bounty.settings import DEBUG, SECRET_KEY
from bounty.moment_js import moment_js

app = Flask(__name__)
app.config.from_object('bounty.settings')
#app.debug = DEBUG
#app.secret_key = SECRET_KEY
print(app.config['SQLALCHEMY_DATABASE_URI'])

manager = Manager(app)

app.jinja_env.globals['moment_js'] = moment_js

lm = LoginManager()
lm.setup_app(app)
lm.login_view = 'user.login'
lm.session_protection = "strong"

from bounty.models import *

from bounty.views import admin, fundraisers, users

app.register_blueprint(fundraisers.fundraiser_bp, url_prefix='/')
app.register_blueprint(admin.admin_bp, url_prefix='/admin')
app.register_blueprint(users.user_bp, url_prefix='/user')
