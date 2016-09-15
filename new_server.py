
import httplib, sys
from socket import *
global gameBoard


file = sys.argv
y = int(file[1])
x = file[2]


with open(x) as file_object:
	gameBoard = [[n for n in line.split()] for line in file_object]
	for r in gameBoard:	
		for m in r:
			print(m)


serverSocket = socket(AF_INET,SOCK_STREAM)
serverSocket.bind(('localhost', y))
serverSocket.listen(1)
##push board to web
# conn=httplib.HTTPConnection('google.com')
# conn.request("GET", "/pathto/object.jpg")
# r = conn.getresponse()
# data = r.read()
# conn.close()
print 'The server is ready to receive'
########HTTP Stuff
while 1:
	connectionSocket, addr = serverSocket.accept()
	sentence = connectionSocket.recv(1024)
	capitalizedSentence = sentence.upper()
	connectionSocket.send(capitalizedSentence)
	connectionSocket.close()
