#!/usr/bin/env python
from flask import Flask
import requests 
from flask_mail import Mail, Message
from conf import Config
import os 

app = Flask(__name__)

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

@app.route('/webhook',methods=['POST'])
def webhook():
    # req= requests.get_json(silent=True, force=True)

    # print("Requests:")
    # print(json.dump(req,indent=4))

    # res = processRequest(req)

    # res = json.dumps(res, indent=4)
    # r= make_response(res)
    # return r
    mailSend()

def mailSend():
    with app.app_context():
        msg = Message(subject="Hello",
            sender=app.config.get("MAIL_USERNAME"),
            recipients=["rachitmanchanda@yahoo.com"], 
            body="Hi")
        mail.send(msg)


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
