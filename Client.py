#!/usr/bin/env python3
import socket
import json

HOST, PORT = "localhost", 9527

f=open("config.json")
data = json.loads(f.read())
f.close()

# data = {
#     "method": "mkdir /tmp/temp_file",
#     "id": "242c41d4-2cc5-4cfb-b815-89e33862e125"
# }

# Create a socket (SOCK_STREAM means a TCP socket)
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    # Connect to server and send data
    client.connect((HOST, PORT))
    client.send(bytes(json.dumps(data), 'UTF-8'))

    # Receive data from the server and shut down
    received = client.recv(1024).decode('UTF-8')
finally:
    client.close()

print ("Sent: {}".format(data))
print ("Received: {}".format(received))