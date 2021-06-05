import threading

from flask import Flask, jsonify, request

import settings

app = Flask(__name__)

SURNAME_DATA = {}


@app.route('/get_surname/<name>', methods=['GET'])
def get_user_surname(name):
    if surname := SURNAME_DATA.get(name):
        return jsonify(surname), 200
    else:
        return jsonify(f'Surname for user {name} not fount'), 404


@app.route('/put_surname/<name>/<surname>', methods=['PUT'])
def put_user_surname(name, surname):
    if old_surname := SURNAME_DATA.get(name):
        SURNAME_DATA[name] = surname
        return jsonify(SURNAME_DATA), 200
    else:
        return jsonify(f'Surname for user {name} not found'), 404


@app.route('/post_surname/<name>/<surname>', methods=['POST'])
def post_user_surname(name, surname):
    if result := SURNAME_DATA.get(name):
        return jsonify(f'Surname for user {name} was created with {surname}'), 304
    else:
        SURNAME_DATA[name] = surname
        return jsonify(name, surname), 200


@app.route('/delete_surname/<name>/<surname>', methods=['DELETE'])
def delete_user_surname(name):
    if surname := SURNAME_DATA.get(name):
        SURNAME_DATA.pop(name)
        return jsonify(name), 200
    else:
        return jsonify(f'Surname for user {name} not found'), 404


def run_mock():
    server = threading.Thread(target=app.run, kwargs={
        'host': settings.MOCK_HOST,
        'port': settings.MOCK_PORT
    })
    server.start()
    return server


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'OK, exiting'), 200
