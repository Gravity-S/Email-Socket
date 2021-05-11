from socket import *
import base64
import json


class Mail:
    def __init__(self, send_to: str, subject: str, msg: str, **kwargs):
        self.subject: str = subject
        self.msg: str = msg
        self.send_to: str = send_to
        if ('mail' in kwargs):
            self.mail: str = kwargs['mail']
        else:
            self.mail: str = "979728128@qq.com"

        if ('pass_code' in kwargs):
            self.pass_code: str = kwargs['pass_code']
        else:
            self.pass_code: str = "qxcahfmwslmbbdaj"

        if ('smtp_server' in kwargs):
            self.smtp_server: str = kwargs['smtp_server']
        else:
            self.smtp_server: str = 'smtp.qq.com'

        if ('smtp_port' in kwargs):
            self.smtp_port: int = int(kwargs['smtp_port'])
        else:
            self.smtp_port: int = 25

    def SendMail(self):
        massage = "\r\n " + self.msg
        user = base64.b64encode(self.mail.encode('utf-8')).decode()
        code = base64.b64encode(self.pass_code.encode('utf-8')).decode()

        mail_server = (self.smtp_server, self.smtp_port)
        client = socket(AF_INET, SOCK_STREAM)
        client.settimeout(3)

        client.connect(mail_server)
        # recv = client.recv(1024)
        # print('recv:', recv)

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

        client.send(('MAIL FROM:<' + self.mail + '>\r\n').encode('utf-8'))
        recv = client.recv(1024)
        print('recv:', recv)

        client.send(('RCPT TO:<' + self.send_to + '>\r\n').encode('utf-8'))
        recv = client.recv(1024)
        print('recv:', recv)

        client.send('DATA\r\n'.encode('utf-8'))
        recv = client.recv(1024)
        print('recv:', recv)

        client.send(('FROM:<' + self.mail + '>\r\n').encode('utf-8'))
        client.send(('SUBJECT:' + self.subject + '\r\n').encode('utf-8'))
        client.send(massage.encode('utf-8'))
        client.send("\r\n.\r\n".encode('utf-8'))
        recv = client.recv(1024)
        print('recv:', recv)

        client.send("QUIT\r\n".encode('utf-8'))
        recv = client.recv(1024)
        print('recv:', recv)

        client.close()
        return self

    def SendLocal(self):
        massage = "\r\n " + self.msg

        mail_server = (gethostname(), 25)
        client = socket(AF_INET, SOCK_STREAM)
        client.settimeout(3)

        client.connect(mail_server)
        # recv = client.recv(1024)
        # print('recv:', recv)

        client.send('HELO Gravity\r\n'.encode('utf-8'))
        recv = client.recv(1024)
        print('recv:', recv)

        client.send(('MAIL FROM:<' + self.mail + '>\r\n').encode('utf-8'))
        recv = client.recv(1024)
        print('recv:', recv)

        client.send(('RCPT TO:<' + self.send_to + '>\r\n').encode('utf-8'))
        recv = client.recv(1024)
        print('recv:', recv)

        client.send('DATA\r\n'.encode('utf-8'))
        recv = client.recv(1024)
        print('recv:', recv)

        client.send(('SUBJECT:' + self.subject + '\r\n').encode('utf-8'))
        client.recv(1024)
        client.send(massage.encode('utf-8'))
        client.recv(1024)
        client.send("\r\n.\r\n".encode('utf-8'))
        recv = client.recv(1024)
        print('recv:', recv)

        client.send("QUIT\r\n".encode('utf-8'))
        recv = client.recv(1024)
        print('recv:', recv)

        client.close()
        return self

    def Save(self):
        mail_json = json.dumps({
            'send_to': self.send_to,
            'subject': self.subject,
            'msg': self.msg,
            'mail': self.mail,
            'smtp_server': self.smtp_server,
            'smtp_port': self.smtp_port
        })
        fp = open(r'Mail.txt', 'a', encoding='utf-8').write(mail_json + '\n')




# mail163 = 'gravitys2021@163.com'
# Code163 = 'EUFSZVCVXHSVLQKZ'
#
# subject = "wywnb"
# msg = "wywnbwywnbwywnbwywnbwywnbwywnbwywnbwywnbwywnb"
# send_to = "441656989@qq.com"
#
# M = Mail(subject=subject, msg=msg, send_to=send_to, mail=mail163, pass_code=Code163, through="163").SendMail()

# massage = "\r\n massage_massage_massage"
# mail_server = (gethostname(), 25)
# client = socket(AF_INET, SOCK_STREAM)
# client.settimeout(3)
#
# client.connect(mail_server)
# # recv = client.recv(1024)
# # print('recv:', recv)
#
# client.send('HELO Gravity\r\n'.encode('utf-8'))
# recv = client.recv(1024)
# print('recv:', recv)
#
# client.send(('MAIL FROM:<mail_mail_mail_mail>\r\n').encode('utf-8'))
# recv = client.recv(1024)
# print('recv:', recv)
#
# client.send(('RCPT TO:<send_to_send_to>\r\n').encode('utf-8'))
# recv = client.recv(1024)
# print('recv:', recv)
#
# client.send('DATA\r\n'.encode('utf-8'))
# recv = client.recv(1024)
# print('recv:', recv)
#
# client.send(('SUBJECT:subject_subject_subject\r\n').encode('utf-8'))
# client.send(massage.encode('utf-8'))
# client.send("\r\n.\r\n".encode('utf-8'))
# recv = client.recv(1024)
# print('recv:', recv)
#
# client.send("QUIT\r\n".encode('utf-8'))
# recv = client.recv(1024)
# print('recv:', recv)
#
# client.close()