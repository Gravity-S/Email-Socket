import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.bind((host, port))
s.listen(5)
while True:
    connect,addr = s.accept()
    print(connect," ",addr)