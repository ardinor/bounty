from flask import Blueprint
from flask.ext.login import login_user, logout_user
from passlib.hash import pbkdf2_sha256
import datetime

from bounty import lm
from bounty.models import User
from bounty.forms import LoginForm, CreateUserForm

user_bp = Blueprint('users', __name__, template_folder='templates')

@user_bp.route('/')
def index():
    return 'okay'

@user_bp.route('/create/', methods=['GET', 'POST'])
def create():
    form = CreateUserForm
    if form.validate_on_submit():
        hashed_pw = pbkdf2_sha256.encrypt(form.password.data)
        user = User(name=form.username.data,
                    password=hashed_pw,
                    email=form.email.data,
                    joined_at=datetime.datetime.now())
        user.save()
        login_user(user)
        flash('User created successfully.')
        return redirect(request.args.get('next') or url_for('fundraiser.index'))

@user_bp.route('/login/')
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #after validation
        login_user(user)
        #if remember me
        #login_user(user, remember=True)
        flash('Login successful.')
        return redirect(request.args.get('next') or url_for('fundraiser.index'))
    return render_template('login.html', form=form)

@user_bp.route('/logout/')
def logout():
    logout_user()
    return redirect('fundraiser.index')

@lm.user_loader
def load_user(userid):
    return User.get(userid)
