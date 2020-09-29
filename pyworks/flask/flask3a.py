# python3

from flask import Flask, render_template

app = Flask(__name__, static_folder=".")

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/echo/<thing>/<place>")
def echo(thing, place):
    return render_template("flask3.html",thing=thing,place=place)

app.run(port=9999,debug=True)
