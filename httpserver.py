import datetime
import BaseHTTPServer

class RequestHandler(BaseHTTPServer.BaseHTTPRequestHandler):
	def do_GET(self):
		self.send_response(200)
		self.end_headers()
		self.wfile.write("The current time is " + str(datetime.datetime.now()))

def run_httpserver():

	PORT = 8000

	httpd = BaseHTTPServer.HTTPServer(("", PORT), RequestHandler)

	print "serving at port", PORT
	httpd.serve_forever()

if __name__ == '__main__':
	run_httpserver()