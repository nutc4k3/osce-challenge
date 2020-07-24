from boofuzz import *

ip = "192.168.15.172"
port = 80

#template https://github.com/jtpereyda/boofuzz-http/blob/master/fuzz_http.py

def main():
	session = Session(
		target = Target(
			connection = SocketConnection(ip, port, proto='tcp')
		),
	)
	s_initialize(name="Request")
	with s_block("Request-Line"):
		s_group("Method", ['GET', 'HEAD', 'POST', 'PUT', 'DELETE', 'CONNECT', 'OPTIONS', 'TRACE'])
		s_delim(" ", name='space-1', fuzzable = False)
		s_string("/index.html", name='Request-URI')
		s_delim(" ", name='space-2', fuzzable = False)
		s_string('HTTP/1.1', name='HTTP-Version', fuzzable = False)
		s_static("\r\n", name="Request-Line-CRLF")
	s_static("\r\n", "Request-CRLF")

	session.connect(s_get("Request"))

	session.fuzz()


if __name__ == '__main__':
	main()