# import the Flask dependency
from flask import Flask

# Create a New Flask App Instance
app = Flask(__name__)

# let's create our first route!
# Next, create a function called hello_world(). 
# Whenever you make a route in Flask, you put the code you want in that specific route below @app.route(). 
@app.route('/')
def hello_world():
    return 'Hello world'