#!/usr/bin/env python
from flask import Flask
import requests 
from flask import make_response
import json
import os 
from slacker import Slacker




app = Flask(__name__)

@app.route('/webhook',methods=[GET,POSTS])
def webhook():
    #req=requests.get_json(silent=True, force=True)

    # print("Requests:")
    # print(json.dump(req,indent=4))

    # res = processRequest(req)

    # res = json.dumps(res, indent=4)
    # r= make_response(res)
    # return r
    mailSend()

    
def mailSend():
    slack=Slacker('xoxp-450789184706-450695730467-585994880290-066e57ee2ee75f5a73ba63f90641059c')
    slack.chat.post_message(channel='technical',
                        text='Your system is being invaded',
                        username='rachitmanchandas',
                        icon_url='http://devarea.com/wp-content/uploads/2017/11/python-300x300.png')

        


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print("Starting app on port %d" % port)

    app.run(debug=False, port=port, host='0.0.0.0')
