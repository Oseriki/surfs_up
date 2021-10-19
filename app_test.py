from flask import Flask

#create a new Flask instance
app = Flask(__name__)

#define the starting point, also known as the root
#forward slash inside of the app.route denotes that we want to put data at the root of routes
@app.route('/')
def hello_world():
    return 'Hello world'