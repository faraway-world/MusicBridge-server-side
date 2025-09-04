from flask import Flask, request
from rpc_handler import update_presence

app = Flask(__name__)

@app.route("/update", methods=["POST"])
def update():
    data = request.json
    title = data.get("title")
    artist = data.get("artist")

    if not title or not artist:
        return "Missing fields", 400

    update_presence(title, artist)
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
