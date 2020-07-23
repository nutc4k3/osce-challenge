from boofuzz import *

ip = "192.168.15.172"
port = 9999

#crashed at 5011

def main():

	session = Session(
		target = Target(
			connection = SocketConnection(ip,port, proto='tcp')))

	s_initialize("gmon")
	s_string("GMON", fuzzable = False)
	s_delim(" ", fuzzable = False)		
	s_string("FUZZ")

	session.connect(s_get("gmon"))
	session.fuzz()

if __name__ == "__main__":
	main()