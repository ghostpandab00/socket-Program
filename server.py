import socket

s = socket.socket()
print("Socket created")

s.bind(('localhost', 9999))

s.listen(5)
print("waiting for connections...")

while True:
    c, addr = s.accept()
    print("Connected with ", addr)

    c.send(bytes("Connected to server ".encode()))

    c.close()