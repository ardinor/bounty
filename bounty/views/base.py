from flask import g
from flask.ext.security import current_user

from bounty import app

@app.before_request
def before_request():
    g.user = current_user
