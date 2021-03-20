from flask import request, jsonify
from app import app
from app.users.processor import Processor
from app.base.helper import header_option, check_session

PREFIX = '/api/user'


@app.route(PREFIX + '/login', methods=['GET', 'OPTIONS'])
def login():
    if request.method == 'OPTIONS':
        print(request.method)
        return jsonify({}), header_option()
    data = request.json
    print(f'data = {data}')
    return jsonify(Processor().login(data)), header_option()


@app.route(PREFIX + '/profile', methods=['GET', 'POST', 'OPTIONS'])
def register():
    if request.method == 'OPTIONS':
        return jsonify({}), header_option()
    data = {'id': check_session(request.headers)}
    if request.method == 'GET':
        return jsonify(Processor().get_profile(data)), header_option()
    data.update(request.json)
    print(f'data = {data}')
    return jsonify(Processor().update_profile(data)), header_option()


@app.route(PREFIX + '/swipe', methods=['GET', 'OPTIONS'])
def swipe():
    if request.method == 'OPTIONS':
        return jsonify({}), header_option()