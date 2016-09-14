#server.py
#import bottle
from bottle import route, run, template, static_file

##Just playing with this stuff to show the board...
##not actually sure where it should go
##http://bottlepy.org/docs/dev/tutorial.html#quickstart-hello-world

#opponent board

#own board
global gameBoard
def print_board(gameBoard):
	for r in gameBoard:	
		for x in r:
			print(x)


with open ('board.txt') as file:
	gameBoard = [[n for n in line.split()] for line in file]
	print_board(gameBoard)


##goes to either
@route('/<board>')
def go(board):
    if(board == 'own_board.html'):
        #return "Hello Own"
        #return gameBoard
        return static_file('board.txt', root='')
    elif(board == 'opponent_board.html'):
        return "Hello Opponent"
run(host='localhost', port=5000)





