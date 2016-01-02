from flask import Flask, request, Response
import requests
import os

app = Flask(__name__)

apikey = os.environ.get('apikey')
apisecret = os.environ.get('apisecret')
phone = os.environ.get('phone')

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
            send_txt("Correct! Your next clue is: 00000001 00011010", number)
        else:
            send_txt("You got it wrong. " + text + " did not receive the Ray Mears book. Try again Becki.", number)

    except:
        pass

    return "hello world"

@app.route('/voice')
def voice():
    message = 'The slopes in America are much better than in Europe. The slopes in America are much better than in Europe.'
    xml = '<?xml version="1.0" encoding="UTF-8"?><vxml version = "2.1"><form><block><prompt>' + message + '</prompt></block></form></vxml>'
    return Response(xml, mimetype='text/xml')

if __name__ == '__main__':
    app.run()
