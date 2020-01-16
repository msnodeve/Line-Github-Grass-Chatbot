from flask import Flask, make_response, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello World!"


@app.route('/webhook', methods=['GET', 'POST'])
def webhook():
    return make_response(jsonify(results()))

def results():
    req = request.get_json(force=True)
    print(req)
    print('------------------------------')
    queryText = req.get('queryResult').get('outputContexts')
    address = queryText[0].get('parameters').get('address')
    color = queryText[0].get('parameters').get('color')
    size = queryText[0].get('parameters').get('size')
    response = \
        {
            'fulfillmentMessages' : [{
                'text' : {'text':
                          ["색 : " + color + " 사이즈 : " + size + " 주소 : " + address]}
            }]
        }
    return response

if __name__ == '__main__':
    app.run(debug=True, port=5000)