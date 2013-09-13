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
    # Send the assertion to Mozilla's verifier service
    data = {"assertion": request.form["assertion"],
            "audience": "http://localhost:5000"}
    resp = post("https://verifier.login.persona.org/verify",
                data=data)
    info = resp.json()

    if info["status"] != "okay":
        abort(403)

    session["email"] = info["email"]
    return Response(status=204)


@app.route("/logout", methods=["POST"])
def logout():
    session.clear()
    return Response(status=204)


if __name__ == '__main__':
    app.run(debug=True)
