#!/usr/bin/env python

from flask import Flask, Response, abort, render_template, request, session
from requests import post

app = Flask(__name__)
app.secret_key = '\x88\xb6\x1f\x0e|6l\xfbhn\xd9\x9f\xc1\xca\x08-'


@app.route('/')
def index():
    return render_template('index.html')


@app.route("/login", methods=["POST"])
def login():
    # Verify assertion and then set a secure session cookie
    pass


@app.route("/logout", methods=["POST"])
def logout():
    # Destroy user's session cookie
    pass


if __name__ == '__main__':
    app.run(debug=True)
