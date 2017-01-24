#!/usr/bin/env python

# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import urllib
import os
import webapp2
import jinja2

from google.appengine.api import users
from google.appengine.ext import ndb
from note_content import master_list

template_dir = os.path.join(os.path.dirname(__file__), 'templates')
jinja_env = jinja2.Environment(loader = jinja2.FileSystemLoader(template_dir))


class Handler(webapp2.RequestHandler):
  def write(self, *a, **kw):
    self.response.out.write(*a, **kw)

  def render_str(self, template, **params):
    t = jinja_env.get_template(template)
    return t.render(params)

  def render(self, template, **kw):
    self.write(self.render_str(template, **kw))

class Info(ndb.Model):
  author = ndb.StringProperty(indexed=False)
  comment = ndb.StringProperty(indexed=False)
  date = ndb.DateTimeProperty(auto_now_add=True)

class MainPage(Handler):
  def get(self):
    error = self.request.get('error', '')

    query = Info.query().order(-Info.date)
    info_list = query.fetch()

    self.render("stage_4_notes.html", master_list = master_list, info_list = info_list, error = error)

  def post(self):

      comment = self.request.get('comment')
      if comment:
        info = Info(comment=comment)
        info.put()
        self.redirect('/')
      else:
        self.redirect('/?error=Please enter a valid comment!')

app = webapp2.WSGIApplication([
    ('/', MainPage)
], debug=True)

