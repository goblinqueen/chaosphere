#!/usr/bin/env python
#
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
import random
import webapp2
import yaml


def roll(chaos):
    card = random.choice(chaos)
    if card['value']:
        picture_number = random.choice(card['value'])
    else:
        picture_number = 0
    picture = '/images/%s.jpg' % picture_number
    return """
    <center><h2>%s</h2>
    <img src=%s />
    </center>
    """ % (card['name'], picture)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        chaos_field = yaml.load(open('chaos.yaml', 'r'))
        self.response.write(roll(chaos_field))


app = webapp2.WSGIApplication([
    ('/', MainHandler)
], debug=True)
