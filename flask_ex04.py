import json
from flask import Flask, request
import requests

app = Flask(__name__)

@app.route('/')
def hello():
    return os.getcwd()

@app.route('/send_post', methods=['GET'])
def send_post():
    params = {
        "param1":"test1",
        "params2":123,
        "params3":"한글"
        }
    res = requests.post('http://127.0.0.1:5000/post', data = json.dumps(params))
    return res.text


@app.route('/post', methods = ["POST"])
def post():
    params = json.loads(request.get_data(), encoding='utf-8')
    if len(params) == 0:
        return 'No parameter'
    
    params_str = ''
    for key in params.keys():
        params_str += 'key: {}, value: {}<br>'.format(key, params[key])
    return params_str

    
if __name__ == '__main__':
    app.run()