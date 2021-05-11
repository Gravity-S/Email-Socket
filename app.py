from flask import Flask, request, render_template
from sendmail import *
import json

app = Flask(__name__, static_folder='static')
ServerFlag = False

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/send_default', methods=['POST'])
def send_default():
    data = request.form
    Mail(subject=data['mail-subject'], msg=data['mail-content'], send_to=data['mail-to']).SendMail().Save()
    return json.dumps("SUCCESS")


@app.route('/send_custom', methods=['POST'])
def send_custom():
    data = request.form
    Mail(subject=data['mail-subject'], msg=data['mail-content'], send_to=data['mail-to'], mail=data['mail-from'],
             pass_code=data['mail-code'], smtp_server=data['smtp-server'], smtp_port=data['smtp-port']).SendMail().Save()
    return json.dumps("SUCCESS")


@app.route('/send_to_myself', methods=['POST'])
def send_to_myself():
    data = request.form
    Mail(subject=data['mail-subject'], msg=data['mail-content'], send_to="Local Smtp Server", mail=data['mail-from'],
         pass_code='', smtp_server='LocalHost', smtp_port='25').SendLocal().Save()
    return json.dumps("SUCCESS")

@app.route('/get_sent_mail', methods=['POST'])
def get_sent_mail():
    fp = open(r'Mail.txt', 'r', encoding='utf-8')
    mail_list = []
    m = fp.readline()
    while m is not '':
        mail_list.append(json.loads(m))
        m = fp.readline()
    return json.dumps(mail_list)

if __name__ == '__main__':
    app.run()