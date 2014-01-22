# -*- coding: utf-8 -*-
import os
basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = True
#generate cookie secret: print base64.b64encode(uuid.uuid4().bytes + uuid.uuid4().bytes)
SECRET_KEY = 'SecretKeyGoesHere'

#Just use sqllite for testing
SQLALCHEMY_DATABASE_URI = 'sqlite:////' + os.path.join(basedir, 'app.db')

ROLE_ADMIN = 2
ROLE_USER = 1

FUNDRAISER_FUNDRAISER = 1
FUNDRAISER_GROUP_PURCHASE = 2
FUNDRAISER_PETITION = 3

STATUS_DRAFT = 1
STATUS_LIVE = 2
STATUS_FINISHED = 3

FUNDRAISERS_PER_PAGE = 6
USERS_PER_PAGE = 20
