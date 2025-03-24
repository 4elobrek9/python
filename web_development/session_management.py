from flask import Flask, session
app = Flask(__name__)
app.secret_key = "secret"
@app.route("/set")
def set_session():
    session["user"] = "Alice"
    return "Session set"
if __name__ == "__main__":
    app.run()