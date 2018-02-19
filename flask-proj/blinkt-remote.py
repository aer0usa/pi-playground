from flask import Flask
from flask import render_template
from blinktPatterns import doSweep, doFlash
import time

app = Flask(__name__)
#app.debug = True # Uncomment to debug

@app.route('/')
def home():
    doSweep()
    return render_template('hello.html',name='Sweep')

@app.route('/flash')
def flash():
    doFlash()
    return render_template('hello.html',name='Flash')

if __name__ == '__main__':
    app.run(host='0.0.0.0')

