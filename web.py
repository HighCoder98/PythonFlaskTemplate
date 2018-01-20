#!/usr/bin/python
# -*- coding: utf-8 -*-

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    "GET /"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True, threaded=True, port=8000, host="0.0.0.0")
