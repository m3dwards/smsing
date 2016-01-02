from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

def send_txt(message, to):
    pass
    #https://rest.nexmo.com/sms/json?api_key=xxxxxxxx&api_secret=xxxxxxxx&to=xxxxxxxxxxxx&from=NexmoWorks&text=hello+from+Nexmo

@app.route('/message')
def message():
    #?msisdn=19150000001&to=12108054321
    #&messageId=000000FFFB0356D1&text=This+is+an+inbound+message
    #&type=text&message-timestamp=2012-08-19+20%3A38%3A23
    text = request.args.get('text')
    number = request.args.get('msisdn')
    
    if (text.lower() == "max"):
        return "Congratulations"
    
    return text + number

@app.route('/voice')
def voice():
    return 'Voice'

if __name__ == '__main__':
    app.run()
