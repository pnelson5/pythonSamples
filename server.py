from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sys

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        print('GET %s' % self.path)
        self.send_response(200)
        self.send_header("Content-type", "application/json")
        self.end_headers()
        out = json.dumps({'status':'UP'})
        self.wfile.write(out.encode("utf-8"))
        self.wfile.close

if __name__ == '__main__':
    port = 8000
    if len(sys.argv) > 1:
        port = int(sys.argv[1])
    HTTPServer(('localhost', port), MyServer).serve_forever()
