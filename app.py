from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/message')
def message():
    return 'Message'

@app.route('/voice')
def voice():
    return 'Voice'

if __name__ == '__main__':
    app.run()
