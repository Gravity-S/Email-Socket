import socket


print("Local Smtp Server start running!")
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 25
s.bind((host, port))

while True:
    s.listen(1000)
    c, addr = s.accept()  # 93

    client_msg = c.recv(1024).decode()  # 97
    if 'HELO' not in client_msg:
        c.send('500: ERROR!'.encode('utf-8'))
        c.close()
        continue
    print('recv: ' + client_msg)
    c.send('250 This is local mail server\r\n'.encode('utf-8'))  # 98

    client_msg = c.recv(1024).decode()  # 101
    if 'MAIL FROM:<' not in client_msg:
        c.send('500: ERROR!'.encode('utf-8'))
        c.close()
        continue
    print('recv: ' + client_msg)
    c.send('250 Ok\r\n'.encode('utf-8'))  # 102

    client_msg = c.recv(1024).decode()  # 105
    if 'RCPT TO:<' not in client_msg:
        c.send('500: ERROR!'.encode('utf-8'))
        c.close()
        continue
    print('recv: ' + client_msg)
    c.send('250 Ok\r\n'.encode('utf-8'))  # 106

    client_msg = c.recv(1024).decode()  # 109
    if client_msg != 'DATA\r\n':
        c.send('500: ERROR!'.encode('utf-8'))
        c.close()
        continue
    print('recv: ' + client_msg)
    c.send('354 Start mail input; end with<CRLF>.<CRLF>'.encode('utf-8'))  # 110

    client_msg = c.recv(1024).decode()  # 119
    c.send('ACK'.encode('utf-8'))
    print('recv: ' + client_msg)

    client_msg = c.recv(1024).decode()  # 119
    c.send('ACK'.encode('utf-8'))
    print('recv: ' + client_msg)

    client_msg = c.recv(1024).decode()  # 119
    if client_msg != '\r\n.\r\n':
        c.send('500: ERROR!'.encode('utf-8'))
        c.close()
        continue
    print('recv: ' + client_msg)
    c.send('250 OK'.encode('utf-8'))

    client_msg = c.recv(1024).decode()  # 119
    if client_msg != 'QUIT\r\n':
        c.send('500: ERROR!'.encode('utf-8'))
        c.close()
        continue
    print('recv: ' + client_msg)
    c.send('221 OK Bye!'.encode('utf-8'))

    c.close()
