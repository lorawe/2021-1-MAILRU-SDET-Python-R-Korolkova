import threading
import time

import requests
from flask import Flask, jsonify, request
import argparse

app = Flask(__name__)

SURNAME_DATA = {"testuser": "10"}
config = {}


@app.route(f'/post_user/<username>', methods=['POST'])
def post_user_surname(username):
    if id := SURNAME_DATA.get(username):
        json = jsonify({"vk_id": f'{id}'})
        response = f'Status: 304' \
                   f'Content-Type: application/json' \
                   f'Response: {json}'
        return response, 304
    else:
        last_user = max(SURNAME_DATA, key=SURNAME_DATA.get)
        if last_user:
            SURNAME_DATA[username] = last_user + 1

        else:
            SURNAME_DATA[username] = 0
        json = jsonify({"vk_id": f'{SURNAME_DATA[username]}'})
        response = f'Status: 200 OK' \
                   f'Content-Type: application/json' \
                   f'Response: {json}'
        return response, 200


@app.route(f'/vk_id/<username>', methods=['GET'])
def get_user_id(username):
    if id := SURNAME_DATA.get(username):
        json = jsonify({"vk_id": f'{id}'})
        response = f'Status: 200 OK' \
                   f'Content-Type: application/json' \
                   f'Response: {json}'
        return response, 200
    else:
        json = jsonify({})
        response = f'Status: 404 Not Found' \
                   f'Content-Type: application/json' \
                   f'Response: {json}'
        return response, 404


def run_mock(host, port):
    server = threading.Thread(target=app.run, kwargs={
        'host': host,
        'port': port
    })
    server.start()
    return server


def start_mock():
    run_mock(config["mock_host"], config["mock_port"])

    started = False
    st = time.time()
    while time.time() - st <= 5:
        try:
            requests.get(f'http://{config["mock_host"]}:{config["mock_port"]}')
            started = True
            break
        except ConnectionError:
            pass

    if not started:
        raise RuntimeError('Mock did not started in 5s!')


def shutdown_mock():
    terminate_func = request.environ.get('werkzeug.server.shutdown')
    if terminate_func:
        terminate_func()


def stop_mock():
    requests.get(f'http://{config["mock_host"]}:{config["mock_port"]}/shutdown')


@app.route('/')
def main():
    return 'This is mock service for vk_api'


@app.route('/shutdown')
def shutdown():
    shutdown_mock()
    return jsonify(f'OK, exiting'), 200


if __name__ == '__main__':
    config["mock_host"] = "localhost"
    config["mock_port"] = "8086"
    app.debug = False
    start_mock()
