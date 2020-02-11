#!flask/bin/python
import json
from flask import Flask, Response
from helloworld.flaskrun import flaskrun

application = Flask(__name__)

@application.route('/', methods=['GET'])
def get():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

@application.route('/', methods=['POST'])
def post():
    return Response(json.dumps({'Output': 'Hello World'}), mimetype='application/json', status=200)

@application.route('/xss', methods =['GET'])
def XSS1():
    param = request.args.get('param', 'not set')

    html = open('xss.html').read()
    # check param
    # param = 'hello'
    resp = make_response(html.replace('{{ param }}', param))
    return resp

if __name__ == '__main__':
    flaskrun(application)
