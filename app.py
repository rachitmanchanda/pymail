#!/usr/bin/env python
from flask import Flask
import requests 
from flask_mail import Mail, Message
from conf import Config
from flask import make_response
import json
import os 

app = Flask(__name__)

@app.route('/webhook',methods=['POST'])
def webhook():
    #req=requests.get_json(silent=True, force=True)

    # print("Requests:")
    # print(json.dump(req,indent=4))

    # res = processRequest(req)

    # res = json.dumps(res, indent=4)
    # r= make_response(res)
    # return r
    res = mailSend()
    res = json.dumps(res, indent=4)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def mailSend():
    mail_settings = {
    "MAIL_SERVER": 'smtp.gmail.com',
    "MAIL_PORT": 465,
    "MAIL_USE_TLS": False,
    "MAIL_USE_SSL": True,
    "MAIL_USERNAME": Config.EMAIL_USER,
    "MAIL_PASSWORD": Config.EMAIL_PASSWORD,
    }

    app.config.update(mail_settings)
    mail = Mail(app)

    with app.app_context():
        msg = Message(subject="Hello",
            sender=app.config.get("MAIL_USERNAME"),
            recipients=["rachitmanchanda@yahoo.com"], 
            body="Hi")
        mail.send(msg)
    return {
        "Success": "true"
    }


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
