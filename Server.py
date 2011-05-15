__author__ = 'czy-thinkpad'
import SimpleHTTPServer
import SocketServer
import os

PORT = 8800
WEBDIR = "c:/"

class PortHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
        def translate_path(self,path):
                os.chdir(WEBDIR)
                return SimpleHTTPServer.SimpleHTTPRequestHandler.translate_path(self,path)

httpd = None
def start():
    try:
        httpd = SocketServer.TCPServer(("", PORT), PortHandler)
        print 'dir %s serving at port %s' % (repr(WEBDIR), PORT)
        httpd.serve_forever()
    except:
        pass
    pass
def end():
    httpd.shutdown()
    pass