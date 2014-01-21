from flask import Blueprint, render_template, abort

from bounty.models import Fundraiser, User, Backer
from bounty.settings import USERS_PER_PAGE

admin_bp = Blueprint('admin', __name__, template_folder='templates')

@admin_bp.route('/')
def index():
    return 'okay'

@admin_bp.route('/user_list/')
@admin_bp.route('/user_list/<int:page>')
def user_list(page=1):
    users = User.query.order_by('name').all().paginate(page, USERS_PER_PAGE, True)
    if users:
        return render_template('admin/user_list.html', users=users)
    else:
        abort(404)

@admin_bp.route('/user/<name>/')
def user(name):
    user = User.query.filter_by(name=name)
    if user:
        return render_template('admin/user_detail.html', user=user)
    else:
        abort(404)

@admin_bp.route('/backer_list/')
@admin_bp.route('/backer_list/<int:page>')
def backer_list(page=1):
    backers = Backer.query.order_by('-created_at').all().paginate(page, USERS_PER_PAGE, True)
    if backers:
        return render_template('admin/backer_list.html', backers=backers)
    else:
        abort(404)

@admin_bp.route('/backer/<id>/')
def backer(id):
    backer = Backer.query.filter_by(id=id)
    if backer:
        return render_template('admin/backer_detail.html', backer=backer)
    else:
        abort(404)

@admin_bp.route('/backer/<id>/delete/', methods=['POST'])
def backer_delete(id):
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
