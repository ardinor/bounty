from flask import Blueprint

user_bp = Blueprint('users', __name__, template_folder='templates')

@user_bp.route('/')
def index():
    return 'okay'

@user_bp.route('/create/', methods=['GET', 'POST'])
def create():
    pass

@user_bp.route('/login/')
def login():
    pass

@user_bp.route('/lougout/')
def logout():
    pass
