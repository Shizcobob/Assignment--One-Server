from flask import Flask

app = Flask(__name__)

@app.route('/', defaults={'path': ''})

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/dojo')
def dojo():
    return "Dojo"

@app.route('/say/<name>')
def say(name):
    return f"Hi {name}"

@app.route('/hello/<string:tester>')
def hello(tester):
    return f"Hello {tester}"

@app.route('/repeat/<int:numba>/<string:theory>')
def repeat(numba, theory):
    return f"I love repeats {numba * theory}"


@app.route('/<path:path>')
def catch_all(path):
    return 'Sorry! No response. Try Again. Path entered not found: %s' % path

if __name__=="__main__":    
    app.run(debug=True)    

