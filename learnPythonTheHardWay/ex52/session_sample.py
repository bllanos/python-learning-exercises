# pip install web.py
import web

# Sessions do not work in debug mode
# http://webpy.org/cookbook/sessions
web.config.debug = False

# Must be a tuple, not a dictionary, for some reason
urls = (
    "/count", "count",
    "/reset", "reset"
)

app = web.application(urls, locals())
store = web.session.DiskStore('sessions')
session = web.session.Session(app, store, initializer={'count':0})

class count:
    def GET(self):
        # count = session.get('count', 1)
        # session['count'] = count + 1
        # return str(count)
        session.count += 1
        return str(session.count)

class reset:
    def GET(self):
        session.kill()
        return "Cleared"

if __name__ == "__main__":
    app.run()
