import http.server

class RequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        return http.server.SimpleHTTPRequestHandler.do_GET(self)
handler = RequestHandler

PORT = 8000

server = http.server.HTTPServer(("",PORT), handler)
server.serve_forever()