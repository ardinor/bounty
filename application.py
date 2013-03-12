# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web

from admin import AdminHandler
from fundraiser import FundraiserCreateHandler
from fundraiser import FundraiserEditHandler


class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        return self.application.db

    @property
    def session(self):
        return self.application.session

    def get_current_user(self):
        auth = self.get_secure_cookie('auth')
        if not auth:
            return None


class IndexHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('index.html')


class LoginHandler(tornado.web.RequestHandler):
    pass


class LogoutHandler(tornado.web.RequestHandler):
    pass


if __name__ == '__main__':

    application = tornado.web.Application(
        handlers=[
                    (r'/', IndexHandler),
                    (r'/login', LoginHandler),
                    (r'/logout', LogoutHandler),
                    (r'/admin', AdminHandler),
                    (r'/fundraiser/create', FundraiserCreateHandler),
                    (r'/fundraiser/([^/]+)/edit', FundraiserEditHandler),
                 ], **{"template_path": "templates"})
    application.listen(8899)
    tornado.ioloop.IOLoop.instance().start()
