#client.py
import sys
import urllib
#import httplib
import http.client

#accept IP address, port, x, y

ipadd = sys.argv[1]
port = sys.argv[2]
x = sys.argv[3] #need to be ints to do the testing
y = sys.argv[4]

#body data
params = urllib.parse.urlencode({'x':x, 'y':y})
headers = {"Content-type": "application/x-www-form-urlencoded", "Content-length": "7"}
conn = http.client.HTTPConnection(ipadd, port)
conn.request("POST", "", params, headers)
response = conn.getresponse()
print("RESPONSE IS")
print(response.status, response.reason)
answer = str(response.read())
print("ANSWER IS")
print(answer)
#look for each part of message in the answer
#message will be hit=1(hit) or 0(miss). if sink, also sink=C,B,R,S,D

#Following each result, client should update the record of the player's shots
#onto the opponent's board??...need to send back to server to update?

for thing in answer:
    if thing == '0':
        #you missed it
        print("miss")
        params = urllib.parse.urlencode({'x': x, 'y': y, 'hit': '0'})
    if thing == '1':
        #you hit it
        print("hit")
        params = urllib.parse.urlencode({'x': x, 'y': y, 'hit': '0'})
    #rest of the prints to test
    if thing == 'C':
        print("carrier sunk")
    if thing == 'B':
        print("battleship sunk")
    if thing == 'R':
        print("cRuiser sunk")
    if thing == 'S':
        print("submarine sunk")
    if thing == 'D':
        print("destroyer sunk")

#conn = http.client.HTTPConnection('localhost', port) #new connection?
conn.request("POST", "/sendback", params, headers) #send stuff back
conn.close #close connection


    
    


