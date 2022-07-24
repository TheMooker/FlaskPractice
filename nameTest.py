from flask import Flask, request, make_response, redirect

app = Flask(__name__)

# Simple route for showing a 'Hello!' message
# @app.route('/')
# def index():
#     return '<h1>Hello!</h1>'


# Grabs the request header, User-Agent, and displays the info it contains on the root url page.
# "The User-Agent request header is a characteristic string that lets servers and network peers identify the application, 
# operating system, vendor, and/or version of the requesting user agent."
# https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/User-Agent
# request cannot be global since in a multithreaded server, multiple requests from multiple clients are happening simultaneously.
# each thread must see a different object in request.
@app.route('/', methods=["POST", "GET"])
def index():
    user_agent = request.headers.get('User-Agent')
    return '<p>Your browser is %s</p>' %user_agent

# creating a response object that also sets a cookie.
@app.route('/response', methods=['POST'])
def responseIndex():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '42')
    return response

# a redirect endpoint
@app.route('/redirect', methods=['POST', "GET"])
def redirectIndex():
    return redirect("http://example.com")

@app.route('/user/<name>', methods=["POST"])
def user(name):
    return '<h1>Hello, %s!</h1>' %name

if __name__ == 'main':
    app.run(debug=True)

