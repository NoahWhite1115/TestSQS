from flask import Flask

app = Flask(__name__)

@app.route('/payload', methods = ['POST', 'GET'])
def handleWebhook():
    if request.method == 'POST':
        result = request.get_json
        print("Got a post request")
        print(result)

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)