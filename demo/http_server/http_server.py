import SimpleHTTPServer
import SocketServer

# 端口号小于7000，服务器无法启动成功
PORT = 8002

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler
httpd = SocketServer.TCPServer(("", PORT), Handler)
print "serving at port", PORT
httpd.serve_forever()
