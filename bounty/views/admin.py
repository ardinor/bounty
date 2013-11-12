from flask import Blueprint

admin_bp = Blueprint('admin', __name__, template_folder='templates')

@admin_bp.route('/')
def index():
    return 'okay'
