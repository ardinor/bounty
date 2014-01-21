from flask import Blueprint, render_template, abort

from bounty.models import Fundraiser, Backer
from bounty.settings import STATUS_LIVE, FUNDRAISER_FUNDRAISER, \
    FUNDRAISER_GROUP_PURCHASE, FUNDRAISER_PETITION, FUNDRAISERS_PER_PAGE

fundraiser_bp = Blueprint('fundraiser', __name__, template_folder='templates')

@fundraiser_bp.route('/')
@fundraiser_bp.route('/index')
@fundraiser_bp.route('/index/<int:page>')
def index(page=1):
    fundraisers = Fundraiser.query.filter_by(status=STATUS_LIVE).paginate(page,
                                                                          FUNDRAISERS_PER_PAGE,
                                                                          True)
    if fundraisers:
        return render_template('fundraisers/list.html', fundraisers=fundraisers)
    else:
        abort(404)

@fundraiser_bp.route('/<name>/', methods=['GET', 'POST'])
def fundraiser(name):
    fundraiser = Fundraiser.query.filter_by(name=name).first()
    if fundraiser.is_published():
        backers = Backer.query.filter_by(backed=fundraiser.id)
        if fundraiser.has_template():
            return render_template('fundraisers/user_uploaded/{}'.format(fundraiser.template),
                                   fundraiser=fundraiser,
                                   backers=backers)
        else:
            return render_template('detail.html',
                                   fundraiser=fundraiser,
                                   backers=backers)
    else:
        abort(404)


@fundraiser_bp.route('/type/<type>/')
@fundraiser_bp.route('/type/<type>/<int:page>')
def fundraiser_type(type, page=1):
    if type == 'group_purchase':
        type = FUNDRAISER_GROUP_PURCHASE
    elif type == 'fundraiser':
        type = FUNDRAISER_FUNDRAISER
    elif type == 'petition':
        type = FUNDRAISER_PETITION
    else:
        abort(404)
    fundraisers = Fundraiser.query.filter_by(type=type).paginate(page,
                                                                 FUNDRAISERS_PER_PAGE,
                                                                 True)
    if fundraisers:
        return render_template('fundraisers/list.html',
                               fundraisers=fundraisers)
    else:
        abort(404)

