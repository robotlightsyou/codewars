''' by convention flask apps are stored in a file named application.py '''

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", name="Emma")

@app.route("/hello")
def hello():
    name = request.args.get("name")
    return render_template("hello.html", name=name)
