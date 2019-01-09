from twisted.web import server, resource
from twisted.internet import reactor, endpoints


class Index(resource.Resource):
    isLeaf = True
    def render_GET(self, request):
        request.setHeader(b"content-type", b"text/plain")
        content = "Hello"
        return content.encode("ascii")

endpoints.serverFromString(reactor, "tcp:8080").listen(server.Site(Index()))
reactor.run()
