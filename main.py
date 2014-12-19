from twisted.web.resource import Resource
from twisted.web.server import Site
from twisted.internet import reactor, endpoints

from route import ROUTE


class Main(Resource):
    isLeaf = False

    def __init__(self):
        Resource.__init__(self)
        for path in ROUTE:
            self.putChild(path, ROUTE[path])


endpoints.serverFromString(reactor, "tcp:8080").listen(Site(Main()))
reactor.run()