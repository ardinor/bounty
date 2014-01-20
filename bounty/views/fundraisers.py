from flask import Blueprint
from bounty.models import Fundraiser, Backer
from bounty.settings import STATUS_LIVE

fundraiser_bp = Blueprint('fundraiser', __name__, template_folder='templates')

@fundraiser_bp.route('/')
def index():
    fundraisers = Fundraiser.query.filter_by(status=STATUS_LIVE)
    return render_template('fundraisers/list.html', fundraisers=fundraisers)

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
def fundraiser_type(type):
    pass

