import web
from ..game_logic.game import QUIT

web.config.debug = False

urls = (
    '/', 'Index'
)

app = web.application(urls, locals())
store = web.session.DiskStore('sessions')
session = web.session.Session(app, store, initializer={})
render = web.template.render('templates')

class Index(object):
    def GET(self):
        return render.index(QUIT)

def main():
    app.run()

__all__ = [main]
