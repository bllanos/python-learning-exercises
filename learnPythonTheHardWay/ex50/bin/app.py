import web

urls = (
    '/', 'Index'
)

app = web.application(urls, globals())

class Index(object):
    def GET(self):
        greeting = "Hello World"
        return greeting

if __name__ == "__main__":
    app.run()
