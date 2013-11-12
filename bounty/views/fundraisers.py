from flask import Blueprint

fundraiser = Blueprint('fundraiser', __name__, template_folder='templates/fundraisers')

@fundraiser.route('/')
def index():
