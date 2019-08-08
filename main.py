import webapp2
import jinja2
import os
import json
from urllib import urlencode
from google.appengine.api import urlfetch

the_jinja_env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPageHandler(webapp2.RequestHandler):
    def get(self):
        form_template = the_jinja_env.get_template('templates/main.html')
        self.response.write(form_template.render())

# class RecipeDisplayHandler(webapp2.RequestHandler):
#     def post(self):
#         query = self.request.get('query')
#         base_url = 'http://www.recipepuppy.com/api/?'
#         params = { 'q': query}
#         response = urlfetch.fetch(base_url + urlencode(params)).content
#         results = json.loads(response)

#         result_template = the_jinja_env.get_template('templates/recipe.html')
#         self.response.write(result_template.render({
#             'results': results
#         }))


app = webapp2.WSGIApplication([
    ('/', MainPageHandler)
], debug=True)