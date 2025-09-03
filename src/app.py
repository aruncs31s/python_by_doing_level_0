from flask import Flask
from levels import level_0
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, World!'



if __name__ == '__main__':
	app.run(debug=True)
