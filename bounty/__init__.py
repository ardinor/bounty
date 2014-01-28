from flask import Flask

from flask.ext.script import Manager
from flask.ext.login import LoginManager
from flask.ext.security import Security, SQLAlchemyUserDatastore
from flask.ext.assets import Environment, Bundle

#from bounty.settings import DEBUG, SECRET_KEY
from bounty.moment_js import moment_js

app = Flask(__name__)
app.config.from_object('bounty.settings')
#app.debug = DEBUG
#app.secret_key = SECRET_KEY

manager = Manager(app)

app.jinja_env.globals['moment_js'] = moment_js

lm = LoginManager()
lm.setup_app(app)
lm.login_view = 'user.login'
lm.session_protection = "strong"

from bounty.models import *

from bounty.views import admin, base, fundraisers, users

app.register_blueprint(fundraisers.fundraiser_bp, url_prefix='/')
app.register_blueprint(admin.admin_bp, url_prefix='/admin')
app.register_blueprint(users.user_bp, url_prefix='/user')

user_datastore = SQLAlchemyUserDatastore(db, User, Role)
security = Security(app, user_datastore)

assets = Environment(app)

css = Bundle('css/bootstrap.min.css',
             'css/bootstrap-responsive.css',
             'css/bootstrap-datetimepicker.min.css',
             'css/bounty.css')
assets.register('css_all', css)

js = Bundle('js/vendor/jquery-1.9.1.min.js',
            'js/vendor/bootstrap.min.js',
            'js/vendor/bootstrap-datetimepicker.min.js',
            'js/vendor/modernizr-2.6.2-respond-1.1.0.min.js',
            'js/bounty.js')
assets.register('js_all', js)

fav_icon = Bundle('img/favicon.ico')
assets.register('fav_icon', fav_icon)
