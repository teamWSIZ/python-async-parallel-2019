from flask import Flask, jsonify, request
from bazy_tutorial.peewee_example import get_all_users, get_all_users_with_name_prefix, FakeUser, as_dict

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


@app.route('/users/upsert', methods=['POST'])
def upsert_user():
    print(f'got:{request.json}')
    data = request.json
    k = FakeUser(**data)
    k.save()
    return jsonify(as_dict(k))


app.run(host='localhost', port=5001, debug=None, load_dotenv=False)  # can skip all args

# możliwa kompilacja do pojedynczego pliku wykonywalnego:
# `pyinstaller _zero.py -n my_flask_app --onefile
