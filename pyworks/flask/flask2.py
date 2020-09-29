from flask import Flask, render_template

app = Flask(__name__, static_folder=".")

@app.route("/")
def home():
    return app.send_static_file("index.html")

@app.route("/echo/<thing>")
def echo(thing):
    return render_template("flask2.html",thing = thing)

app.run(port=9999,debug=True)