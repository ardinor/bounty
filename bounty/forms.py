from flask.ext.wtf import Form
from wtforms import TextField, BooleanField, PasswordField, \
    TextAreaField
from wtforms.fields.html5 import EmailField
from wtforms.validators import Required, Length, EqualTo


class LoginForm(Form):
    username = TextField('Username', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('remember_me', default=False)


class CreateUserForm(Form):
    username = TextField('Username', validators=[Required(), Length(max=50)])
    email = EmailField('E-mail', validators=[Required(), Length(max=255)])
    password = PasswordField('Password', validators=[Required()])
    password_verify = PasswordField('Password Again',
        validators=[Required(), EqualTo('password', message='Passwords must match')])


class FundraiserCreateForm(Form):
    pass
