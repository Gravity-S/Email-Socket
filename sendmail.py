from socket import *
import base64


def SendMail(title: str, msg: str, send_to: str, mail: str = "979728128@qq.com", pass_code: str = "qxcahfmwslmbbdaj",
             through: str = 'qq'):
    massage = "\r\n " + msg
    user = base64.b64encode(mail.encode('utf-8')).decode()
    code = base64.b64encode(pass_code.encode('utf-8')).decode()

    mail_server = ("smtp." + through + ".com", 25)
    client = socket(AF_INET, SOCK_STREAM)
    client.connect(mail_server)
    recv = client.recv(1024)
    print('recv:', recv)

    client.send('HELO Gravity\r\n'.encode('utf-8'))
    recv = client.recv(1024)
    print('recv:', recv)

    client.send('AUTH LOGIN\r\n'.encode('utf-8'))
    recv = client.recv(1024)
    print('recv:', recv)

    client.send((user + '\r\n').encode('utf-8'))
    recv = client.recv(1024)
    print('recv:', recv)

    client.send((code + '\r\n').encode('utf-8'))
    recv = client.recv(1024)
    print('recv:', recv)

    client.send(('MAIL FROM:<' + mail + '>\r\n').encode('utf-8'))
    recv = client.recv(1024)
    print('recv:', recv)

    client.send(('RCPT TO:<' + send_to + '>\r\n').encode('utf-8'))
    recv = client.recv(1024)
    print('recv:', recv)

    client.send('DATA\r\n'.encode('utf-8'))
    recv = client.recv(1024)
    print('recv:', recv)

    client.send(('FROM:<' + mail + '>\r\n').encode('utf-8'))
    client.send(('SUBJECT:' + title + '\r\n').encode('utf-8'))
    client.send(massage.encode('utf-8'))
    client.send("\r\n.\r\n".encode('utf-8'))
    recv = client.recv(1024)
    print('recv:', recv)

    client.send("QUIT\r\n".encode('utf-8'))
    recv = client.recv(1024)
    print('recv:', recv)

    client.close()


# mail163 = 'gravitys2021@163.com'
# Code163 = 'EUFSZVCVXHSVLQKZ'
#
# title = "测试标题"
# msg = "一二三四五六七，发福发方法窿"
# send_to = "979728128@qq.com"
# SendMail(title=title, msg=msg, send_to=send_to, mail=mail163, pass_code=Code163, through="163")
