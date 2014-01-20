from flask import Blueprint

admin_bp = Blueprint('admin', __name__, template_folder='templates')

@admin_bp.route('/')
def index():
    return 'okay'

@admin_bp.route('/user_list/')
def user_list():
    pass

@admin_bp.route('/user/<name>/')
def user(name):
    pass

@admin_bp.route('/backer_list/')
def backer_list():
    pass

@admin_bp.route('/backer/<name>/')
def backer(name):
    pass

@admin_bp.route('/backer/<name>/delete/', methods=['POST'])
def backer_delete(name):
    pass

@admin_bp.route('/fundraiser/')
def fundraiser_list():
    pass

@admin_bp.route('/fundraiser/<name>/')
def fundraiser(name):
    pass

@admin_bp.route('/fundraiser/create/', methods=['GET', 'POST'])
def fundraiser_create():
    pass

@admin_bp.route('/fundraiser/<name>/delete', methods=['POST'])
def fundraiser_delete(name):
    pass

@admin_bp.route('/fundraiser/<name>/edit', methods=['GET', 'POST'])
def fundraiser_edit(name):
    pass
