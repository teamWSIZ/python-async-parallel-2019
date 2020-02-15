import json
import time
from typing import Dict
import threading

from flask import Flask, jsonify, request

from bazy_tutorial.a import get_all_users, get_all_users_with_name_prefix

app = Flask(__name__)


@app.route('/status')
def get_json_data():
    return jsonify({'comment': f'App działa OK'})


@app.route('/users')
def get_users():
    return jsonify(get_all_users())


@app.route('/users/details/<username>')
def get_users_by_name_prefix(username):
    return jsonify(get_all_users_with_name_prefix(username))


# # dostępna pod: http://localhost:5001/compute?a=10&b=0
# @app.route('/compute')
# def compute():
#     a = int(request.args.get('a'))
#     b = int(request.args.get('b'))
#     print(f'request a={a}, thread:{threading.current_thread().name}')
#     time.sleep(10.0)
#     if b == 0:
#         # teraz zwracamy komunikat o błędzie, oraz http error-code 400 (BAD_REQUEST)
#         return jsonify({'comment': 'b==0, cannot divide'}), 400
#     return jsonify({'sum': a + b, 'difference': a - b, 'division': a / b})
#
#
# # dostępna pod: http://localhost:5001/welcome/roadrunner/suffix/nice%20to%20meet%20you
# @app.route('/welcome/<username>/suffix/<message>')
# def welcome(username, message):
#     return jsonify({'comment': f'Hello {username}, {message}!'})


app.run(host='localhost', port=5001, debug=None, load_dotenv=False)  # can skip all args

# możliwa kompilacja do pojedynczego pliku wykonywalnego:
# `pyinstaller _zero.py -n my_flask_app --onefile
