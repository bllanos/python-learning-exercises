import web
from ..game_logic.game import QUIT, run_game
from serialization import GameOutputJSONEncoder
from uuid import uuid4

web.config.debug = False

urls = (
    '/', 'Index',
    '/game', 'Game'
)

app = web.application(urls, locals())
store = web.session.DiskStore('sessions')
# The contents of sessions are a workaround for the fact that live generators
# cannot be serialized (i.e. to be stored in sessions).
# See http://grokbase.com/t/python/python-bugs-list/112qmspt71/issue11299-allow-deepcopying-and-pickling-paused-generators
# Had I known, I would have used some means other than generators to store state.
session = web.session.Session(app, store, initializer={'sessionId': uuid4()})
render = web.template.render('templates')
encoder = GameOutputJSONEncoder()

generators = {}
# Keeps track of which users have visited the index page before
# playing the game, while the server was running.
goodSessions = {}

class Index(object):
    def GET(self):
        sessionId = session.sessionId
        if not (sessionId in goodSessions):
            goodSessions[sessionId] = True
        return render.index(QUIT)

class Game(object):
    def POST(self):
        data = web.input(text=None)
        sessionId = session.sessionId
        gen = None
        if not (sessionId in generators):
            gen = run_game()
            generators[sessionId] = gen
            output = gen.next()
            if not((sessionId in goodSessions) or output.error):
                output.error = "We lost track of your progress. \
                    You are starting over, sorry :("
        else:
            gen = generators[sessionId]
            output = gen.send(data.text)

        web.header('Content-Type', 'application/json')
        return encoder.encode(output)

def main():
    app.run()

__all__ = [main]
