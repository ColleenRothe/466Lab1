from bottle import get, run, request, response, route, template, Bottle
import sys
import http.client
import urllib
from urllib import parse

#test integer:
#http://stackoverflow.com/questions/5424716/python-how-to-check-if-input-is-a-number

#how to do the table
#http://www.w3schools.com/tags/tag_tr.asp

#accept port and file for the board
port = sys.argv[1]
file = sys.argv[2]

# sink stuff
class Sink:
    def __init__(self,cn,bn,rn,sn,dn):
        self.c=cn
        self.b=bn
        self.r=rn
        self.s=sn
        self.d=dn

nums = Sink(0,0,0,0,0)

#create own board
ownboard = []
board = open(file)
for i in range(0,10):
    row = board.readline().strip('\n') #newline creating probs
    ownboard.append([]) #2D
    for thing in row:
        ownboard[i].append(thing)

#create opponent board
opponentboard = [['_' for n in range(0,10)] for n in range (0, 10)]

#start bottle
app = Bottle()

#need to deal with:
#out of bounds: HTTP Not Found
#already fired upon: HTTP Gone
#bad format: HTTP Bad Request (not an int?)
@app.post('/')
def process_action():
    x=request.POST['y'] #need to be opposite
    y=request.POST['x']

    try: #have to do first so it can be int for the rest
        x=int(x)
        y=int(y)
    except ValueError:
        print("GOT Here First")
        response.status = 400 #bad request
        return
    if x == '10' or y>=10 or x<0 or y<0:
        print("GOT HERE")
        response.status = 404 #out of bounds
        return
    #look at board
    if ownboard[x][y] == "_":
        #miss
        ownboard[x][y] = "O" #nothing there
        return parse.urlencode({'hit': 0})
    elif ownboard[x][y] == "O" or ownboard[x][y] == "X":
        #already hit there 410 gone
        response.status = 410
        return
    else:
        #hit something

        if ownboard[x][y] == "C":
            nums.c +=1
        elif ownboard[x][y] == "B":
            nums.b +=1
        elif ownboard[x][y] == "R":
            nums.r +=1
        elif ownboard[x][y] == "S":
            nums.s +=1
        elif ownboard[x][y] == "D":
            nums.d +=1

        #hit
        ownboard[x][y] = "X"

        if nums.c== 5:
            return parse.urlencode({'hit':1, 'sink':'C'})
        elif nums.b == 4:
             return parse.urlencode({'hit':1, 'sink':'B'})
        elif nums.r == 3:
             return parse.urlencode({'hit':1, 'sink':'R'})
        elif nums.s== 3:
             return parse.urlencode({'hit':1, 'sink':'S'})
        elif nums.d == 2:
             return parse.urlencode({'hit':1, 'sink':'D'})
        else:
            return parse.urlencode({'hit':1})
#doesn't exactly work
@app.post('/sendback')
def do_opponent():
    y=request.POST['x']
    x=request.POST['y']
    hit=request.POST['hit']
   #copy same stuff from above
    try: #have to do first so it can be int for the rest
        x=int(x)
        y=int(y)
    except ValueError:
        print("GOT UP HERE")
        response.status = 400 #bad request
        return
    if x == '10' or y>=10 or x<0 or y<0:
        print("GOT HERE")
        response.status = 404 #out of bounds
        return
    #look at board...
    if(hit == '0'): #miss
        opponentboard[x][y] = 'O'
    else:
        opponentboard[x][y] = 'X' #hit
#show own board
@app.get('/own_board.html')
def own_board(): #<tr> = row containing 1+ <td>elements
    board = "Your Own Board <table>" #start table
    for i in range(0,10):
        board +=str("<tr>") #new row
        for j in range(0,10):
            board +=str("<td>") + str(ownboard[i][j]) + str("<td>") #new thing
        board +=str("</tr>") #new row
    board += str("<table>") #end table
    return board

#show opponent board
@app.get('/opponent_board.html')
def opponent_board(): #<tr> = row containing 1+ <td>elements
    board = "Opponent Board <table>" #start table
    for i in range(0,10):
        board +=str("<tr>") #new row
        for j in range(0,10):
            board +=str("<td>") + str(opponentboard[i][j]) + str("<td>") #new thing
        board +=str("</tr>") #new row
    board += str("<table>") #end table
    return board


run(app, host='0.0.0.0', port=port) #only one run for all
