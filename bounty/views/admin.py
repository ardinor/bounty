from flask import Blueprint, render_template, abort, redirect, url_for
from flask.ext.security import roles_accepted, roles_required

from bounty import db
from bounty.models import Fundraiser, User, Backer
from bounty.forms import FundraiserCreateForm
from bounty.settings import USERS_PER_PAGE, FUNDRAISERS_PER_PAGE

admin_bp = Blueprint('admin', __name__, template_folder='templates')

@admin_bp.route('/')
@roles_accepted('admin', 'staff')
def index():
    return 'okay'


@admin_bp.route('/user_list/')
@admin_bp.route('/user_list/<int:page>')
@roles_required('admin')
def user_list(page=1):
    users = User.query.order_by('name').all().paginate(page, USERS_PER_PAGE, True)
    if users:
        return render_template('admin/user_list.html', users=users)
    else:
        abort(404)


@admin_bp.route('/user/<name>/')
@roles_required('admin')
def user(name):
    user = User.query.filter_by(name=name).first_or_404()
    return render_template('admin/user_detail.html', user=user)


@admin_bp.route('/backer_list/')
@admin_bp.route('/backer_list/<int:page>')
@roles_accepted('admin', 'staff')
def backer_list(page=1):
    backers = Backer.query.order_by('-created_at').all().paginate(page, USERS_PER_PAGE, True)
    if backers:
        return render_template('admin/backer_list.html', backers=backers)
    else:
        abort(404)


@admin_bp.route('/backer/<id>/')
@roles_accepted('admin', 'staff')
def backer(id):
    backer = Backer.query.filter_by(id=id).first_or_404()
    return render_template('admin/backer_detail.html', backer=backer)


@admin_bp.route('/backer/<id>/delete/', methods=['POST'])
@roles_accepted('admin', 'staff')
def backer_delete(id):
    backer = Backer.query.filter_by(id=id).first_or_404()
    db.session.delete(backer)
    db.session.commit()
    return redirect(url_for('admin.backer_list'))


@admin_bp.route('/fundraiser/')
@admin_bp.route('/fundraiser/<int:page>')
@roles_accepted('admin', 'staff')
def fundraiser_list(page=1):
    # order_by?
    fundraisers = Fundraiser.query.all().paginate(page, FUNDRAISERS_PER_PAGE, True)
    if fundraisers:
        return render_template('admin/fundraiser_list.html',
            fundraisers=fundraisers)
    else:
        abort(404)

@admin_bp.route('/fundraiser/<name>/')
@roles_accepted('admin', 'staff')
def fundraiser(name):
    fundraiser = Fundraiser.query.filter_by(name=name).first_or_404()
    return render_template('admin/fundraiser_detail.html', fundraiser=fundraiser)

@admin_bp.route('/fundraiser/create/', methods=['GET', 'POST'])
@roles_accepted('admin', 'staff')
def fundraiser_create():
    if g.user is not None and g.user.is_authenticated():
        return redirect(url_for('users.login'))
    form = FundraiserCreateForm()
    if form.validate_on_submit():
        #figure out other fields
        fundraiser = Fundraiser(title=form.title.data,
                                slug=form.slug.data,
                                goal=form.goal.data,
                                )
        db.session.add(fundraiser)
        db.session.commit()
        return redirect(url_for('admin.fundraiser', fundraiser=fundraiser.name))

    return render_template('admin/fundraiser_create.html')

@admin_bp.route('/fundraiser/<name>/delete', methods=['POST'])
@roles_accepted('admin', 'staff')
def fundraiser_delete(name):
    fundraiser = Fundraiser.query.filter_by(name=name).first_or_404()
    db.session.delete(fundraiser)
    db.session.commit()
    return redirect(url_for('admin.fundraiser_list'))


@admin_bp.route('/fundraiser/<name>/edit', methods=['GET', 'POST'])
@roles_accepted('admin', 'staff')
def fundraiser_edit(name):
    fundraiser = Fundraiser.query.filter_by(name=name).first_or_404()
    pass
