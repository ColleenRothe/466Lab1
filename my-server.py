#used a tutorial from tutorialspoint.com

import socket, sys, httplib
global gameBoard

def makeConnection(portnum):
   s = socket.socket()
   host = socket.gethostname()
   port = portnum
   s.bind((host, port))
   s.listen(1)                 # listen for connection from client
   while True:
      conn, address = s.accept()
      inmessage = conn.recv(4096) # HTTP POST request from client
      X, Y = receiveMessage(inmessage)
      if X >= 0:               # if message is not formatted correctly can't update board
         error, hit, sink = updatePlayerBoard(X,Y)
      else:
         error, hit, sink = 3, False, 0

      outmessage = sendResult(error, hit, sink)
      conn.send(outmessage)    # HTTP respone message to client
      conn.close()             # close connection

def receiveMessage(message):   # takes in the message received by the socket
   X = 0
   Y = 0
   data = message.get_data()
# TO-DO read in message data and gather X,Y coords
# return X = -1 if message not formatted correctly
   return X, Y                 # returns the integer values of the fire coord

def updatePlayerBoard(X, Y):   # takes in the int coords being fired on
   error = 0                   # 0 none, 1 out of bounds, 2 already fired at
   hit = False                 # True hit, False miss
   sink = 0                    # 0 no sink, C, B, R, S, D sunk ship
   if X < 0 or Y < 0 or X > 9 or Y > 9:
      error = 1                # coord do not exist on board
   elif gameBoard[X][Y] == 'X' or gameBoard[X][Y] == 'O':
      error = 2                # coord already fired at
   elif gameBoard[X][Y] == '~':
      hit = False
      gameBoard[X][Y] = 'O'    # update board to show it was a miss
   else:
      hit = True               # it was a hit
      ship = gameBoard[X][Y]   # this is the ship that was hit
      gameBoard[X][Y] = 'X'    # update to show it was a hit

      sink = ship              # assume that the hit was a sink
      for r in gameBoard:      # go through all other positions on board to prove other wise
         for m in r:
            if m == ship:
               sink = 0
               break
   makeHTMLdoc()
   return error, hit, sink     # returns what type if any error occured, hit/miss, and what sunk

def sendResult(error, hit, sink):
   message = 'blah'
#TO-DO format message
   return message

def createBoard(filename):
   with open(filename) as file_object:
      gameBoard = [[n for n in line] for line in file_object]

def makeHTMLdoc():
   htmlfile = open('own_board.html','w')

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
port = int(sys.argv[1])     # use port given from command line
boardname = sys.argv[2]     # use board give from command line
createBoard(boardname)
makeHTMLdoc()
makeConnection(port)
