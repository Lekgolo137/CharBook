import webapp2
from google.appengine.api import users


class MainHandler(webapp2.RequestHandler):
    def get(self):
        if users.get_current_user():
            self.redirect(users.create_logout_url("/"))
        else:
            self.redirect("/")


app = webapp2.WSGIApplication([("/logout", MainHandler)], debug=True)
