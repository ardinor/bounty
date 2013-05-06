# -*- coding: utf-8 -*-
from tornado.web import HTTPError
#from tornado.httpserver import HTTPParseBody
from tornado.escape import json_decode
import datetime
import json
import unicodedata
import re

from base import BaseHandler


class FundraiserBase(BaseHandler):

    @property
    def fundraisers(self):
        fundraisers = self.db.fundraisers
        return fundraisers


class FundraiserIndexHandler(FundraiserBase):

    def get(self):
        recent = self.fundraisers.find().sort('-launched').limit(30)
        self.render('index.html', recent=recent)


class FundraiserCreateHandler(FundraiserBase):

    def get(self):
        self.render('fundraiser/create.html',
                    fundraiser=None,
                    error=None)

    def post(self):
        title = self.get_argument('title', None)
        slug = self.get_argument('slug', None)
        goal = self.get_argument('goal', None)
        deadline = self.get_argument('deadline', None)
        description = self.get_argument('description', None)

        slug = unicodedata.normalize('NFKD', slug).encode('ascii', 'ignore')
        slug = re.sub(r'[^\w]+', ' ', slug)
        slug = slug.replace(' ', '_').lower().strip()

        fundraiser = {'title': title, 'slug': slug,
                      'goal': goal, 'deadline': deadline,
                      'description': description}

        if None in fundraiser.values():
            self.render('fundraiser/create.html', fundraiser=fundraiser,
                        error=1)

        if self.fundraisers.find_one({'slug': fundraiser['slug']}):
            self.render('fundraiser/create.html', fundraiser=fundraiser,
                        error=2)

        if self.fundraisers.find_one({'title': fundraiser['title']}):
            self.render('fundraiser/create.html', fundraiser=fundraiser,
                        error=3)

        fundraiser['launched'] = datetime.datetime.utcnow()
        fundraiser['current_funding'] = 0
        fundraiser['backers_count'] = 0

        self.fundraisers.save(fundraiser)
        self.redirect('{}'.format(slug))


class FundraiserEditHandler(FundraiserBase):

    def get(self, fundraiser_slug):
        fundraiser = self.fundraisers.find_one({'slug': fundraiser_slug})
        if fundraiser:
            self.render('fundraiser/detail.html',
                        fundraiser=fundraiser)
        else:
            raise HTTPError(404)


class FundraiserDeleteHandler(FundraiserBase):

    def get(self, fundraiser_slug):
        fundraiser = self.fundraisers.find_one({'slug': fundraiser_slug})
        if fundraiser:
            self.fundraisers.remove(fundraiser)
            self.redirect('/admin')
        else:
            raise HTTPError(404)


class FundraiserDetailHandler(FundraiserBase):

    def get(self, fundraiser_slug):
        fundraiser = self.fundraisers.find_one({'slug': fundraiser_slug})
        if fundraiser:
            self.render('fundraiser/detail.html',
                        fundraiser=fundraiser)
        else:
            raise HTTPError(404)


class FundraiserBackHandler(FundraiserBase):

    def get(self, fundraiser_slug):
        fundraiser = self.fundraisers.find_one({'slug': fundraiser_slug})
        if fundraiser:
            self.render('fundraiser/back.html',
                        fundraiser=fundraiser)
        else:
            raise HTTPError(404)


# class FundraiserBackResponseHandler(HTTPParseBody):

#     def __call__(self):
#         self.stream.read_bytes(self.content_length, self.parse_json)

#     def parse_json(self, data):
#         print data
#         try:
#             json_data = json.loads(data)
#         except ValueError:
#             raise tornado.httpserver._BadRequestException(
#                 "Invalid JSON structure."
#             )
#         if type(json_data) != dict:
#             raise tornado.httpserver._BadRequestException(
#                 "We only accept key value objects!"
#             )
#         for key, value in json_data.iteritems():
#             self.request.arguments[key] = [value,]
#             self.done()
class FundraiserBackResponseHandler(FundraiserBase):

    def prepare(self):
        if self.request.headers.get("Content-Type") == "application/json":
            self.json_args = json_decode(self.request.body)

    def post(self):

        #self.json_args.get("foo")
        self.write(self.json_args)


class FundraiserDetailJSONHandler(FundraiserBase):

    def get(self, fundraiser_slug):
        fundraiser = self.fundraisers.find_one({'slug': fundraiser_slug})
        if fundraiser:
            datetime_handler = lambda obj: obj.isoformat() if isinstance(obj, datetime.datetime) else None
            self.set_header('Content-Type', 'application/json')
            self.write(json.dumps(fundraiser, default=datetime_handler))
        else:
            raise HTTPError(404)
