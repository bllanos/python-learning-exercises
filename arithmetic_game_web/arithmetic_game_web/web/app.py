import web

web.config.debug = False

urls = (
    '/', 'Index'
)

app = web.application(urls, locals())
store = web.session.DiskStore('sessions')
session = web.session.Session(app, store, initializer={})

class Index(object):
    def GET(self):
        web.seeother('/static/index.html')

if __name__ == "__main__":
    app.run()
