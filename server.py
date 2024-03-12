#!/usr/bin/env python
from http.server import HTTPServer, SimpleHTTPRequestHandler 
import ssl
httpd = HTTPServer(('0.0.0.0', 443), SimpleHTTPRequestHandler)
httpd.socket = ssl.wrap_socket(
    httpd.socket,
    keyfile="key.pem",
    certfile='cert.pem',
    server_side=True)
httpd.serve_forever()

# password: jebigadojaja
