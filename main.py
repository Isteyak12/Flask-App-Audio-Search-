from flask import Flask, render_template
from subprocess import Popen

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_app')
def start_app():
    Popen(['python', 'YT.py'])
    return "Voice Recognition App started"

if __name__ == '__main__':
    app.run(debug=True)
