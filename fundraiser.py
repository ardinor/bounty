# -*- coding: utf-8 -*-
#import tornado.web

from base import BaseHandler

class FundraiserBase(BaseHandler):

    @property
    def fundraisers(self):
        fundraisers = self.db.fundraisers
        return fundraisers


class FundraiserCreateHandler(FundraiserBase):

    def get(self):
        self.render('fundraiser/create.html')

    def post(self):
        title = self.get_argument('title', None)
        slug = self.get_arguments('slug', None)
        goal = self.get_argument('goal', None)
        deadline = self.get_argument('deadline', None)
        description = self.get_argument('description', None)

        #sanitise

        self.redirect('fundraiser/{}'.format(slug))


class FundraiserEditHandler(FundraiserBase):

    def get(self, fundraiser_slug):
        fundraiser = self.fundraisers.find_one({'slug': fundraiser_slug})
        if fundraiser:
            self.render('fundraiser/detail.html',
                fundraiser=fundraiser)
        else:
            raise tornado.web.HTTPError(404)


class FundraiserDetailHandler(FundraiserBase):

    def get(self, fundraiser_slug):
        fundraiser = self.fundraisers.find_one({'slug': fundraiser_slug})
        if fundraiser:
            self.render('fundraiser/detail.html',
                fundraiser=fundraiser)
        else:
            raise tornado.web.HTTPError(404)
