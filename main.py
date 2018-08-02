#!/usr/bin/python
#
# Copyright 2018 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

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
import webapp2
import os
import random
import jinja2


def get_fortune():
    #add a list of fortunes to the empty fortune_list array
    fortune_list=['You will find great luck today, if you go out and search for it.', 
    'The world conspires against you, but if you stand your ground, you will be rewarded.', 
    'You will be challenged by your peers, and if you succeed, you shall earn their respect.',
    'Keep a look out for opportunities today, it might just define the rest of your life.',
    'Today is a good day to look for love. Someone\'s heart yearns for yours!',
    'Today is a good day to look to the future. Make a change that will impact you in the long term.',
    'Treat yourself today. You\'ve made it through some tough times.',
    'Try making something new, get your creative juices flowing. You never know what will come of it.']
    #use the random library to return a random element from the array
    random_fortune = fortune_list[random.randint(0, len(fortune_list)-1)]
    return(random_fortune)


#remember, you can get this by searching for jinja2 google app engine
jinja_current_directory = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class FortuneHandler(webapp2.RequestHandler):
    def get(self):
        fortune = get_fortune()
        # In part 2, instead of returning this string,
        # make a function call that returns a random fortune.
        fortune_template = (jinja_current_directory.get_template('templates/result.html'))
        sign = self.request.get("sign")
        fortune_dict = {'sign': sign, 'fortune':fortune}
        self.response.write(fortune_template.render(fortune_dict))
    #add a post method
    #def post(self):
    
    def post(self):
        fortune_template = (jinja_current_directory.get_template('templates/result.html'))
        sign = self.request.get("sign")
        fortune = get_fortune()
        fortune_dict = {'sign': sign, 'fortune':fortune}
        self.response.write(fortune_template.render(fortune_dict))

class HelloHandler(webapp2.RequestHandler):
    def get(self):
        template = (jinja_current_directory.get_template('templates/welcome.html'))
        self.response.write(template.render())
        
class GoodbyeHandler(webapp2.RequestHandler):
    def get(self):
        self.response.write('My response is Goodbye World.')

#the route mapping
app = webapp2.WSGIApplication([
    #this line routes the main url ('/')  - also know as
    #the root route - to the Fortune Handler
    ('/', HelloHandler),
    ('/predict', FortuneHandler),#maps '/predict' to the FortuneHandler
    ('/farewell', GoodbyeHandler)
], debug=True)
