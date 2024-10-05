# Creating the server:

# Import flask to create the server
from flask import Flask
import json

# Create the app
app = Flask(__name__)

# Create API Endpoint
#'/' is defining 'root' as in home page
@app.get("/") 
def home():
    return "Hello from Flask"
@app.get("/about")
def about():
    #Return name in JSON format (convert python to json for js webpage)
    me = {"name":"Clinton Hockenberry"}
    return json.dumps(me)

@app.get("/greet/<name>")
def greet(name):
    return f"""
    <h1 style='color:blue;text-align:center;'>
    Hello, {name}
    </h1>
    """

@app.get("/square/<int:number>")
def sqrt(number):
    return f"""
    <p style='font-size:20px;color:green;'>
    the square of {number} is {number*number}
    </p>
    """

@app.get("/farewell/<name>")
def farewell(name):
    return f"""
    <h2 style='color:black;'>
    Farewell, {name}
    </h2>
    """



# When code is saved, changes will be applied
app.run(debug=True)