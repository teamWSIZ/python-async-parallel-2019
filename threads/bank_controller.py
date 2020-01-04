import threading

from flask import Flask, jsonify, request

from bank import Bank
from config import magic, server_port, server_host
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

bank = Bank()


@app.route('/')
@app.route('/status')
def get_json_data():
    return jsonify({'comment': f'Bank działa OK'})


@app.route('/funds/get')
def get_funds():
    return jsonify({'funds': bank.funds})


@app.route('/accounts/<accountid>/details')
def account(accountid):
    print(accountid)
    print(type(accountid))
    return 'Hello %s!' % accountid


@app.route('/funds/draw')
def draw_funds():
    amount = int(request.args.get('amount'))
    operation_OK = bank.draw_funds(amount)
    return jsonify({'OK': operation_OK, 'comment:': ''})


@app.route('/funds/add')
def add_funds():
    amount = int(request.args.get('amount'))
    operation_OK = bank.add_funds(amount)
    return jsonify({'OK': operation_OK, 'comment:': ''})


print(f'magic:{magic}')
app.run(host=server_host, port=server_port, debug=None, load_dotenv=False)  # can skip all args
