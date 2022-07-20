from flask import Flask, request

app = Flask(__name__)

# @app.route('/')
# def index():
#     return '<h1>Hello!</h1>'

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' %user_agent


@app.route('/user/<name>')
def user(name):
    return '<h1>Hello, %s!</h1>' %name

if __name__ == 'main':
    app.run(debug=True)

