"""
Helloworld.py.

Pretty simple hello world flask app to demonstrate the EE  exercise.
Slightly overcomplicated to demonstrate following requests.
"""

import socket
import datetime
from flask import Flask
from flask import jsonify
from flask import request
from multiprocessing import Value

app = Flask(__name__)
requests = Value('i', 0)


@app.route('/', methods=['GET'])
def HelloWorld():
    """Sample catchall for this webserver"""
    with requests.get_lock():
        requests.value += 1
    return jsonify({
        'message': 'Hello World!',
        'requests_counter': requests.value,
        'timestamp': datetime.datetime.utcnow(),
        'server_hostname': socket.gethostname(),
        'client_ip_address': request.environ['REMOTE_ADDR']
    }), 200


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9000)
