from flask import Flask,request
import requests as rq 
app = Flask(__name__)

@app.route("/")
def index():
    return '<h1 style="color:pink">blah blah blah</h1><img src="https://17xxhp2l9bsg2qr0nd29eere-wpengine.netdna-ssl.com/wp-content/uploads/2020/12/mexico-df-6.jpg" alt="Mexico City Private Tour with official tour guide and private driver" jsname="HiaYvf" jsaction="load:XAeZkd;" class="n3VNCb" data-noaft="1" style="width: 450px; height: 320.25px; margin: 0px;">'


@app.route('/hype/<name>')
def hype(name):
    return f"{name} ist die Beste"


@app.route('/thanks/<name1>/<name2>')
def thanks(name1,name2):
    return f"{name1} thanks {name2}"
