import webapp2
from webapp2_extras import jinja2
from google.appengine.api import users
from google.appengine.ext import ndb


class Character(ndb.Model):
    user_id = ndb.StringProperty(required=True)
    name = ndb.StringProperty(required=True)
    description = ndb.StringProperty(required=True)


class MainHandler(webapp2.RequestHandler):
    def get(self):
        characters = Character.query(Character.user_id == users.get_current_user().user_id())
        html = ""
        for character in characters:
            html += '<tr>' \
                        '<td>' \
                            '<a href="/character'+str(character.key.id())+'">'+character.name+'</a>' \
                        '</td>' \
                        '<td>' \
                            '<a href="/delete'+str(character.key.id())+'"><i class="material-icons">delete_forever</i></a>' \
                        '</td>' \
                    '</tr>'
        jinja = jinja2.get_jinja2(app=self.app)
        self.response.write(jinja.render_template("main.html") + html + "</table></div>")


app = webapp2.WSGIApplication([("/", MainHandler)], debug=True)
