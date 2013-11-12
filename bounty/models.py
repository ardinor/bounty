from bounty import db

from settings import ROLE_USER

class Fundraiser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50), unique=True)
    slug = db.Column(db.String(50), unique=True)
    goal = db.Column(db.Float)
    #description = db.Column(db.Text)
    status = db.Column(db.String(50))
    template = db.Column(db.String(50))
    fundraiser_type = db.Column(db.String(50))
    deadline = db.Column(db.DateTime)
    launched = db.Column(db.DateTime)
    current_funding = db.Column(db.Float)
    backer_count = db.Column(db.Integer)

    def __repr__(self):
        return '<Fundraiser {}>'.format(self.title)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    password = db.Column(db.String(200))
    email = db.Column(db.String(200), unique=True)
    joined_at = db.Column(db.DateTime)
    rank = db.Column(db.SmallInteger, default = ROLE_USER)
    backer_messages = db.relationship('BackMessage', backref='user',
                                      lazy='dynamic')

    def __repr__(self):
        return '<User {}>'.format(self.name)

class Backer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(50))
    #need?
    #display_name = db.Column(db.String(50))
    email = db.Column(db.String(200))
    address_line1 = db.Column(db.String(200))
    address_line2 = db.Column(db.String(200))
    state = db.Column(db.String(10))
    postcode = db.Column(db.Integer)
    card_token = db.Column(db.String(40))
    #Max length should be 45 (http://stackoverflow.com/questions/166132/maximum-length-of-the-textual-representation-of-an-ipv6-address)
    ip_address = db.Column(db.String(45))
    amount = db.Column(db.Float)
    created_at = db.Column(db.DateTime)
    messages = db.relationship('BackMessage', backref='backer',
                               lazy='dynamic')

class BackerMessage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    backer_id = db.Column(db.Integer, db.ForeignKey('backer.id'))
    date = db.Column(db.DateTime)
    status = db.Column(db.String(40))
    message = db.Column(db.String(200))
    staff = db.Column(db.Integer, db.ForeignKey('user.id'))  #need to make a 'System' user for system generated messages?
