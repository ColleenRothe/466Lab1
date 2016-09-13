#server.py
#import bottle
from bottle import route, run, template

##Just playing with this stuff to show the board...
##not actually sure where it should go
##http://bottlepy.org/docs/dev/tutorial.html#quickstart-hello-world

##goes to either
@route('/<board>')
def go(board):
    if(board == 'own_board.html'):
        return "Hello Own"
    elif(board == 'opponent_board.html'):
        return "Hello Opponent"
run(host='localhost', port=5000)





