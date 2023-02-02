from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, Tridis Madafakis por edhe karriakis"

