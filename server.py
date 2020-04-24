from http.server import HTTPServer, BaseHTTPRequestHandler


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def __init__(self):

    def doGet(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'HELLO WORLD')

httpd = HTTPServer(('localhost',8000), SimpleHTTPRequestHandler)
httpd.serve_forever()
