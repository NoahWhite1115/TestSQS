from flask import Flask, request
from queue_utils import get_queue, send_to_queue

app = Flask(__name__)
queue = get_queue('test_queue')

@app.route('/payload', methods = ['POST', 'GET'])
def handleWebhook():
    if request.method == 'POST':
        result = request.get_json()
        print("Got a post request")
        print(result)
        response = send_to_queue(queue, result)
        print(response)
        if 'Successful' in response:
            print("Success")
        for msg_meta in response['Failed']:
            print("Failed")
        return "success"

if __name__ == '__main__':
   app.run(host='0.0.0.0', port=80)