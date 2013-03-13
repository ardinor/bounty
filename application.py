# -*- coding: utf-8 -*-

import tornado.ioloop
import tornado.web
import tornado.options
import tornado.httpserver

#import pymongo
import os

from admin import AdminHandler
from base import BaseHandler
from fundraiser import FundraiserCreateHandler
from fundraiser import FundraiserEditHandler
from fundraiser import FundraiserDetailHandler
from fundraiser import FundraiserDetailJSONHandler


class IndexHandler(BaseHandler):

    def get(self):
        recent = self.db.fundraisers.find().sort('-launched').limit(15)
        self.render('index.html', recent=recent)


class LoginHandler(tornado.web.RequestHandler):

    def get(self):
        self.render('login.html')


class LogoutHandler(tornado.web.RequestHandler):
    pass


class Application(tornado.web.Application):

    def __init__(self):

        handlers = [
                    (r'/', IndexHandler),
                    (r'/login', LoginHandler),
                    (r'/logout', LogoutHandler),
                    (r'/admin', AdminHandler),
                    (r'/fundraiser/create', FundraiserCreateHandler),
                    (r'/fundraiser/([^/]+)/edit', FundraiserEditHandler),
                    (r'/fundraiser/([^/]+)', FundraiserDetailHandler),
                    (r'/fundraiser/([^/]+).json', FundraiserDetailJSONHandler),
                   ]
        settings = dict(
            template_path=os.path.join(os.path.dirname(__file__), 'templates'),
            static_path=os.path.join(os.path.dirname(__file__), 'static'),
            debug=True,
            xsrf_cookies=True,
            cookie_secret='SECRET_KEY_HERE',
            login_url='/login',
            )

        tornado.web.Application.__init__(self, handlers, **settings)

if __name__ == '__main__':

    tornado.options.parse_command_line()
    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(8888)
    tornado.ioloop.IOLoop.instance().start()
