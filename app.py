from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def index():
    data = {{'name' : 'Python'}, {'name': 'Colin'}, {'name': 'Kimi'}}
    return render_template('index.html', name="Colin", number=7 data=data)

@app.route('/home')
def home_get():
    return 'Home'

@app.route('/home', methods=['POST'])
def home_post():
    return 'Posted!'

@app.route('/json')
def json():
    return jsonify({'mykey' : 'JSON Value!', 'mylist' : [1, 2, 3, 4, 5]})

@app.route('/dynamic', defaults={'user_input' : 'Default!'})
@app.route('/dynamic/<user_input>')
def dyanmic(user_input):
    return f'The sring the user entered was: { user_input }'

@app.route('/query')
def query():
    user_input = request.args.get('user_input')
    second_input = request.args.get('second_input')
    return f'The query string contains: { user_input }'

@app.route('/form')
def form_get():
    return '<form method="POST><input type="text" name="user_input"><input type="submit"></form>'

@app.route('/form', methods=['POST'])
def form_post():
    return 