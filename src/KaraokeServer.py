from flask import Flask
from flask import request
from flask import jsonify
from switchController import runInput
from flask_cors import CORS, cross_origin
import sys

app = Flask(__name__)
cors = CORS(app, resources={r"/foo": {"origins": "*"}})
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route('/queue', methods = ['POST','OPTIONS'])
@cross_origin(origin='*',headers=['Content-Type','Authorization'])
def queue():
	data = request.json['number']
	arr = map(int, str(data))
	runInput(arr)
	return data

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0', port=5000)