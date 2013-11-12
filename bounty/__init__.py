from flask import Flask
from settings import DEBUG, SECRET_KEY

app = Flask(__name__)
app.debug = DEBUG
app.secret_key = SECRET_KEY
