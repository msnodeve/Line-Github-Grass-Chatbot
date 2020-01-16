from flask import Flask, request

app = Flask(__name__)


@app.route('/query')
def index():
    args = request.args
    result = args.get('id')
    insert()
    return "Hello, " + result


@app.route('/path/<param1>/<param2>')
def path_param(param1, param2):
    return param1 + "   :   " + param2


@app.route('/body', methods=['POST'])
def request_body():
    body = request.json
    id = body['id']
    name = body['name']

    return "ID : " + str(id) + ", name : " + name


if __name__ == '__main__':
    app.run(debug=True)
