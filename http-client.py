#used tutorials from tutorialspoint.com to complete code

import sys, httplib,urllib
global gameBoard

def estConnection(address, portnum, X, Y):
    host = address
    port = portnum
    h = httplib.HTTPConnection(address, port)
    h.connect()
    outmessage = makeMessage(X,Y)
    h.request(outmessage)
    inmessage = h.getResponse(4096)
    error, hit, sink = readMessage(inmessage)
    if error == 0:
        updateBoard(X, Y, hit)
    h.close()

def makeMessage(X,Y):
    params = urllib.urlencode({'@x':X,'@y':Y})
    message = "POST", "", params
    return message

def readMessage(message):
   error = 0                   # 0 none, 1 out of bounds, 2 already fired at
   hit = False                 # True hit, False miss
   sink = 0                    # 0 no sink, C, B, R, S, D sunk ship
#TO-DO read HTTP message
   return error, hit, sink

def updateBoard(X, Y, hit):
    if hit:
        gameBoard[X][Y] = 'X'
    else:
        gameBoard[X][Y] = 'O'
    makeHTMLdoc()

def makeHTMLdoc():
   htmlfile = open('opponent_board.html','w')
   htmlfile.write("""<html>
   <head></head>
   <body><p>Hello World!</p>
   <table>""")
   for i in range(0,10):
       htmlfile.write("""<tr>""")
       for j in range(0,10):
           htmlfile.write("""<td>"""+str(gameBoard[i][j])+"""</td>""")
       htmlfile.write("""</tr>""")
   htmlfile.write("""</table></body>
   </html>""")

   htmlfile.close()


# this is the 'main'--------------------------------------------------------
IPadd = sys.argv[1]
port = int(sys.argv[2])
X = int(sys.argv[3])
Y = int(sys.argv[4])
gameBoard = [['~' for n in range(0,10)] for n in range (0, 10)]
makeHTMLdoc()
makeConnection(IPadd, port, X, Y)
