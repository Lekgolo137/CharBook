import webapp2
from google.appengine.api import users
from google.appengine.ext import ndb
import time


class Character(ndb.Model):
    user_id = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        try:
            character = Character.get_by_id(int(self.request.uri[-16:]))
            if character.user_id == users.get_current_user().user_id():
                character.key.delete()
            time.sleep(0.1)
        except:
            pass
        self.redirect("/")


app = webapp2.WSGIApplication([("/delete.*", MainHandler)], debug=True)
