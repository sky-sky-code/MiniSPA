from flask import Flask, jsonify, render_template
from flask_cors import CORS
from server.app.db.crud import all_data, filter_data, _add_data

app = Flask(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})

@app.route('/', methods=['GET'])
def all_voice():
    response_object = {'status': 'success', 'singleTable': all_data()}
    return jsonify(response_object)

@app.route('/<column>&<comparison>&<data_input>', methods=['GET'])
def filter_voice(column, comparison, data_input):
    response_object = {
        'status': 'success',
        'filterData': filter_data(column, comparison, data_input)
    }
    return jsonify(response_object)

if __name__ == "__main__":
    _add_data()
    app.run()