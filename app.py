from flask import Flask

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return 'Hello Fuckers'

@app.route('/home')
def home():
    return 'Home'

@app.route('/json')
def json():
    return 'Home'
