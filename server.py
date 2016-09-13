#server.py
#import bottle
from bottle import route, run, template

##Just playing with this stuff to show the board...
##not actually sure where it should go
##http://bottlepy.org/docs/dev/tutorial.html#quickstart-hello-world


##@route('/own_board.html')
##def own_board():
##    return "Hello World!"
##run(host='localhost', port=5000)

@route('/opponent_board.html')
def opponent_board():
    return "Hello World!"
run(host='localhost', port=5000)



