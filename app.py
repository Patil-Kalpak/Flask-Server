
from flask import Flask,render_template
from flask import request
app = Flask(__name__)

@app.route("/")
def fun():
    return "Dhreuvesh | Kalpak | Mohit | Rohan"





