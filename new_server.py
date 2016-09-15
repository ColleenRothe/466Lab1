

from socket import *
serverName = 'localhost'
serverPort = 4000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
#####HTTP Stuff
import urllib
params= urllib.urlencode(
	{'spam': 1, 'eggs': 2, 'bacon': 0})
f = urllib.urlopen("http://srvr.com/cgi-bin/query?%s" % params)
data = f.read()

sentence = raw_input('Input lowercase sentence:')
clientSocket.send(sentence)
modifiedSentence = clientSocket.recv(1024)
print 'From Server:', modifiedSentence
clientSocket.close()
