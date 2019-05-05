import webapp2
from webapp2_extras import jinja2
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
                data = {"name": character.name,
                        "description": character.description}
            else:
                self.redirect("/")
        except:
            data = {"name": "",
                    "description": ""}
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("character.html", **data))

    def post(self):
        try:
            character = Character.get_by_id(int(self.request.uri[-16:]))
            character.name = self.request.get("name")
            character.description = self.request.get("description")
            character.put()
        except:
            Character(
                user_id=users.get_current_user().user_id(),
                name=self.request.get("name"),
                description=self.request.get("description")
            ).put()
        time.sleep(0.1)
        self.redirect("/")


app = webapp2.WSGIApplication([("/character.*", MainHandler)], debug=True)
