from flask import Blueprint

fundraiser_bp = Blueprint('fundraiser', __name__, template_folder='templates')

@fundraiser_bp.route('/')
def index():
    return 'okay!'
