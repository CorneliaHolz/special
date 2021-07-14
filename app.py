from flask import Flask,request
import requests as rq 
app = Flask(__name__)

@app.route("/")
def index():
    return "<h1 style='color:pink'>blah blah blah</h1>"