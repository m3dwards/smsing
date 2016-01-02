from flask import Flask, request
import requests
import os

app = Flask(__name__)

apikey = os.environ('apikey')
apisecret = os.environ('apisecret')
phone = os.environ('phone')

@app.route('/')
def hello_world():
    return 'Hello World!'

def send_txt(message, to):
    requests.get('https://rest.nexmo.com/sms/json?api_key=' + apikey + '&api_secret=' + apisecret + '&from=' + phone  + '&to=' + to + '&text=' + message)
    #https://rest.nexmo.com/sms/json?api_key=xxxxxxxx&api_secret=xxxxxxxx&to=xxxxxxxxxxxx&from=NexmoWorks&text=hello+from+Nexmo

@app.route('/message')
def message():
    
    try:
        #?msisdn=19150000001&to=12108054321
        #&messageId=000000FFFB0356D1&text=This+is+an+inbound+message
        #&type=text&message-timestamp=2012-08-19+20%3A38%3A23
        text = request.args.get('text')
        number = request.args.get('msisdn')
    
        if (text.lower() == "max"):
            send_txt("00000001 00011010", number)
        else:
            send_txt("You got it wrong. " + text + " did not receive the Ray Mears book. Try again Becki.", number)

    except:
        pass

    return "hello world"

@app.route('/voice')
def voice():
    return 'Voice'

if __name__ == '__main__':
    app.run()
