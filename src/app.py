from flask import Flask
from levels import level_0
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'

@app.route('/check')
def task():
	return level_0()


if __name__ == '__main__':
	app.run(debug=True)
