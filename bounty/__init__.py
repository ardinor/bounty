from flask import Flask

from settings import DEBUG, SECRET_KEY
from moment_js import moment_js

app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY

app.jinja_env.globals['moment_js'] = moment_js
