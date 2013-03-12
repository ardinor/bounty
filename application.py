# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver

import pymongo
import os

from admin import AdminHandler
from fundraiser import FundraiserCreateHandler
from fundraiser import FundraiserEditHandler


class Application(tornado.web.Application):

    def __init__(self):

        handlers = [
                    (r'/', IndexHandler),
                    (r'/login', LoginHandler),
                    (r'/logout', LogoutHandler),
                    (r'/admin', AdminHandler),
                    (r'/fundraiser/create', FundraiserCreateHandler),
                    (r'/fundraiser/([^/]+)/edit', FundraiserEditHandler),
                 ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True,
            )

        tornado.web.Application.__init__(self, handlers, **settings)


class BaseHandler(tornado.web.RequestHandler):

    @property
    def db(self):
        conn = pymongo.Connection()
        db = conn.bounty
        return db


class IndexHandler(BaseHandler):

    def get(self):
        recent = self.db.fundraisers.find().sort('-launched').limit(15)
        self.render('index.html', recent=recent)


class LoginHandler(tornado.web.RequestHandler):
    pass


class LogoutHandler(tornado.web.RequestHandler):
    pass


if __name__ == '__main__':

    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
