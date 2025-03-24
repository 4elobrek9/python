from flask import Flask, request
app = Flask(__name__)
@app.route("/login", methods=["POST"])
def login():
    return "Logged in"
if __name__ == "__main__":
    app.run()