#!/usr/bin/env python3
#
# The *hello server* is an HTTP server that responds to a GET request by
# sending back a friendly greeting.  Run this program in your terminal and
# access the server at http://localhost:8000 in your browser.

#import module
from http.server import HTTPServer, BaseHTTPRequestHandler

#define handler class that inherits from BaseHTTPRequestHandler
class HelloHandler(BaseHTTPRequestHandler):
    #first method:
    # When the web server receives a GET request,
    # it will call this method to respond to it.
    def do_GET(self):
        # First, send status code:
        # a 200 OK response.
        self.send_response(200)

        # Then send headers.
        self.send_header('Content-type', 'text/plain; charset=utf-8')
        self.end_headers()

        # Now, write the response body.
        #self.wfile.write() is passed a bytes object
        # -->need to encode the string into a byte object!
        self.wfile.write("Hello, HTTP!\n".encode())

if __name__ == '__main__':
    server_address = ('', 8000)  # Serve on all addresses, port 8000.
    httpd = HTTPServer(server_address, HelloHandler)
    httpd.serve_forever()
