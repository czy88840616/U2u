__author__ = 'czy-thinkpad'
import SimpleHTTPServer
import SocketServer
import os

PORT = 8800

class PortHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        os.chdir(WEBROOT)
        return SimpleHTTPServer.SimpleHTTPRequestHandler.translate_path(self, path)

httpd = None
def start(WEBDIR):
    global WEBROOT
    WEBROOT = WEBDIR
    try:
        httpd = SocketServer.TCPServer(("", PORT), PortHandler)
        httpd.serve_forever()
    except:
        pass
    pass
def end():
    httpd.shutdown()
    pass