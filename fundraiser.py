# -*- coding: utf-8 -*-
import tornado.web


class FundraiserCreateHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('fundraiser/create.html')

    def post(self):
        title = self.get_argument('title', None)
        goal = self.get_argument('goal', None)
        deadline = self.get_argument('deadline', None)
        description = self.get_argument('description', None)

        #sanitise


class FundraiserEditHandler(tornado.web.RequestHandler):
    pass
