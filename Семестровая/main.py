#!/usr/bin/python3

from http.server import HTTPServer, BaseHTTPRequestHandler
import ssl
import json

import bot

class ReqHandler(BaseHTTPRequestHandler):
    b = bot.Bot();

    def do_POST(s):
        length = int(s.headers.get('Content-Length'))
        #print("length:",length)
        post = s.rfile.read(length).decode("utf-8")
        data=json.loads(post)
        response = s.b.request(data)        

        s.send_response(200)
        s.send_header("Content-type", "application/json")
        s.end_headers()
        s.wfile.write(bytearray(response,'utf-8'))



httpd = HTTPServer(('', 80), ReqHandler)
#httpd.socket = ssl.wrap_socket (httpd.socket, certfile='./ssl/server.pem', server_side=True)
httpd.serve_forever()
