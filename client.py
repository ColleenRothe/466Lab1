import sys
import urllib
#import httplib
import http.client

#accept IP address, port, x, y

ipadd = sys.argv[1]
port = sys.argv[2]
x = sys.argv[3]  
y = sys.argv[4]

#body data
params = urllib.parse.urlencode({'x':x, 'y':y})
headers = {"Content-type": "application/x-www-form-urlencoded", "Content-length": "7"}
conn = http.client.HTTPConnection(ipadd, port)
conn.request("POST", "", params, headers)
response = conn.getresponse()
print(response.status, response.reason)
answer = str(response.read())
print(answer)
#look for each part of message in the answer
#message will be hit=1(hit) or 0(miss). if sink, also sink=C,B,R,S,D

#Following each result, client should update the record of the player's shots
#onto the opponent's board??...need to send back to server to update?

for thing in answer:
    if thing == '0':
        #you missed it
        param = urllib.parse.urlencode({'x': x, 'y': y , 'hit': '0'})
        #send back to server to update the opponent board
        headers = {"Content-type": "application/x-www-form-urlencoded", "Content-length": "13"} #update length!!
        conn.request("POST", "/sendback", param, headers)
    if thing == '1':
        #you hit it
        param = urllib.parse.urlencode({'x': x, 'y': y, 'hit': '1'})
        #send back to server to update the opponent board
        headers = {"Content-type": "application/x-www-form-urlencoded", "Content-length": "13"} #update length!
        conn.request("POST", "/sendback", param, headers)
  
conn.close() #close connection

