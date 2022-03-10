#!/usr/bin/python3

import socket

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 4444

serversocket.bind((host, port))

serversocket.listen(3)

while True:
    clientsocket,address = serversocket.accept()

    print("Received connection from: %s " % str(address))

    message = "Hello, Thank you for connection to the server!" + "\r\n"

    clientsocket.send(message.encode('ascii'))

    clientsocket.close()