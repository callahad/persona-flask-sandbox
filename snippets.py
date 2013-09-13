# Make Pyflakes happy in the snippets file...
from flask import Flask, Response, abort, request, session
from requests import post
app = Flask(__name__)


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
