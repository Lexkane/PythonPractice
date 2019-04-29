import time
from http.server import BaseHTTPRequestHandler,HTTPServer

HOST_NAME='localhost'
PORT_NUMBER=8080

class MyHander(BaseHTTPRequestHandler):
	def do_HEAD(s):
		s.send_responce(200)
		s.send_header('Content-type','text/html')
		s.end_headers()
	def do_GET(s):
		'''Respond to a GET request'''
		s.send_responce(200)
		s.send_header('Content-type','text/html')
		s.end_headers()
		s.wfile.write(b'<html><head><title>Title goes here.</title></head>')
		s.wfile.write(b'<body><p>This is test body.</p>')
		s.wfile.write(b'<p> You accessed path:{}</p>'.format(s.path.ecode()))
		s.wfile.write(b'</body></htnl>)
		
		if __name__=='__main__':
			server_class=HTTPServer
			httpd=server_class((HOST_NAME,PORT_NUMBER),MyHander)
			print(time.asctime(),f"Server Starts- {HOST_NAME}:{PORT_NUMBER}")
			try:
				httpd.serve_forever()
			exept KeyboardInterrupt:
				pass
			httpd.server_close()
			print(time.asctime(),f'Server Stops- {HOST_NAME}:{PORT_NUMBER})