import sys

__author__ = 'czy-thinkpad'
import SimpleHTTPServer
import SocketServer
import os

PORT = 3722
WEBROOT = 'C:/'
class PortHandler(SimpleHTTPServer.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        os.chdir(WEBROOT)
        return SimpleHTTPServer.SimpleHTTPRequestHandler.translate_path(self, path)

httpd = None
def start():
    try:
        httpd = SocketServer.TCPServer(("", PORT), PortHandler)
        httpd.serve_forever()
    except:
        pass
    pass
def end():
    httpd.shutdown()
    pass

if __name__ == '__main__':
    print 'ok'
    if len(sys.argv) > 1 and os.path.exists(sys.argv[1]):
        WEBROOT = sys.argv[1]
        print 'start'
        start()